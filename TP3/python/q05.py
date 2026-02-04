# -*- coding: utf-8 -*-
"""
TP3 - Question 5 : Limites en température

Question théorique :
- Pour quelle valeur de T retrouve-t-on le modèle homogène ?
- Comment décrire le modèle pour T = 0 ?
"""


def main():
    """
    Programme principal
    """
    print("=== Limites en température ===")
    print("• Quand T → ∞ : exp(-U/T) → 1")
    print("  → l'adsorption est acceptée partout, on retrouve le modèle homogène (Q1)")
    print("• Quand T = 0 : exp(-U/T) → 0")
    print("  → seules les positions à distance d < r_surf sont acceptées")
    print("  → adsorption uniquement près des atomes (sites préférentiels)")


if __name__ == "__main__":
    main()
