import numpy as np
from constants import m_const
from data_structs import (
    basic_structs,
    t_structs,
    good_weather_conditions,
    terminal_speed,
)


class InitialConditions:
    # basic_structs
    basic_struct = basic_structs()
    t_struct = t_structs()
    gwc = good_weather_conditions()
    terminal_speed = terminal_speed()

    def __init__(self):
        self.PP()
        self.viento_corte()
        self.constantes_T()
        self.condiciones_buen_tiempo()
        self.terminal_vel_rain_drop()
        self.terminal_vel_snow()
        self.terminal_vel_granite()

    def PP(self):
        integ = np.zeros(m_const.NX4 + 2)
        for k in range(m_const.NX4):
            zetaa = (2 * k - 2) * m_const.DX1 / 4
            zetam = (2 * k - 1) * m_const.DX1 / 4
            zetad = (2 * k) * m_const.DX1 / 4
            ya = 1 / self.TT(zetaa)
            ym = 1 / self.TT(zetam)
            yd = 1 / self.TT(zetad)
            integ[k] = integ[k - 1] + ya + 4 * ym + yd

        for k in range(m_const.NZ + 2):
            self.basic_struct.Presi0[k] = m_const.P00 * np.exp(
                -m_const.G / m_const.RD * integ[2 * k] * m_const.DX1 / 4 / 3
            )

        self.basic_struct.Presi0[0] = m_const.P00
        self.basic_struct.Presi0[-1] = m_const.P00

    def TT(self, zeta):
        a = 298.15
        if zeta <= 2000:
            return a - 9e-3 * zeta
        elif zeta <= 5500:
            xx = zeta - 2000
            return a - 18 - xx * (9e-3 - 2e-3 * xx / 3500 / 2)
        elif zeta <= 9000:
            xx = zeta - 5500
            return a - 46 - 7e-3 * xx
        elif zeta <= 11000:
            xx = zeta - 9000
            return a - 70.5 - 7e-3 * xx + 1.75e-6 * xx**2
        elif zeta <= 12000:
            return a - 77.5
        else:
            xx = zeta - 12000
            return a - 77.5 + 50 * (xx / 9000) ** 2

    def viento_corte(self):
        for k in range(m_const.NZ):
            zeta = k * m_const.DX1
            if zeta <= 500:
                self.basic_struct.UU[k] = 0
                self.basic_struct.VV[k] = 0
            elif zeta <= 2000:
                zeta1 = zeta - 500
                aux = 4 * (zeta1 / 1500) ** 2
                self.basic_struct.UU[k] = aux
                self.basic_struct.VV[k] = 0
            elif zeta <= 9000:
                zeta1 = zeta - 2000
                vb = zeta1 / 7000
                self.basic_struct.UU[k] = 4 - 10 * vb**2
                self.basic_struct.VV[k] = 3 * vb**0.5
            else:
                zeta1 = zeta - 9000
                self.basic_struct.UU[k] = -6 + 4 * (zeta1 / 9000) ** 2
                self.basic_struct.VV[k] = 3 - 5 * (zeta1 / 9000) ** 0.5

            self.basic_struct.UU[k] = self.basic_struct.UU[k] * 0.7
            self.basic_struct.VV[k] = self.basic_struct.VV[k] * 0

    def constantes_T(self):
        value_list = [313, 203, -1]

        for k in value_list:
            self.t_struct.Tk[k] = k - m_const.T0
            self.t_struct.Tvis[k] = 4.9e-8 * self.t_struct.Tk[k] + m_const.VIS0
            if k < 273.15:
                self.t_struct.Tvis[k] = (
                    self.t_struct.Tvis[k] - 1.2e-10 * self.t_struct.Tk[k] ** 2
                )

            # calores latentes de evaporacion, fusion y sublimacion
            gam = 0.167 + 3.67e-4 * k
            self.t_struct.Tlvl[k] = m_const.LVL0 * (self.T0 / k) ** gam
            self.t_struct.Tlsl[k] = (
                m_const.LSL0
                + 0.485 * self.t_struct.Tk[k]
                - 2.5e-3 * self.t_struct.Tk[k] ** 2
            ) * 4180
            self.t_struct.Tlvs[k] = self.t_struct.Tlvl[k] + self.t_struct.Tlsl[k]

            # tension de vapor de saturacion liquido y solido
            aux = m_const.A3 + self.t_struct.Tk[k] * (
                m_const.A4
                + self.t_struct.Tk[k] * (m_const.A5 + self.t_struct.Tk[k] * m_const.A6)
            )
            aux = 0 + self.t_struct.Tk[k] * (
                m_const.A1
                + self.t_struct.Tk[k] * (m_const.A2 + self.t_struct.Tk[k] * aux)
            )
            self.t_struct.Telvs[k] = aux * 100

            aux = m_const.B3 + self.t_struct.Tk[k] * (
                m_const.B4
                + self.t_struct.Tk[k] * (m_const.B5 + self.t_struct.Tk[k] * m_const.B6)
            )
            aux = m_const.B0 + self.t_struct.Tk[k] * (
                m_const.B1
                + self.t_struct.Tk[k] * (m_const.B2 + self.t_struct.Tk[k] * aux)
            )
            self.t_struct.Tesvs[k] = aux * 100

            if k < 220:
                aux = self.t_struct.Tlvl[220] / m_const.RV * (1 / 220 - 1 / k)
                self.t_struct.Telvs[k] = self.t_struct.Telvs[220] * np.exp(aux)
                aux = self.t_struct.Tlvs[220] / m_const.RV * (1 / 220 - 1 / k)
                self.t_struct.Tesvs[k] = self.t_struct.Tesvs[220] * np.exp(aux)

            self.t_struct.Eautcn[k] = 10 ** (0.035 * self.t_struct.Tk[k] - 0.7)
            self.t_struct.Eacrcn[k] = np.exp(0.09 * self.t_struct.Tk[k])

    def recalc_presion_y_tita(self):
        Press00 = self.PP2()
        for k in range(self.nz1):
            self.basic_struct.Tita0[k] = (
                self.basic_struct.Temp0[k] * (m_const.P00 / Press00[k]) ** m_const.KAPA
            )
            self.basic_struct.Pres00[k] = (
                self.basic_struct.Temp0[k] / self.basic_struct.Tita0[k]
            )
            self.basic_struct.cc2[k] = (
                m_const.CP
                * m_const.RD
                * self.basic_struct.Tita0[k]
                * self.basic_struct.Pres00[k]
                / m_const.CV
            )

        self.basic_struct.Tita0[-1] = self.basic_struct.Tita0[0]
        self.basic_struct.Pres00[-1] = self.basic_struct.Pres00[0]
        self.basic_struct.Den0[-1] = self.basic_struct.Den0[0]
        self.basic_struct.Qvap0[-1] = 0

        for i in range(1, m_const.NX1):
            for j in range(1, m_const.NX1):
                self.Pres1[i, j, 0] = self.Pres1[i, j, 1]
                self.Pres1[i, j, -1] = self.Pres1[i, j, 1]
                self.Pres2[i, j, 0] = self.Pres1[i, j, 1]
                self.Pres2[i, j, -1] = self.Pres1[i, j, 1]
                self.Titaa1[i, j, 0] = self.Titaa1[i, j, 1]
                self.Titaa1[i, j, -1] = self.Titaa1[i, j, 1]
                self.Qvap1[i, j, 0] = self.Qvap1[i, j, 1]
                self.Qvap1[i, j, -1] = self.Qvap1[i, j, 1]

        Qvaptot = 0
        for k in range(m_const.NZ1):
            Qvaptot += self.basic_struct.Qvap0[k]
            self.basic_struct.Qvaprel[k] = self.basic_struct.Qvap0[k] / Qvaptot

        aertot = 0
        for k in range(m_const.NZ1):
            aertot += self.basic_struct.aer0[k]
            self.basic_struct.aerrel[k] = self.basic_struct.aer0[k] / aertot

    def PP2(self):
        Den00 = np.zeros(2 * m_const.NZ1 + 2)
        integ = np.zeros(2 * m_const.NZ1 + 2)
        for k in range(m_const.NZ1):
            Den00[2 * k] = self.basic_struct.Den0[k]
            Den00[2 * k + 1] = (
                self.basic_struct.Den0[k] + self.basic_struct.Den0[k + 1]
            ) / 2

        Den00[2 * m_const.NZ1] = self.basic_struct.Den0[m_const.NZ1]
        Den00[2 * m_const.NZ1 + 1] = (
            2 * self.basic_struct.Den0[m_const.NZ1] - Den00[2 * m_const.NZ1 - 1]
        )

        integ[0] = 0
        for k in range(1, m_const.NZ1):
            ya = Den00[2 * k - 1]
            ym = Den00[2 * k]
            yd = Den00[2 * k + 1]
            integ[k] = integ[k - 1] + ya + 4 * ym + yd

        for k in range(1, m_const.NZ1):
            self.basic_struct.Pres00[k] = (
                m_const.P00 - m_const.G * integ[k] * m_const.DX1 / 6
            )

        self.basic_struct.Pres00[0] = m_const.P00
        self.basic_struct.Pres00[-1] = m_const.P00

    def condiciones_buen_tiempo(self):
        for k in range(m_const.NZ1 + 2):
            zeta = k * m_const.DX1
            self.basic_struct.Temp0[k] = self.TT(zeta)
            self.basic_struct.Den0[k] = (
                self.basic_struct.Presi0[k] / m_const.RD / self.basic_struct.Temp0[k]
            )
            self.basic_struct.Tita0[k] = (
                self.basic_struct.Temp0[k]
                * (m_const.P00 / self.basic_struct.Presi0[k]) ** m_const.KAPA
            )
            self.basic_struct.Pres00[k] = (
                self.basic_struct.Temp0[k] / self.basic_struct.Tita0[k]
            )
            self.basic_struct.aer0[k] = 10000 * np.exp(-zeta / 2500)

        self.basic_struct.Temp0[-1] = self.basic_struct.Temp0[0]
        self.basic_struct.Den0[-1] = self.basic_struct.Den0[0]
        self.basic_struct.Tita0[-1] = self.basic_struct.Tita0[0]
        self.basic_struct.Pres00[-1] = self.basic_struct.Pres00[0]
        self.basic_struct.aer0[-1] = -self.basic_struct.aer0[0]

        for k in range(m_const.NZ1 + 1):
            zeta = k * m_const.DX1
            for i in range(m_const.NX1 + 1):
                equis = i * m_const.DX1
                for j in range(m_const.NX1 + 1):
                    ygrie = j * m_const.DX1
                    G1 = np.exp(
                        -((m_const.CENTX - equis) ** 2 + (m_const.CENTY - ygrie) ** 2)
                        / m_const.RADIOMED**2
                    )
                    self.gwc.Titaa1[i, j, k] = (
                        m_const.TEMPER
                        * np.exp(-((zeta - m_const.CENTZ) ** 2) / m_const.SIGMAT)
                        * G1
                    )
                    if self.gwc.Titaa1[i, j, k] < 1e-5:
                        self.gwc.Titaa1[i, j, k] = 0

                    G1 = np.exp(
                        -(
                            (m_const.CENAERX - equis) ** 2
                            + (m_const.CENAERY - ygrie) ** 2
                        )
                        / m_const.RADIOMED**2
                    )
                    self.gwc.aer1[i, j, k] = (
                        m_const.AERPER * np.exp(-(zeta**2) / m_const.SIGMAA) * G1
                    )

            if zeta <= 500:
                rel = 0.55 + 0.05 * zeta / 500
            elif zeta <= 1500:
                rel = 0.6
            elif zeta <= 4000:
                rel = 0.6 - (zeta - 1500) / 2500 * 0.25
            elif zeta <= 7000:
                rel = 0.35 - (zeta - 4000) / 3000 * 0.25
            else:
                rel = 0.1 - (zeta - 7000) / 3000 * 0.02

            n = int(self.basic_struct.Temp0[k])
            aux = self.basic_struct.Temp0[k] - n
            elv = self.t_struct.Telvs[n] * (1 - aux) + self.t_struct.Telvs[n + 1] * aux

            self.basic_struct.Qvap0[k] = (
                rel * elv / m_const.RV / self.basic_struct.Temp0[k]
            )

            # recalculo de la densidad
            self.basic_struct.Den0[k] += self.basic_struct.Qvap0[k]

    def terminal_vel_rain_drop(self):
        for k in range(m_const.NZ1 + 1):
            self.terminal_speed.Av[2 * k - 1] = (
                m_const.AV0
                * (
                    (m_const.P00 / self.basic_struct.Presi0[k - 1]) ** 0.286
                    + (m_const.P00 / self.basic_struct.Presi0[k]) ** 0.286
                )
                / 2
            )
            self.terminal_speed.Av[2 * k] = (
                m_const.AV0 * (m_const.P00 / self.basic_struct.Presi0[k]) ** 0.286
            )

    def terminal_vel_snow(self):
        for k in range(m_const.NZ1 + 1):
            self.terminal_speed.Vtnie[2 * k - 1] = (
                m_const.VTNIE0
                * (
                    (m_const.P00 / self.basic_struct.Presi0[k - 1]) ** 0.3
                    + (m_const.P00 / self.basic_struct.Presi0[k]) ** 0.3
                )
                / 2
            )
            self.terminal_speed.Vtnie[2 * k] = (
                m_const.VTNIE0 * (m_const.P00 / self.basic_struct.Presi0[k]) ** 0.3
            )

    def terminal_vel_granite(self):
        for k in range(m_const.NZ1 + 1):
            aux = 2.754 * m_const.RHOGRA**0.605
            self.terminal_speed.Vtgra0[2 * k] = (
                aux
                / self.t_struct.Tvis(self.basic_struct.Temp0[k]) ** 0.21
                / self.basic_struct.Den0[k] ** 0.395
            )

        for k in range(1, m_const.NZ1 + 1):
            self.terminal_speed.Vtgra0[2 * k - 1] = (
                self.terminal_speed.Vtgra0[2 * k - 2]
                + self.terminal_speed.Vtgra0[2 * k]
            ) / 2
