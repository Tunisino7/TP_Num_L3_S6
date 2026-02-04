# -*- coding: utf-8 -*-
"""
TP3 - Question 7 : Configurations pour différentes températures

Visualisation des configurations finales pour T = 0, 1, 2, 5, 10
sur surface structurée.
"""

import numpy as np
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q06 import remplissage_surface_structuree, visualiser_avec_reseau


def main():
    """
    Programme principal
    """
    L = 20.0
    R = 0.4
    MAX_TRIES = 10000
    r_surf = 0.05
    U = 10.0

    np.random.seed(42)

    print("=== Configurations pour différentes températures ===\n")
    T_values = [0, 1, 2, 5, 10]

    for T in T_values:
        print(f"Simulation pour T = {T}")
        x, y, n = remplissage_surface_structuree(L, R, MAX_TRIES, r_surf, U, T)
        fraction = n * np.pi * R**2 / L**2
        print(f"  n = {n}, fraction = {fraction:.4f}\n")

        filename = f"q07_T{T}.pdf"
        visualiser_avec_reseau(x, y, R, L, T, filename)


if __name__ == "__main__":
    main()
