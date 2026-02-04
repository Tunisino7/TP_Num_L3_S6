# -*- coding: utf-8 -*-
"""
TP4 - Questions 4 et 5 : Diagonalisation de la matrice Hamiltonienne

Question 4 : Créer les tableaux d et e pour la matrice tridiagonale H
Question 5 : Utiliser eigh_tridiagonal pour trouver valeurs et vecteurs propres
"""

import numpy as np
from scipy.linalg import eigh_tridiagonal
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q01_q02 import potentiel_puits


def construire_hamiltonien(x, V, delta_x):
    """
    Construit les diagonales d et e de la matrice Hamiltonienne tridiagonale.
    
    La matrice H a la forme :
        H_ii = 2/δx² + V_i (diagonale principale)
        H_i(i±1) = -1/δx² (diagonales adjacentes)
    
    Paramètres :
        x : tableau des positions
        V : tableau des valeurs du potentiel
        delta_x : pas de discrétisation
    
    Retour :
        d : diagonale principale (taille n)
        e : diagonale supérieure (taille n-1)
    """
    n = len(x)
    
    # Diagonale principale : 2/δx² + V_i
    d = 2.0 / delta_x**2 + V
    
    # Diagonales adjacentes : -1/δx²
    e = -np.ones(n - 1) / delta_x**2
    
    return d, e


def diagonaliser_hamiltonien(d, e):
    """
    Diagonalise la matrice Hamiltonienne tridiagonale.
    
    Paramètres :
        d : diagonale principale
        e : diagonale supérieure
    
    Retour :
        w : valeurs propres (énergies), ordre croissant
        v : vecteurs propres (fonctions d'onde), en colonnes
    """
    w, v = eigh_tridiagonal(d, e)
    return w, v


def main():
    """
    Programme principal - Questions 4 et 5
    """
    # Paramètres
    L = 5.0
    n = 100
    
    # Discrétisation
    delta_x = L / (n - 1)
    x = np.linspace(-L/2, L/2, n)
    
    print("=== TP4 - Questions 4 et 5 ===")
    print(f"Paramètres :")
    print(f"  L = {L}")
    print(f"  n = {n}")
    print(f"  δx = {delta_x:.4f}")
    
    # Potentiel du puits infini (V = 0 partout)
    V = potentiel_puits(x)
    
    print(f"\n=== Question 4 : Construction de la matrice H ===")
    
    # Construire les diagonales de H
    d, e = construire_hamiltonien(x, V, delta_x)
    
    print(f"Taille de la diagonale principale d : {len(d)}")
    print(f"Taille de la diagonale supérieure e : {len(e)}")
    print(f"Premiers éléments de d : {d[:5]}")
    print(f"Premiers éléments de e : {e[:5]}")
    
    print(f"\n=== Question 5 : Diagonalisation ===")
    
    # Diagonaliser
    w, v = diagonaliser_hamiltonien(d, e)
    
    print(f"Nombre de valeurs propres trouvées : {len(w)}")
    print(f"Forme de la matrice des vecteurs propres : {v.shape}")
    print(f"\nPremières énergies propres (10 premières) :")
    for i in range(min(10, len(w))):
        print(f"  E[{i}] = {w[i]:.6f}")
    
    print(f"\nÉnergies minimale et maximale :")
    print(f"  E_min = {w[0]:.6f}")
    print(f"  E_max = {w[-1]:.6f}")


if __name__ == "__main__":
    main()
