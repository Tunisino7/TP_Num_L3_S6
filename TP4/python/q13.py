# -*- coding: utf-8 -*-
"""
TP4 - Question 13 : Double puits symétrique profond

Refaire Q12 avec a=400 pour étudier l'effet d'une barrière plus haute.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q01_q02 import potentiel_double_puits
from q04_q05 import construire_hamiltonien, diagonaliser_hamiltonien
from q07 import normalize


def main():
    """
    Programme principal - Question 13
    """
    # Paramètres
    L = 20.0
    n = 1000
    a = 400.0  # Barrière haute
    r1 = -2.0
    r2 = -0.5
    r3 = 0.5
    r4 = 2.0
    
    # Discrétisation
    delta_x = L / (n - 1)
    x = np.linspace(-L/2, L/2, n)
    
    print("=== TP4 - Question 13 : Double puits symétrique profond ===")
    print(f"Paramètres : L = {L}, n = {n}")
    print(f"δx = {delta_x:.6f}")
    print(f"Double puits : a = {a}, r1 = {r1}, r2 = {r2}, r3 = {r3}, r4 = {r4}\n")
    
    # Potentiel double puits
    V = potentiel_double_puits(x, a, r1, r2, r3, r4)
    
    # Diagonaliser
    d, e = construire_hamiltonien(x, V, delta_x)
    w, v = diagonaliser_hamiltonien(d, e)
    
    # Normaliser
    psi_norm = normalize(v, delta_x)
    
    # Affichage énergies
    print("Énergies des premiers niveaux :")
    for p in range(min(10, len(w))):
        print(f"  E_{p} = {w[p]:.8f}")
    
    print("\n=== Analyse des doublets ===")
    print("Doublet 1 :")
    print(f"  E_0 = {w[0]:.10f}")
    print(f"  E_1 = {w[1]:.10f}")
    print(f"  ΔE = {w[1] - w[0]:.10e} (levée de dégénérescence)")
    
    print("Doublet 2 :")
    print(f"  E_2 = {w[2]:.10f}")
    print(f"  E_3 = {w[3]:.10f}")
    print(f"  ΔE = {w[3] - w[2]:.10e}")
    
    # Graphique 1 : Potentiel et énergies
    fig, axes = plt.subplots(2, 1, figsize=(12, 10))
    
    # Potentiel avec niveaux d'énergie
    ax1 = axes[0]
    ax1.plot(x, V, 'k-', linewidth=2, label='V(x)', alpha=0.7)
    for p in range(min(10, len(w))):
        if w[p] < 0:  # États liés
            ax1.axhline(y=w[p], color='blue', linestyle='--', linewidth=0.8, alpha=0.5)
            ax1.text(-9, w[p], f'E_{p}', fontsize=9, color='blue')
    ax1.axhline(y=0, color='red', linestyle='-', linewidth=1, alpha=0.5, label='E=0')
    ax1.set_xlabel('Position x', fontsize=12)
    ax1.set_ylabel('Énergie', fontsize=12)
    ax1.set_title(f'Double puits symétrique profond (a={int(a)})', fontsize=13, fontweight='bold')
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-5, 5)
    ax1.set_ylim(-120, 50)
    
    # Fonctions d'onde du premier doublet
    ax2 = axes[1]
    colors = ['blue', 'red']
    for p in range(2):
        psi_p = psi_norm[:, p]
        ax2.plot(x, psi_p, color=colors[p], linewidth=2, 
                 label=f'ψ_{p}(x) (E={w[p]:.6f})', alpha=0.8)
    ax2.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
    ax2.axvline(x=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    ax2.set_xlabel('Position x', fontsize=12)
    ax2.set_ylabel('ψ(x)', fontsize=12)
    ax2.set_title('États fondamentaux : symétrique (ψ_0) et antisymétrique (ψ_1)', 
                  fontsize=13, fontweight='bold')
    ax2.legend(fontsize=11)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(-5, 5)
    
    plt.tight_layout()
    
    # Sauvegarde
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    output_path = os.path.join(output_dir, f'q13_double_puits_sym_a{int(a)}.pdf')
    plt.savefig(output_path, dpi=150)
    print(f"\nFigure sauvegardée : {output_path}")
    
    plt.show()
    
    print("\n=== Commentaire ===")
    print("• Avec a=400, la barrière est beaucoup plus haute qu'avec a=1.")
    print("• L'effet tunnel est fortement supprimé.")
    print("• Les fonctions d'onde sont très localisées dans chaque puits")
    print("  avec peu d'amplitude dans la région centrale.")
    print("• Les doublets sont presque parfaitement dégénérés : ΔE ≈ 0.")
    print("• Limite : deux puits découplés, chacun avec son spectre propre.")
    print("• Les états ne sont plus ψ_gauche ± ψ_droite mais quasi-isolés.")


if __name__ == "__main__":
    main()
