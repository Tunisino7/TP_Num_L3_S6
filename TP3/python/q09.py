# -*- coding: utf-8 -*-
"""
TP3 - Question 9 : Interprétation de la courbe η(T)

Analyse qualitative de la dépendance en température.
"""


def main():
    """
    Programme principal
    """
    print("=== Interprétation de η(T) ===")
    print("• À basse température (T → 0) :")
    print("  les particules s'adsorbent près des atomes (sites préférentiels)")
    print("  → structure ordonnée et fraction de surface plus élevée.")
    print("• À haute température (T ≫ U) :")
    print("  exp(-U/T) ≈ 1, l'adsorption devient quasi uniforme")
    print("  → on retrouve l'état RSA aléatoire, fraction plus faible.")
    print("\nTempérature critique :")
    print("Une transition ordre→désordre peut être définie autour de T_c ≈ U/2.")
    print("\nPrédiction à basse T :")
    print("La fraction tend vers une valeur proche de l'empilement ordonné")
    print("(entre η_carré = π/4 et η_hex = π√3/6), mais reste inférieure")
    print("car le système est bloqué sans réarrangements.")


if __name__ == "__main__":
    main()
