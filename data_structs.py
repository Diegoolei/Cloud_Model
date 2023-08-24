import numpy as np
from constants import m_const


class Main_structs():
    def __init__(self):
        self.Titaa1 = np.zeros(m_const.NX1, m_const.NX1, m_const.NZ1)
        self.Titaa2 = np.zeros(m_const.NX1, m_const.NX1, m_const.NZ1)
        self.main_vars = np.zeros(m_const.LT1 + 1, dtype=object)
        self.advaer1 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advaer2 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advgot1 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advgot2 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advllu1 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advllu2 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advcri1 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advcri2 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advnie1 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advnie2 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advgra1 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advgra2 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advvap1 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)
        self.advvap2 = np.zeros(m_const.NX1 + 4, m_const.NX1 + 3)


# Estructuras Basicas (ESTBAS.I)
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


#
class t_structs():
    def __init__(self):
        self.Tvis = np.zeros(111)
        self.Tlvl = np.zeros(111)
        self.Tlsl = np.zeros(111)
        self.Tlvs = np.zeros(111)
        self.Telvs = np.zeros(111)
        self.Tesvs = np.zeros(111)
        self.Eautcn = np.zeros(111)
        self.Eacrcn = np.zeros(111)
        self.Tk = np.zeros(111)


#
class good_weather_conditions():
    def __init__(self):
        self.Pres1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Pres2 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Titaa1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Qvap1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.aer1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.U2 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.V1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.V2 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.W1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.W2 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Qvap2 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Qgot1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Qgot2 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Qllu1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Qllu2 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Qcri1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Qcri2 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Qnie1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Qnie2 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Qgra1 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.Qgra2 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))
        self.aer2 = np.zeros((m_const.NX1 + 4, m_const.NX1 + 3, m_const.NZ1 + 4))


class terminal_speed():
    def __init__(self):
        self.Av = np.zeros(2 * m_const.NZ1 + 9)
        self.Vtnie = np.zeros(2 * m_const.NZ1 + 9)
        self.Vtgra0 = np.zeros(2 * m_const.NZ1 + 9)
