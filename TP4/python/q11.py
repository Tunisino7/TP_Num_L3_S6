# -*- coding: utf-8 -*-
"""
TP4 - Question 11 : Visualisation fonctions d'onde oscillateur harmonique

Tracer le potentiel V(x) et les densités de probabilité |ψ_p(x)|² décalées de E_p
pour p = 0, 1, 2 avec L=20, n=100.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q01_q02 import potentiel_harmonique
from q04_q05 import construire_hamiltonien, diagonaliser_hamiltonien
from q07 import normalize


def main():
    """
    Programme principal - Question 11
    """
    # Paramètres
    L = 20.0
    n = 100
    
    # Discrétisation
    delta_x = L / (n - 1)
    x = np.linspace(-L/2, L/2, n)
    
    print("=== TP4 - Question 11 : Fonctions d'onde oscillateur harmonique ===")
    print(f"Paramètres : L = {L}, n = {n}")
    print(f"δx = {delta_x:.6f}\n")
    
    # Potentiel harmonique
    V = potentiel_harmonique(x)
    
    # Diagonaliser
    d, e = construire_hamiltonien(x, V, delta_x)
    w, v = diagonaliser_hamiltonien(d, e)
    
    # Normaliser
    psi_norm = normalize(v, delta_x)
    
    # Affichage énergies
    print("Énergies des premiers niveaux :")
    for p in range(min(5, len(w))):
        print(f"  E_{p} = {w[p]:.6f}")
    
    # Graphique
    plt.figure(figsize=(12, 8))
    
    # Potentiel
    plt.plot(x, V, 'k-', linewidth=2, label='V(x) = (1/2)x²', alpha=0.7)
    
    # Fonctions d'onde p = 0, 1, 2
    colors = ['blue', 'green', 'red']
    for p in range(3):
        psi_p = psi_norm[:, p]
        rho_p = np.abs(psi_p)**2  # Densité de probabilité
        
        # Décalage par E_p
        plt.plot(x, w[p] + rho_p * 5, color=colors[p], linewidth=2, 
                 label=f'|ψ_{p}(x)|² + E_{p} (E={w[p]:.3f})', alpha=0.8)
        
        # Ligne horizontale à E_p
        plt.axhline(y=w[p], color=colors[p], linestyle='--', linewidth=1, alpha=0.4)
    
    plt.xlabel('Position x', fontsize=13)
    plt.ylabel('Énergie / Densité de probabilité', fontsize=13)
    plt.title(f'Oscillateur harmonique : V(x) et |ψ_p(x)|² (L={int(L)}, n={n})', 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11, loc='best')
    plt.grid(True, alpha=0.3)
    plt.xlim(-6, 6)  # Focus sur région intéressante
    plt.ylim(0, max(w[2] + 5*np.max(np.abs(psi_norm[:, 2])**2), np.max(V[abs(x) < 6])))
    plt.tight_layout()
    
    # Sauvegarde
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    output_path = os.path.join(output_dir, f'q11_harmonique_fonctions_n{n}_L{int(L)}.pdf')
    plt.savefig(output_path, dpi=150)
    print(f"\nFigure sauvegardée : {output_path}")
    
    plt.show()
    
    print("\n=== Commentaire ===")
    print("• p=0 : État fondamental, densité maximale au centre (ψ gaussienne)")
    print("• p=1 : Un nœud au centre, densité nulle en x=0")
    print("• p=2 : Deux nœuds, densité maximale en trois lobes")
    print("• Les fonctions d'onde s'étendent plus loin quand E augmente")
    print("• Comportement classique : aux points de retour V(x) = E_p,")
    print("  la densité quantique est maximale (vitesse classique nulle)")


if __name__ == "__main__":
    main()
