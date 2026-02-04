# -*- coding: utf-8 -*-
"""
TP3 - Question 11 : Accélération avec numba

Extension de l'étude MAX_TRIES jusqu'à 512000 avec M=100 répétitions.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

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
    def remplissage_nb(L, R, MAX_TRIES):
        N_MAX = int(L ** 2 / (np.pi * R ** 2))
        x = np.empty(N_MAX)
        y = np.empty(N_MAX)
        n = 0
        echecs = 0

        while echecs < MAX_TRIES:
            x_new = coord_nb(L, R)
            y_new = coord_nb(L, R)

            if place_libre_nb(n, x, y, x_new, y_new, R) == 1:
                x[n] = x_new
                y[n] = y_new
                n += 1
                echecs = 0
            else:
                echecs += 1

        return n


    @njit
    def stats_nb(L, R, MAX_TRIES, M):
        frac = np.empty(M)
        for i in range(M):
            n = remplissage_nb(L, R, MAX_TRIES)
            frac[i] = n * np.pi * R ** 2 / L ** 2
        return np.mean(frac), np.std(frac)


def main():
    """
    Programme principal
    """
    L = 20.0
    R = 0.4
    M = 100

    MAX_TRIES_values = [1000 * (2 ** k) for k in range(0, 10)]  # 1000 à 512000

    np.random.seed(42)

    if NUMBA_OK:
        print("Numba détecté : calcul accéléré activé.")
    else:
        print("Numba non détecté : calculs très lents en mode Python.")

    frac_moy = []
    frac_std = []

    for MAX_TRIES in MAX_TRIES_values:
        print(f"MAX_TRIES = {MAX_TRIES} ...")
        if NUMBA_OK:
            moy, std = stats_nb(L, R, MAX_TRIES, M)
        else:
            fractions = []
            for _ in range(M):
                n = 0
                x = np.empty(int(L ** 2 / (np.pi * R ** 2)))
                y = np.empty(int(L ** 2 / (np.pi * R ** 2)))
                echecs = 0
                while echecs < MAX_TRIES:
                    x_new = R + np.random.rand() * (L - 2 * R)
                    y_new = R + np.random.rand() * (L - 2 * R)
                    libre = 1
                    for i in range(n):
                        dx = x[i] - x_new
                        dy = y[i] - y_new
                        if np.sqrt(dx * dx + dy * dy) < 2 * R:
                            libre = 0
                            break
                    if libre == 1:
                        x[n] = x_new
                        y[n] = y_new
                        n += 1
                        echecs = 0
                    else:
                        echecs += 1
                fractions.append(n * np.pi * R ** 2 / L ** 2)
            moy = float(np.mean(fractions))
            std = float(np.std(fractions))

        frac_moy.append(moy)
        frac_std.append(std)

    plt.figure(figsize=(12, 7))
    plt.errorbar(MAX_TRIES_values, frac_moy, yerr=frac_std, fmt='o-'
                , capsize=4, capthick=1.5, markersize=6, linewidth=1.5)
    plt.xscale('log')
    plt.xlabel('MAX_TRIES', fontsize=13)
    plt.ylabel('Fraction de surface occupée η', fontsize=13)
    plt.title('Étude de convergence (M=100) avec numba', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, which='both')
    plt.tight_layout()

    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'q11.pdf')
    plt.savefig(output_path, dpi=150)
    print(f"Figure sauvegardée : {output_path}")

    plt.show()


if __name__ == "__main__":
    main()
