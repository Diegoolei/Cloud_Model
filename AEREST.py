import itertools
import numpy as np
import multiprocessing


class Dimension:
    nz1 = 101
    nombre = "31"
    paso = "10"
    file_name = f"nube{nombre}{paso}.sal"

    def __init__(self):
        self.aerm = np.zeros(self.nz1)
        self.imax = np.zeros(self.nz1)
        self.jmax = np.zeros(self.nz1)
        self.max_aer_perturbation = np.zeros(self.nz1)

        self.vapm = np.zeros(self.nz1)
        self.lmax = np.zeros(self.nz1)
        self.mmax = np.zeros(self.nz1)
        self.max_vap_perturbation = np.zeros(self.nz1)

        self.Qvap1, self.aer1 = self.read_3d(self.file_name)

    def read_3d(self):
        # Esta funcion lee la salida del la nube en 3-D
        with open(self) as f:
            lines = f.readlines()
            Qvap1 = lines[5]
            aer1 = lines[11]
        return Qvap1, aer1

    def aeroana(self):
        # Calculo de la perturbacion de aerosoles y vapor en la estela
        pool = multiprocessing.Pool()
        pool.map(self.calcular_estadisticas, range(self.nz1))
        pool.close()

    def calcular_estadisticas(self, k):
        for i, j in itertools.product(range(1, self.nx1), range(1, self.nx1)):
            if self.aer1[i, j, k] > self.max_aer_perturbation[k]:
                self.max_aer_perturbation[k] = self.aer1[i, j, k]
                self.imax[k] = i
                self.jmax[k] = j
            if self.Qvap1[i, j, k] > self.max_vap_perturbation[k]:
                self.max_vap_perturbation[k] = self.Qvap1[i, j, k]
                self.lmax[k] = i
                self.mmax[k] = j

        for i in range(self.imax[k] - 2, self.imax[k] + 2):
            for j in range(self.jmax[k] - 2, self.jmax[k] + 2):
                self.aerm[k] += self.aer1[i, j, k]
                self.vapm[k] += self.aer1[i, j, k]

        self.aerm[k] /= 25
        self.vapm[k] /= 25

    def grabar(self):
        # Esta funcion graba los resultados
        with open(f"aerest{self.nombre}.{self.paso}", "w") as f:
            with open(f"vapest{self.nombre}.{self.paso}", "w") as g:
                for k in range(self.nz1):
                    f.write(
                        f"{k} {self.aerm[k]} {self.imax[k]} {self.jmax[k]} {self.max_aer_perturbation[k]} \n"
                    )
                    g.write(
                        f"{k} {self.vapm[k]} {self.lmax[k]} {self.mmax[k]} {self.max_vap_perturbation[k]}\n"
                    )


def pert_aerosol_y_vapor_de_estela():
    # Este programa lee la salida del la nube en 3-D y calcula la perturbacion
    # de aerosoles y vapor en la estela
    dimension = Dimension()
    dimension.aeroana()
    dimension.grabar()


pert_aerosol_y_vapor_de_estela()
