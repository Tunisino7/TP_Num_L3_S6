# -*- coding: utf-8 -*-
"""
TP4 - Question 9 : Potentiel harmonique - Comparaison énergies avec théorie

Étudier le potentiel harmonique avec L=5, n=100 et comparer avec la théorie.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q01_q02 import potentiel_harmonique
from q04_q05 import construire_hamiltonien, diagonaliser_hamiltonien


def energie_theorique_harmonique(p):
    """
    Énergie théorique pour l'oscillateur harmonique.
    
    E_p = (p + 1/2) ℏω
    
    Avec k=1, m=1, ω=√(k/m)=1, ℏ²/(2m)=1, on a ℏω = √2.
    
    Donc : E_p = (p + 1/2) √2
    
    Paramètres :
        p : numéro du niveau (p = 0, 1, 2, ...)
    
    Retour :
        E_p
    """
    return (p + 0.5) * np.sqrt(2)


def main():
    """
    Programme principal - Question 9
    """
    # Paramètres
    L = 5.0
    n = 100
    
    # Discrétisation
    delta_x = L / (n - 1)
    x = np.linspace(-L/2, L/2, n)
    
    print("=== TP4 - Question 9 : Oscillateur harmonique ===")
    print(f"Paramètres : L = {L}, n = {n}")
    print(f"Potentiel : V(x) = (1/2)x²")
    print(f"ℏω = √2 ≈ {np.sqrt(2):.6f}\n")
    
    # Potentiel harmonique
    V = potentiel_harmonique(x)
    
    # Diagonaliser
    d, e = construire_hamiltonien(x, V, delta_x)
    w, v = diagonaliser_hamiltonien(d, e)
    
    # Énergies théoriques
    p_values = np.arange(min(50, len(w)))
    E_theo = energie_theorique_harmonique(p_values)
    
    # Comparaison
    print("Comparaison énergies numériques vs théoriques :")
    print(f"{'p':<5} {'E_num':<15} {'E_theo':<15} {'Écart relatif':<15}")
    print("-" * 55)
    for p in range(min(10, len(p_values))):
        ecart_rel = abs(w[p] - E_theo[p]) / E_theo[p] * 100
        print(f"{p:<5} {w[p]:<15.6f} {E_theo[p]:<15.6f} {ecart_rel:<15.6f}%")
    
    # Graphique
    plt.figure(figsize=(12, 7))
    
    plt.plot(p_values, w[:len(p_values)], 'bo-', linewidth=2, markersize=6, 
             label='Numérique', alpha=0.7)
    plt.plot(p_values, E_theo, 'r--', linewidth=2, label='Théorique', alpha=0.8)
    
    plt.xlabel('Niveau p', fontsize=13)
    plt.ylabel('Énergie E_p', fontsize=13)
    plt.title(f'Énergies propres de l\'oscillateur harmonique (L={L}, n={n})', 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Sauvegarde
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    output_path = os.path.join(output_dir, f'q09_harmonique_energies_n{n}_L{int(L)}.pdf')
    plt.savefig(output_path, dpi=150)
    print(f"\nFigure sauvegardée : {output_path}")
    
    plt.show()
    
    print("\n=== Commentaire ===")
    print("• L'accord est bon pour les bas niveaux d'énergie.")
    print("• Pour les niveaux élevés, l'écart augmente significativement.")
    print("• Raison : la fonction d'onde s'étend loin du centre pour E élevée")
    print("  et est tronquée par les conditions aux limites ψ(±L/2) = 0.")
    print("• L=5 est trop petit : la particule \"sent\" les murs artificiels.")


if __name__ == "__main__":
    main()
