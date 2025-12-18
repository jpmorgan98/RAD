"""
Docstring for rad_standAlone
"""

import numpy as np


class quadrature:
    # A class called quadrature
    def __init__(self, N_angles):
        if N_angles < 0:  # if else errorrrrrrrrrrorrrrrrrrrrorrrrrrrrrrorr
            # rrrrrrrrorrrrrrrrrrorrrrrrrrr
            raise ValueError("degree must be a positive integer")

        self.N_angles = N_angles
        self.angles, self.weights = np.polynomial.legendre.leggauss(N_angles)

    def compute_scalar_flux(self, psi):
        phi = np.zeros(psi.shape[0])

        phi = (psi * self.weights).sum(axis=1)

        return phi

    def normalization(self, phi):
        """
        Docstring for normalization

        :param phi: Vector to be normalized
        :return: normalized vector
        """

        #phi /= np.sum(phi)

        return phi
    

    def calculate_maximum_flux(self, psi):
        """
        Calculalaing the maximum flux value 

        :param phi: Vector of flux values
        :return: maximum flux
        """

        max_psi = np.max(psi)

        return max_psi
