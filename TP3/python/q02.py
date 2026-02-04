# -*- coding: utf-8 -*-
"""
TP3 - Question 2 : Visualisation de la configuration finale

On affiche la configuration obtenue pour la surface homogène et on vérifie
qu'il n'y a pas de chevauchement ni de particules qui dépassent les bords.
"""

import numpy as np
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q01 import remplissage, visualiser_adsorption


def main():
    """
    Programme principal
    """
    # Paramètres
    L = 20.0
    R = 0.4
    MAX_TRIES = 1000

    np.random.seed(42)

    print("=== Visualisation de l'adsorption RSA (Q2) ===")
    print(f"Paramètres : L = {L}, R = {R}, MAX_TRIES = {MAX_TRIES}")

    # Simulation
    x, y, n = remplissage(L, R, MAX_TRIES)

    # Fraction de surface occupée
    fraction_surface = n * np.pi * R**2 / L**2
    print(f"Nombre de particules : {n}")
    print(f"Fraction de surface : {fraction_surface:.4f}")

    # Visualisation
    visualiser_adsorption(x, y, R, L, filename="q02.pdf")


if __name__ == "__main__":
    main()
