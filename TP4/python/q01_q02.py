# -*- coding: utf-8 -*-
"""
TP4 - Questions 1 et 2 : Définition des potentiels et discrétisation

Question 1 : Écrire trois fonctions pour les potentiels (puits infini, harmonique, double puits)
Question 2 : Définir l'intervalle [-L/2, L/2], le discrétiser et tracer les trois potentiels
"""

import numpy as np
import matplotlib.pyplot as plt
import os


def potentiel_puits(x):
    """
    Potentiel du puits carré infini : V(x) = 0 partout
    
    Paramètres :
        x : position (scalaire ou tableau numpy)
    
    Retour :
        V(x) = 0
    """
    return np.zeros_like(x)


def potentiel_harmonique(x):
    """
    Potentiel harmonique : V(x) = (1/2) m ω² x²
    
    On prend ω = 1/m et ℏ²/(2m) = 1, donc :
    V(x) = (1/2) k x² avec k = 1
    
    Paramètres :
        x : position
    
    Retour :
        V(x) = (1/2) x²
    """
    return 0.5 * x**2


def potentiel_double_puits(x, a=1.0, r1=-2.0, r2=-0.5, r3=0.5, r4=2.0):
    """
    Double puits : V(x) = a(x - r1)(x - r2)(x - r3)(x - r4)
    
    Polynôme de degré 4 dont les racines sont r1, r2, r3, r4.
    
    Paramètres :
        x : position
        a : facteur multiplicatif
        r1, r2, r3, r4 : racines du polynôme
    
    Retour :
        V(x)
    """
    return a * (x - r1) * (x - r2) * (x - r3) * (x - r4)


def main():
    """
    Programme principal - Questions 1 et 2
    """
    # Paramètres
    L = 5.0
    n = 100
    
    # Discrétisation de l'intervalle [-L/2, L/2]
    delta_x = L / (n - 1)
    x = np.linspace(-L/2, L/2, n)
    
    print("=== TP4 - Questions 1 et 2 ===")
    print(f"Paramètres :")
    print(f"  L = {L}")
    print(f"  n = {n}")
    print(f"  δx = {delta_x:.4f}")
    print(f"  Intervalle : [{x[0]:.2f}, {x[-1]:.2f}]")
    
    # Calcul des trois potentiels
    V_puits = potentiel_puits(x)
    V_harmonique = potentiel_harmonique(x)
    V_double_puits = potentiel_double_puits(x, a=1.0, r1=-2.0, r2=-0.5, r3=0.5, r4=2.0)
    
    # Tracer les trois potentiels
    plt.figure(figsize=(14, 5))
    
    # Puits infini
    plt.subplot(1, 3, 1)
    plt.plot(x, V_puits, 'b-', linewidth=2)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('V(x)', fontsize=12)
    plt.title('Puits carré infini', fontsize=13, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.xlim(-L/2, L/2)
    
    # Potentiel harmonique
    plt.subplot(1, 3, 2)
    plt.plot(x, V_harmonique, 'r-', linewidth=2)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('V(x)', fontsize=12)
    plt.title('Potentiel harmonique', fontsize=13, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.xlim(-L/2, L/2)
    
    # Double puits
    plt.subplot(1, 3, 3)
    plt.plot(x, V_double_puits, 'g-', linewidth=2)
    plt.axhline(y=0, color='k', linestyle='--', linewidth=0.8, alpha=0.5)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('V(x)', fontsize=12)
    plt.title('Double puits', fontsize=13, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.xlim(-L/2, L/2)
    
    plt.tight_layout()
    
    # Sauvegarde
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'q01_q02.pdf')
    plt.savefig(output_path, dpi=150)
    print(f"\nFigure sauvegardée : {output_path}")
    
    plt.show()
    
    print("\n=== Interprétation ===")
    print("• Puits infini : V(x) = 0 partout (particule libre dans la boîte)")
    print("• Potentiel harmonique : V(x) = (1/2)x² (oscillateur quantique)")
    print("• Double puits : polynôme de degré 4 avec deux minimums symétriques")


if __name__ == "__main__":
    main()
