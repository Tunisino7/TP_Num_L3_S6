# -*- coding: utf-8 -*-
"""
TP4 - Question 10 : Potentiel harmonique avec L=20

Refaire Q9 avec L=20 pour étudier l'influence de la discrétisation spatiale.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q01_q02 import potentiel_harmonique
from q04_q05 import construire_hamiltonien, diagonaliser_hamiltonien
from q09 import energie_theorique_harmonique


def main():
    """
    Programme principal - Question 10
    """
    # Paramètres
    L = 20.0
    n = 100
    
    # Discrétisation
    delta_x = L / (n - 1)
    x = np.linspace(-L/2, L/2, n)
    
    print("=== TP4 - Question 10 : Oscillateur harmonique avec L étendu ===")
    print(f"Paramètres : L = {L}, n = {n}")
    print(f"δx = {delta_x:.6f}")
    print(f"Potentiel : V(x) = (1/2)x²\n")
    
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
             label='Numérique (L=20)', alpha=0.7)
    plt.plot(p_values, E_theo, 'r--', linewidth=2, label='Théorique', alpha=0.8)
    
    plt.xlabel('Niveau p', fontsize=13)
    plt.ylabel('Énergie E_p', fontsize=13)
    plt.title(f'Énergies propres de l\'oscillateur harmonique (L={int(L)}, n={n})', 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Sauvegarde
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    output_path = os.path.join(output_dir, f'q10_harmonique_energies_n{n}_L{int(L)}.pdf')
    plt.savefig(output_path, dpi=150)
    print(f"\nFigure sauvegardée : {output_path}")
    
    plt.show()
    
    print("\n=== Commentaire ===")
    print("• Avec L=20, l'accord est bien meilleur qu'avec L=5 (Q9).")
    print("• Les conditions aux limites artificielles (ψ(±L/2)=0) perturbent moins")
    print("  car la fonction d'onde décroît exponentiellement loin du centre.")
    print(f"• Inconvénient : δx = {delta_x:.4f} est plus grand (n fixé)")
    print("  donc la discrétisation spatiale est plus grossière.")
    print("• Compromis : il faut augmenter n pour améliorer δx tout en gardant L grand.")


if __name__ == "__main__":
    main()
