# -*- coding: utf-8 -*-
"""
TP4 - Question 7 : Normalisation et visualisation des fonctions d'onde (puits infini)

Normaliser les fonctions d'onde et tracer |ψ|² décalées verticalement par E_p.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q01_q02 import potentiel_puits
from q04_q05 import construire_hamiltonien, diagonaliser_hamiltonien


def normalize(v, delta_x):
    """
    Normalise les vecteurs propres (fonctions d'onde).
    
    Les colonnes de v sont déjà normalisées par eigh_tridiagonal,
    mais on applique le facteur 1/√(δx) pour respecter la normalisation continue.
    
    Paramètres :
        v : matrice des vecteurs propres (n × n)
        delta_x : pas de discrétisation
    
    Retour :
        v_norm : vecteurs propres normalisés
    """
    v_norm = v / np.linalg.norm(v, axis=0)  # Normaliser les colonnes
    v_norm /= np.sqrt(delta_x)              # Facteur 1/√(δx)
    return v_norm


def main():
    """
    Programme principal - Question 7
    """
    # Paramètres
    L = 5.0
    n = 100
    
    # Discrétisation
    delta_x = L / (n - 1)
    x = np.linspace(-L/2, L/2, n)
    
    print("=== TP4 - Question 7 : Fonctions d'onde du puits infini ===")
    print(f"Paramètres : L = {L}, n = {n}\n")
    
    # Potentiel
    V = potentiel_puits(x)
    
    # Diagonaliser
    d, e = construire_hamiltonien(x, V, delta_x)
    w, v = diagonaliser_hamiltonien(d, e)
    
    # Normaliser
    v_norm = normalize(v, delta_x)
    
    print("Normalisation vérifiée :")
    for p in range(3):
        integrale = np.sum(v_norm[:, p]**2) * delta_x
        print(f"  ∫|ψ_{p}|² dx = {integrale:.6f}")
    
    # Tracer les fonctions d'onde au carré, décalées par E_p
    plt.figure(figsize=(12, 8))
    
    # Tracer le potentiel (V = 0)
    plt.axhline(y=0, color='k', linestyle='--', linewidth=1, alpha=0.5, label='V(x) = 0')
    
    # Tracer les 3 premières fonctions d'onde
    p_max = 3
    for p in range(p_max):
        psi_squared = v_norm[:, p]**2
        # Décaler verticalement par E_p
        plt.plot(x, w[p] + psi_squared * 2, linewidth=2, label=f'p={p}, E_{p}={w[p]:.3f}')
        # Ligne horizontale pour E_p
        plt.axhline(y=w[p], color='gray', linestyle=':', linewidth=0.8, alpha=0.5)
    
    plt.xlabel('x', fontsize=13)
    plt.ylabel('Énergie / |ψ(x)|²', fontsize=13)
    plt.title('Fonctions d\'onde au carré du puits carré infini', 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11, loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.xlim(-L/2, L/2)
    plt.tight_layout()
    
    # Sauvegarde
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    output_path = os.path.join(output_dir, f'q07_puits_fonctions_n{n}_L{int(L)}.pdf')
    plt.savefig(output_path, dpi=150)
    print(f"\nFigure sauvegardée : {output_path}")
    
    plt.show()
    
    print("\n=== Discussion ===")
    print("• p=0 : fonction d'onde fondamentale, une seule bosse (pas de nœud)")
    print("• p=1 : premier état excité, deux bosses (un nœud au centre)")
    print("• p=2 : deuxième état excité, trois bosses (deux nœuds)")
    print("• Chaque état a (p+1) bosses et p nœuds, comme attendu.")
    print("• La fonction d'onde s'annule bien aux extrémités de l'intervalle.")


if __name__ == "__main__":
    main()
