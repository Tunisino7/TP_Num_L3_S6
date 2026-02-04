# -*- coding: utf-8 -*-
"""
TP3 - Question 3 : Analyse statistique de l'adsorption

On répète l'expérience M=20 fois pour calculer la moyenne et l'écart-type
du nombre de particules adsorbées et de la fraction de surface occupée.
"""

import numpy as np
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q01 import remplissage


def analyse_statistique(L, R, MAX_TRIES, M):
    """
    Effectue M simulations et calcule les statistiques.

    Paramètres :
        L : côté du carré
        R : rayon des particules
        MAX_TRIES : nombre d'échecs consécutifs maximum
        M : nombre d'expériences

    Retour :
        moyennes et écarts-types
    """
    n_list = np.zeros(M)
    frac_list = np.zeros(M)

    print(f"Simulation de {M} expériences...")

    for i in range(M):
        if (i + 1) % 5 == 0:
            print(f"  Expérience {i+1}/{M}")

        _, _, n = remplissage(L, R, MAX_TRIES)
        n_list[i] = n
        frac_list[i] = n * np.pi * R**2 / L**2

    n_moy = np.mean(n_list)
    n_std = np.std(n_list)

    frac_moy = np.mean(frac_list)
    frac_std = np.std(frac_list)

    return n_moy, n_std, frac_moy, frac_std


def main():
    """
    Programme principal
    """
    L = 20.0
    R = 0.4
    MAX_TRIES = 1000
    M = 20

    np.random.seed(42)

    print("=== Analyse statistique de l'adsorption ===")
    print("Paramètres :")
    print(f"  L = {L}, R = {R}")
    print(f"  MAX_TRIES = {MAX_TRIES}")
    print(f"  Nombre d'expériences M = {M}\n")

    n_moy, n_std, frac_moy, frac_std = analyse_statistique(L, R, MAX_TRIES, M)

    print("\n=== Résultats statistiques ===")
    print("Nombre de particules adsorbées :")
    print(f"  <n> = {n_moy:.1f} ± {n_std:.1f}")
    print("\nFraction de surface occupée :")
    print(f"  η = {frac_moy:.3f} ± {frac_std:.3f}")
    print(f"  η = {frac_moy:.2%} ± {frac_std:.2%}")


if __name__ == "__main__":
    main()
