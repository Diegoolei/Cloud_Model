import scipy.constants as const


# Constants (CONST.I)
class m_const():
    PI = const.pi
    G = const.gravitational_constant

    GAM1P8 = 0.9134
    GAM2P8 = 1.6765
    GAM3P8 = 4.6941742
    GAM4P8 = 17.837862

    RD = 287.04
    RV = 461.05
    KAPA = 0.2857
    EPS = 0.622646
    T0 = 273.15
    P00 = 101300
    KAIR = 2.40e-2
    CWL = 4218.0
    CWV = 1839.0
    CWI = 2106.0
    LVL0 = 2.500e6
    LSL0 = 79.7
    LVS0 = 2.835e6
    CP = 1003.0
    CV = 716.0
    ELVS0 = 610.78
    ESVS0 = 610.918

    DV0 = 2.11e-5
    VIS0 = 1.718e-5
    RHOW = 1000.0
    RHOCRI = 900.0
    RHONIE = 100.0
    RHOGRA = 500.0
    N0GOT = 2.9e24
    N0LLU = 4912189.0
    N0NIE = 1.66e5
    N0GRA = 310.0
    AV0 = 1455.0
    VTNIE0 = 0.5
    EFCOL = 0.8
    EFCOLGN = 0.7


# Constants (DIMEN.I)

    NX1 = 50
    NZ1 = 45
    NZ = 64
    DX1 = 300.0
    DT1 = 2.0
    DT2 = 1.0
    DT3 = 0.2


# Constants (INICIO11.I)

    CENTX = (NX1 + 1.0) * DX1 / 2.0  # Coord x de la perturbacion inicial
    CENTY = (NX1 + 1.0) * DX1 / 2.0  # Coord y de la perturbacion inicial
    CENTZ = 0.0  # Coord z de la perturbacion inicial
    CENAERX = (NX1 + 1.0) * DX1 / 2.0 + 4000.0  # Coord x de la perturbacion de aerosoles
    CENAERY = (NX1 + 1.0) * DX1 / 2.0 + 1000.0  # Coord y de la perturbacion de aerosoles
    CENAERZ = 0.0  # Coord z de la perturbacion de aerosoles
    SIGMAT = 2 * 1000.0**2.0  # Decaimiento en z de la perturbacion en T
    SIGMAA = 200.0**2.0  # Decaimiento en z de la perturbacion en A
    RADIOMED = 2000.0  # Ancho de la perturbacion
    TEMPER = 0.7  # Perturbacion maxima de temperatura
    AERPER = 10000.0  # Perturbacion maxima de aerosoles

    A0 = 6.10780
    A1 = 4.43652e-1
    A2 = 1.42895e-2
    A3 = 2.65065e-4
    A4 = 3.03124e-6
    A5 = 2.03408e-8
    A6 = 6.13682e-11

    B0 = 6.10918
    B1 = 5.03470e-1
    B2 = 1.88601e-2
    B3 = 4.17622e-4
    B4 = 5.82472e-6
    B5 = 4.83880e-8
    B6 = 1.83883e-10

# Constants (INICIO.F)
    NX4 = 500
    VC = 1.5 / 3000**2
    VH = 5000 / PI
