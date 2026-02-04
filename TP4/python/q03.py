# -*- coding: utf-8 -*-
"""
TP4 - Question 3 : Interprétation physique des conditions aux limites

Question : Quel sens physique cela a-t-il de poser ψ(-1) = ψ(n) = 0 ?
Quelle est la conséquence pour le potentiel effectif ?
"""


def main():
    """
    Programme principal - Question 3
    """
    print("=== TP4 - Question 3 : Conditions aux limites ===\n")
    
    print("Question : Quel sens physique a la condition ψ(-1) = ψ(n) = 0 ?")
    print("Quelle conséquence pour le potentiel effectif ?\n")
    
    print("Réponse :")
    print("─" * 70)
    print("• Poser ψ(-1) = ψ(n) = 0 signifie que la fonction d'onde s'annule")
    print("  aux extrémités de l'intervalle [-L/2, L/2].")
    print()
    print("• Sens physique :")
    print("  - La particule ne peut pas exister hors de cet intervalle")
    print("  - On simule un potentiel infini aux bords : V(±L/2) = +∞")
    print("  - C'est comme si la particule était confinée dans une \"boîte\"")
    print()
    print("• Conséquence pour le potentiel effectif :")
    print("  - Quel que soit le potentiel V(x) défini dans [-L/2, L/2],")
    print("    on ajoute implicitement des \"murs infinis\" aux extrémités")
    print("  - Le potentiel effectif devient :")
    print("    V_eff(x) = V(x)       si x ∈ [-L/2, L/2]")
    print("    V_eff(x) = +∞         sinon")
    print()
    print("• Condition de validité :")
    print("  - Il faut que L soit suffisamment grand pour que la fonction")
    print("    d'onde soit négligeable aux bords : ψ(±L/2) ≈ 0")
    print("  - Si ce n'est pas le cas, les résultats sont faussés car la")
    print("    particule \"sent\" les murs artificiels")
    print("─" * 70)


if __name__ == "__main__":
    main()
