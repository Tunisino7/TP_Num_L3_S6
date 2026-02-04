# -*- coding: utf-8 -*-
"""
TP3 - Question 6 : Surface structurée (algorithme de Métropolis)

Modèle avec atomes de surface organisés en réseau carré.
Implémentation de l'algorithme de Métropolis pour la probabilité d'adsorption.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q01 import coord, place_libre


def dist_latt(x_new, y_new):
    """
    Calcule la distance du centre de la particule à l'atome le plus proche.

    Les atomes sont aux coordonnées entières (0, 0), (0, 1), (1, 0), etc.

    Paramètres :
        x_new, y_new : coordonnées de la particule

    Retour :
        distance à l'atome le plus proche
    """
    x_atom = np.rint(x_new)
    y_atom = np.rint(y_new)

    distance = np.sqrt((x_new - x_atom)**2 + (y_new - y_atom)**2)

    return distance


def remplissage_surface_structuree(L, R, MAX_TRIES, r_surf, U, T):
    """
    Simule le remplissage avec interactions de surface (algorithme de Métropolis).

    Paramètres :
        L : côté du carré
        R : rayon des particules
        MAX_TRIES : nombre d'échecs consécutifs maximum
        r_surf : distance caractéristique d'interaction
        U : coût énergétique pour s'éloigner des atomes
        T : température (en unités kB*T)

    Retour :
        x, y : coordonnées des particules adsorbées
        n : nombre de particules
    """
    N_MAX = int(L**2 / (np.pi * R**2))

    x = np.empty(N_MAX)
    y = np.empty(N_MAX)

    n = 0
    echecs = 0

    while echecs < MAX_TRIES:
        x_new = coord(L, R)
        y_new = coord(L, R)

        if place_libre(n, x, y, x_new, y_new, R) == 0:
            echecs += 1
            continue

        d = dist_latt(x_new, y_new)

        accepter = False

        if d < r_surf:
            accepter = True
        else:
            if T == 0:
                accepter = False
            else:
                if T * np.log(np.random.rand()) < -U:
                    accepter = True

        if accepter:
            x[n] = x_new
            y[n] = y_new
            n += 1
            echecs = 0
        else:
            echecs += 1

    return x[:n], y[:n], n


def visualiser_avec_reseau(x, y, R, L, T, filename):
    """
    Visualise l'adsorption avec le réseau d'atomes de surface.
    """
    fig, ax = plt.subplots(figsize=(10, 10))

    for i in range(int(L) + 1):
        for j in range(int(L) + 1):
            ax.plot(i, j, 'rx', markersize=3, markeredgewidth=0.5)

    circles = [plt.Circle((xi, yi), radius=R, linewidth=0.5,
                         edgecolor='black', facecolor='blue', alpha=0.6)
               for xi, yi in zip(x, y)]

    c = matplotlib.collections.PatchCollection(circles, match_original=True)
    ax.add_collection(c)

    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_aspect('equal')
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(f'Adsorption sur surface structurée (T = {T})\n' +
                 f'{len(x)} particules adsorbées', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Figure sauvegardée : {output_path}")

    plt.show()


def main():
    """
    Programme principal - Test pour une température donnée
    """
    L = 20.0
    R = 0.4
    MAX_TRIES = 10000
    r_surf = 0.05
    U = 10.0
    T = 0.0

    np.random.seed(42)

    print("=== Adsorption sur surface structurée ===")
    print(f"Paramètres :")
    print(f"  L = {L}, R = {R}")
    print(f"  MAX_TRIES = {MAX_TRIES}")
    print(f"  r_surf = {r_surf}, U = {U}")
    print(f"  Température T = {T}")
    print("\nSimulation en cours...")

    x, y, n = remplissage_surface_structuree(L, R, MAX_TRIES, r_surf, U, T)

    fraction = n * np.pi * R**2 / L**2

    print(f"\n=== Résultats ===")
    print(f"Nombre de particules : {n}")
    print(f"Fraction de surface : {fraction:.4f} ({fraction*100:.2f}%)")

    visualiser_avec_reseau(x, y, R, L, T, "q06.pdf")

    print("\nRéponse aux questions théoriques :")
    print("• Pour T → ∞ : exp(-U/T) → 1, on retrouve le modèle homogène (Q1)")
    print("• Pour T = 0 : seules les particules à d < r_surf sont acceptées")
    print("  → adsorption uniquement près des atomes (sites préférentiels)")


if __name__ == "__main__":
    main()
