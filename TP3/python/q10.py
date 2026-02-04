# -*- coding: utf-8 -*-
"""
TP3 - Question 10 : Étude de convergence avec MAX_TRIES

Analyse de l'influence du nombre maximum de tentatives MAX_TRIES
sur la fraction de surface occupée.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q01 import remplissage


def etude_convergence(L, R, MAX_TRIES_values, M):
    """
    Étudie l'évolution de la fraction avec MAX_TRIES.
    """
    fractions_moy = []
    fractions_std = []

    for MAX_TRIES in MAX_TRIES_values:
        print(f"MAX_TRIES = {MAX_TRIES} ...")

        fractions = []
        for _ in range(M):
            _, _, n = remplissage(L, R, MAX_TRIES)
            fraction = n * np.pi * R**2 / L**2
            fractions.append(fraction)

        fractions_moy.append(np.mean(fractions))
        fractions_std.append(np.std(fractions))

    return MAX_TRIES_values, fractions_moy, fractions_std


def main():
    """
    Programme principal
    """
    L = 20.0
    R = 0.4
    M = 20

    MAX_TRIES_values = [1000, 2000, 4000, 8000, 16000, 32000]

    np.random.seed(42)

    print("=== Étude de convergence avec MAX_TRIES ===\n")
    print(f"Paramètres : L = {L}, R = {R}, M = {M}\n")

    MT_vals, frac_moy, frac_std = etude_convergence(L, R, MAX_TRIES_values, M)

    print("\n=== Résultats ===")
    print(f"{'MAX_TRIES':<12} {'Fraction moy.':<15} {'Écart-type':<12}")
    print("-" * 40)
    for mt, f, s in zip(MT_vals, frac_moy, frac_std):
        print(f"{mt:<12} {f:<15.4f} {s:<12.4f}")

    plt.figure(figsize=(12, 7))

    plt.errorbar(MT_vals, frac_moy, yerr=frac_std, fmt='o-',
                capsize=5, capthick=2, markersize=8, linewidth=2,
                label=f'Simulation (M={M})')

    plt.xscale('log')
    plt.xlabel('MAX_TRIES', fontsize=13)
    plt.ylabel('Fraction de surface occupée η', fontsize=13)
    plt.title("Convergence de l'adsorption en fonction de MAX_TRIES",
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, which='both')
    plt.tight_layout()

    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'q10.pdf')
    plt.savefig(output_path, dpi=150)
    print(f"\nFigure sauvegardée : {output_path}")

    plt.show()

    print("\n=== Analyse ===")
    print(f"Pour MAX_TRIES = 1000  : η ≈ {frac_moy[0]:.4f}")
    print(f"Pour MAX_TRIES = 32000 : η ≈ {frac_moy[-1]:.4f}")

    if len(frac_moy) >= 3:
        variation = abs(frac_moy[-1] - frac_moy[-2]) / frac_moy[-1] * 100
        print(f"\nVariation entre 16000 et 32000 : {variation:.2f}%")

        if variation < 1.0:
            print("→ Convergence atteinte (variation < 1%)")
        else:
            print("→ Pas encore totalement convergé")


if __name__ == "__main__":
    main()
