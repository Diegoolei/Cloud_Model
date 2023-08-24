import itertools
from init import InitialConditions
import pandas as pd
from constants import m_const
from data_structs import Main_structs
from shared_data import Main_vars
import numpy as np
from turbu import turbu1, turbu2, inomo


# Función principal
def modelo():
    # Inicializar condiciones iniciales
    i_c = InitialConditions()
    m_s = Main_structs()
    # Inicializar variables
    titaa_init(m_s)
    for tt in range(1, m_const.LT1 + 1):
        # Inicializar variables
        m_s.main_vars[tt] = Main_vars()
        array_init(m_s, tt)

        # Calcular dinámica y termodinámica
        for k in range(1, m_const.NZ1):
            n = k
            dden0z = (i_c.gwc.Den0[k + 1] - i_c.basic_struct.Den0[k - 1]) / i_c.basic_struct.Den0[k]
            turbu1(n)
        for i in range(1, m_const.NX1):
            ls = i
            for j in range(1, m_const.NX1):
                m = j
                turbu2(ls, m, n)
                inomo(ls, m, n, dden0z)

                # Calcular energía cinética
                ener1 = 0.0
                ener1 += 0.5 * i_c.basic_struct.Den0[k] * (
                    i_c.gwc.U2[i][j][k] ** 2.0
                    + i_c.gwc.V2[i][j][k] ** 2.0
                    + i_c.gwc.W2[i][j][k] ** 2.0
                )
    return 0


def array_init(m_s: Main_structs, i_c: InitialConditions):
    for i, j in itertools.product(range(m_const.NX1), range(m_const.NX1)):
        m_s.advvap1[i][j] = (
            i_c.gwc.W2[i][j][1]
            * (i_c.gwc.Qvap1[i][j][1] + i_c.gwc.Qvap1[i][j][0])
            / 4.0
        )
        m_s.advgot1[i][j] = 0.0
        m_s.advllu1[i][j] = i_c.gwc.W2[i][j][1] * i_c.gwc.Qllu1[i][j][1]
        if i_c.gwc.W2[i][j][1] > 0:
            m_s.advllu1[i][j] = 0.0
        m_s.advaer1[i][j] = (
            i_c.gwc.W2[i][j][1]
            * (i_c.gwc.aer1[i][j][1] + i_c.gwc.aer1[i][j][0])
            / 4.0
        )
        if i_c.gwc.W2[i][j][1] < 0:
            m_s.advaer1[i][j] = m_s.advaer1[i][j] * 1.5
        m_s.advcri1[i][j] = 0.0
        m_s.advnie1[i][j] = i_c.gwc.W2[i][j][1] * i_c.gwc.Qnie1[i][j][1]
        if i_c.gwc.W2[i][j][1] > 0:
            m_s.advnie1[i][j] = 0.0
        m_s.advgra1[i][j] = i_c.gwc.W2[i][j][1] * i_c.gwc.Qgra1[i][j][1]
        if i_c.gwc.W2[i][j][1] > 0:
            m_s.advgra1[i][j] = 0.0


def titaa_init(m_s):
    for i, j, k in itertools.product(
        range(m_const.NX1), range(m_const.NX1), range(m_const.NZ1)
    ):
        m_s.Titaa1[i][j][k] += 0.8 * np.exp(
            -((i - 35) ** 2.0 + (j - 25.5) ** 2.0 + (k - 8) ** 2.0) / 50.0
        )
        m_s.Titaa2[i][j][k] += 0.8 * np.exp(
            -((i - 35) ** 2.0 + (j - 25.5) ** 2.0 + (k - 8) ** 2.0) / 50.0
        )


modelo()
