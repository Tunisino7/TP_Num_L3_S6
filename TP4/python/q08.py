# -*- coding: utf-8 -*-
"""
TP4 - Question 8 : Comparaison fonctions d'onde numériques vs théoriques

Comparer ψ_num avec ψ_theo pour p=1 et p=55.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q01_q02 import potentiel_puits
from q04_q05 import construire_hamiltonien, diagonaliser_hamiltonien
from q07 import normalize


def fonction_onde_theorique_puits(x, p, L):
    """
    Fonction d'onde théorique pour le puits carré infini.
    
    ψ_p(x) = √(2/L) sin(π(p+1)(x + L/2) / L)
    
    Paramètres :
        x : positions
        p : numéro du niveau
        L : largeur du puits
    
    Retour :
        ψ_p(x)
    """
    return np.sqrt(2 / L) * np.sin(np.pi * (p + 1) * (x + L/2) / L)


def main():
    """
    Programme principal - Question 8
    """
    # Paramètres
    L = 5.0
    n = 100
    
    # Discrétisation
    delta_x = L / (n - 1)
    x = np.linspace(-L/2, L/2, n)
    
    print("=== TP4 - Question 8 : Comparaison ψ_num vs ψ_theo ===")
    print(f"Paramètres : L = {L}, n = {n}\n")
    
    # Potentiel et diagonalisation
    V = potentiel_puits(x)
    d, e = construire_hamiltonien(x, V, delta_x)
    w, v = diagonaliser_hamiltonien(d, e)
    v_norm = normalize(v, delta_x)
    
    # Niveaux à comparer
    p_values = [1, 55]
    
    for p in p_values:
        print(f"\n=== Niveau p = {p} ===")
        
        # Fonctions d'onde
        psi_num = v_norm[:, p]
        psi_theo = fonction_onde_theorique_puits(x, p, L)
        
        # Vérifier que le signe est cohérent (phase arbitraire)
        if np.dot(psi_num, psi_theo) < 0:
            psi_num = -psi_num
        
        # Erreur relative
        erreur = np.abs(psi_num - psi_theo)
        erreur_max = np.max(erreur)
        erreur_moy = np.mean(erreur)
        
        print(f"Erreur max : {erreur_max:.6f}")
        print(f"Erreur moyenne : {erreur_moy:.6f}")
        
        # Graphique
        fig, axes = plt.subplots(2, 1, figsize=(12, 10))
        
        # Graphe 1 : ψ(x)
        axes[0].plot(x, psi_num, 'b-', linewidth=2, label='Numérique', alpha=0.7)
        axes[0].plot(x, psi_theo, 'r--', linewidth=2, label='Théorique', alpha=0.8)
        axes[0].set_xlabel('x', fontsize=12)
        axes[0].set_ylabel('ψ(x)', fontsize=12)
        axes[0].set_title(f'Fonction d\'onde pour p={p} (E={w[p]:.3f})', 
                         fontsize=13, fontweight='bold')
        axes[0].legend(fontsize=11)
        axes[0].grid(True, alpha=0.3)
        axes[0].set_xlim(-L/2, L/2)
        
        # Graphe 2 : erreur |ψ_num - ψ_theo|
        axes[1].plot(x, erreur, 'g-', linewidth=2)
        axes[1].set_xlabel('x', fontsize=12)
        axes[1].set_ylabel('|ψ_num - ψ_theo|', fontsize=12)
        axes[1].set_title(f'Erreur absolue (max={erreur_max:.6f})', 
                         fontsize=13, fontweight='bold')
        axes[1].grid(True, alpha=0.3)
        axes[1].set_xlim(-L/2, L/2)
        
        plt.tight_layout()
        
        # Sauvegarde
        output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
        output_path = os.path.join(output_dir, f'q08_puits_comparaison_p{p}_n{n}_L{int(L)}.pdf')
        plt.savefig(output_path, dpi=150)
        print(f"Figure sauvegardée : {output_path}")
        
        plt.show()
    
    print("\n=== Diagnostic ===")
    print("• Pour p=1 : accord excellent, erreur négligeable")
    print("  → la fonction d'onde varie lentement, bien échantillonnée par δx")
    print("• Pour p=55 : erreur importante, oscillations mal capturées")
    print("  → la fonction d'onde oscille rapidement, δx trop grand")
    print("  → on atteint la limite de résolution : λ ≈ L/(p+1) ≈ δx")
    print("• Solution : augmenter n pour diminuer δx")


if __name__ == "__main__":
    main()
