# -*- coding: utf-8 -*-
"""
TP3 - Question 4 : Comparaison avec un empilement ordonné

Calcul des fractions de surface occupée pour un empilement carré
et hexagonal, puis comparaison qualitative avec l'empilement aléatoire.
"""

import numpy as np


def main():
    """
    Programme principal
    """
    eta_carre = np.pi / 4
    eta_hex = np.pi * np.sqrt(3) / 6

    print("=== Empilement ordonné ===")
    print(f"Empilement carré : η = π/4 = {eta_carre:.3f}")
    print(f"Empilement hexagonal : η = π√3/6 = {eta_hex:.3f}")

    print("\n=== Comparaison qualitative ===")
    print("L'adsorption aléatoire (RSA) donne une fraction plus faible,")
    print("car l'empilement n'est pas optimisé et le système est bloqué")
    print("dans un état de jamming avant d'atteindre la compacité idéale.")


if __name__ == "__main__":
    main()
