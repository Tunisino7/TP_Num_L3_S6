# -*- coding: utf-8 -*-
"""
TP4 - Question 6 : Comparaison des énergies propres avec la théorie (puits infini)

Tracer les énergies numériques et théoriques pour le puits carré infini.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q01_q02 import potentiel_puits
from q04_q05 import construire_hamiltonien, diagonaliser_hamiltonien


def energie_theorique_puits(p, L):
    """
    Énergie théorique pour le puits carré infini.
    
    E_p = (ℏ²π²(p+1)²) / (2mL²)
    
    Avec ℏ²/(2m) = 1, on a :
    E_p = π²(p+1)² / L²
    
    Paramètres :
        p : numéro du niveau (p = 0, 1, 2, ...)
        L : largeur du puits
    
    Retour :
        E_p
    """
    return (np.pi * (p + 1) / L)**2


def main():
    """
    Programme principal - Question 6
    """
    # Paramètres
    L = 5.0
    n = 100
    
    # Discrétisation
    delta_x = L / (n - 1)
    x = np.linspace(-L/2, L/2, n)
    
    print("=== TP4 - Question 6 : Puits carré infini ===")
    print(f"Paramètres : L = {L}, n = {n}\n")
    
    # Potentiel
    V = potentiel_puits(x)
    
    # Construire et diagonaliser H
    d, e = construire_hamiltonien(x, V, delta_x)
    w, v = diagonaliser_hamiltonien(d, e)
    
    # Énergies théoriques
    p_values = np.arange(len(w))
    E_theo = energie_theorique_puits(p_values, L)
    
    # Comparaison pour les premiers niveaux
    print("Comparaison énergies numériques vs théoriques :")
    print(f"{'p':<5} {'E_num':<15} {'E_theo':<15} {'Écart relatif':<15}")
    print("-" * 55)
    for p in range(min(10, len(w))):
        ecart_rel = abs(w[p] - E_theo[p]) / E_theo[p] * 100
        print(f"{p:<5} {w[p]:<15.6f} {E_theo[p]:<15.6f} {ecart_rel:<15.4f}%")
    
    # Graphique
    plt.figure(figsize=(12, 7))
    
    plt.plot(p_values, w, 'bo-', linewidth=2, markersize=6, label='Numérique', alpha=0.7)
    plt.plot(p_values, E_theo, 'r--', linewidth=2, label='Théorique', alpha=0.8)
    
    plt.xlabel('Niveau p', fontsize=13)
    plt.ylabel('Énergie E_p', fontsize=13)
    plt.title(f'Énergies propres du puits carré infini (L={L}, n={n})', 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Sauvegarde
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f'q06_puits_energies_n{n}_L{int(L)}.pdf')
    plt.savefig(output_path, dpi=150)
    print(f"\nFigure sauvegardée : {output_path}")
    
    plt.show()
    
    print("\n=== Discussion ===")
    print("• L'accord est excellent pour les bas niveaux d'énergie.")
    print("• Pour les niveaux élevés, l'écart augmente car la fonction d'onde")
    print("  oscille rapidement et n'est plus bien échantillonnée avec δx fixe.")
    print("• Pour améliorer : augmenter n (diminuer δx).")


if __name__ == "__main__":
    main()
