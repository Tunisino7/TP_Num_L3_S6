# -*- coding: utf-8 -*-
"""
TP3 - Question 8 : Courbe η(T) avec M = 100 simulations

Étude de la fraction moyenne de surface occupée en fonction de la température
pour T ∈ [0, 10] avec ΔT = 0,5. Utilisation de numba si disponible.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from q06 import remplissage_surface_structuree

try:
    from numba import njit
    NUMBA_OK = True
except Exception:
    NUMBA_OK = False


if NUMBA_OK:
    @njit
    def coord_nb(L, R):
        return R + np.random.rand() * (L - 2 * R)


    @njit
    def place_libre_nb(n, x, y, x_new, y_new, R):
        if n == 0:
            return 1
        for i in range(n):
            dx = x[i] - x_new
            dy = y[i] - y_new
            if np.sqrt(dx * dx + dy * dy) < 2 * R:
                return 0
        return 1


    @njit
    def dist_latt_nb(x_new, y_new):
        x_atom = np.rint(x_new)
        y_atom = np.rint(y_new)
        return np.sqrt((x_new - x_atom) ** 2 + (y_new - y_atom) ** 2)


    @njit
    def remplissage_struct_nb(L, R, MAX_TRIES, r_surf, U, T):
        N_MAX = int(L ** 2 / (np.pi * R ** 2))
        x = np.empty(N_MAX)
        y = np.empty(N_MAX)
        n = 0
        echecs = 0

        while echecs < MAX_TRIES:
            x_new = coord_nb(L, R)
            y_new = coord_nb(L, R)

            if place_libre_nb(n, x, y, x_new, y_new, R) == 0:
                echecs += 1
                continue

            d = dist_latt_nb(x_new, y_new)

            accepter = False
            if d < r_surf:
                accepter = True
            else:
                if T == 0.0:
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

        return n


    @njit
    def moyenne_fraction_nb(L, R, MAX_TRIES, r_surf, U, T, M):
        frac = np.empty(M)
        for i in range(M):
            n = remplissage_struct_nb(L, R, MAX_TRIES, r_surf, U, T)
            frac[i] = n * np.pi * R ** 2 / L ** 2
        return np.mean(frac), np.std(frac)


def etude_temperature(L, R, MAX_TRIES, r_surf, U, T_values, M):
    """
    Calcule la fraction moyenne de surface pour différentes températures.
    """
    fractions_moy = []
    fractions_std = []

    for T in T_values:
        print(f"Température T = {T:.1f} ...")
        if NUMBA_OK:
            moy, std = moyenne_fraction_nb(L, R, MAX_TRIES, r_surf, U, T, M)
        else:
            fractions = []
            for _ in range(M):
                _, _, n = remplissage_surface_structuree(L, R, MAX_TRIES, r_surf, U, T)
                fractions.append(n * np.pi * R ** 2 / L ** 2)
            moy = float(np.mean(fractions))
            std = float(np.std(fractions))

        fractions_moy.append(moy)
        fractions_std.append(std)

    return np.array(T_values), np.array(fractions_moy), np.array(fractions_std)


def main():
    """
    Programme principal
    """
    L = 20.0
    R = 0.4
    MAX_TRIES = 10000
    r_surf = 0.05
    U = 10.0

    np.random.seed(42)

    if NUMBA_OK:
        print("Numba détecté : calcul accéléré activé.")
    else:
        print("Numba non détecté : calculs plus lents (mode Python).")

    T_range = np.arange(0, 10.5, 0.5)
    M = 100

    T_vals, frac_moy, frac_std = etude_temperature(L, R, MAX_TRIES, r_surf, U, T_range, M)

    plt.figure(figsize=(12, 7))

    plt.errorbar(T_vals, frac_moy, yerr=frac_std, fmt='o-',
                capsize=3, capthick=1, markersize=5, linewidth=1.5,
                label=f'Simulation (M={M})')

    plt.axhline(y=np.pi * np.sqrt(3) / 6, color='green', linestyle='--',
                linewidth=1.5, label=f'Empilement hexagonal (η={np.pi*np.sqrt(3)/6:.3f})')
    plt.axhline(y=np.pi / 4, color='orange', linestyle='--',
                linewidth=1.5, label=f'Empilement carré (η={np.pi/4:.3f})')

    plt.xlabel('Température T', fontsize=13)
    plt.ylabel('Fraction de surface occupée η', fontsize=13)
    plt.title("Fraction de surface en fonction de la température", fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'q08.pdf')
    plt.savefig(output_path, dpi=150)
    print(f"Figure sauvegardée : {output_path}")

    plt.show()


if __name__ == "__main__":
    main()
