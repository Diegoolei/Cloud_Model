# Estructuras Basicas (ESTBAS.I)
import numpy as np
from constants import m_const


class basic_structs():
    def __init__(self):
        self.Temp0 = np.zeros(m_const.NZ1 + 7)
        self.Tita0 = np.zeros(m_const.NZ1 + 7)
        self.Pres00 = np.zeros(m_const.NZ1 + 7)
        self.Presi0 = np.zeros(m_const.NZ1 + 7)
        self.UU = np.zeros(m_const.NZ1 + 7)
        self.VV = np.zeros(m_const.NZ1 + 7)
        self.cc2 = np.zeros(m_const.NZ1 + 7)
        self.Den0 = np.zeros(m_const.NZ1 + 7)
        self.aer0 = np.zeros(m_const.NZ1 + 7)
        self.Qvap0 = np.zeros(m_const.NZ1 + 7)
        self.Qvaprel = np.zeros(m_const.NZ1)
        self.aerrel = np.zeros(m_const.NZ1)


class t_structs():
    def __init__(self):
        self.Tvis = np.zeros(3)
        self.Tlvl = np.zeros(3)
        self.Tlsl = np.zeros(3)
        self.Tlvs = np.zeros(3)
        self.Telvs = np.zeros(3)
        self.Tesvs = np.zeros(3)
        self.Eautcn = np.zeros(3)
        self.Eacrcn = np.zeros(3)
        self.Tk = np.zeros(3)


class good_weather_conditions():
    def __init__(self):
        self.Pres1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 4, m_const.NZ1 + 4))
        self.Pres2 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 4, m_const.NZ1 + 4))
        self.Titaa1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 4, m_const.NZ1 + 4))
        self.Qvap1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 4, m_const.NZ1 + 4))
        self.aer1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 4, m_const.NZ1 + 4))


class terminal_speed():
    def _init_(self):
        self.Av = np.zeros(2 * m_const.NZ1 + 9)
        self.Vtnie = np.zeros(2 * m_const.NZ1 + 9)
        self.Vtgra0 = np.zeros(2 * m_const.NZ1 + 9)