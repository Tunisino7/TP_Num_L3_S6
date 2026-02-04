# -*- coding: utf-8 -*-
"""
Question 8 : Utilisation de RK4
Comparaison de l'erreur avec la méthode d'Euler
"""
import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4


def deriv(t, y, params):
    """Dérivées pour l'oscillateur harmonique."""
    omega = params
    dy = np.zeros(2)
    dy[0] = y[1]
    dy[1] = -omega**2 * y[0]
    return dy


def solution_analytique(t, x0, v0, omega):
    """Solution exacte de l'oscillateur."""
    return x0 * np.cos(omega * t) + (v0 / omega) * np.sin(omega * t)


def simuler_rk4(dt, t_max, omega, x0, v0):
    """Simule l'oscillateur avec RK4."""
    temps = np.arange(0.0, t_max + dt, dt)
    n_points = temps.size
    x_values = np.empty(n_points)
    
    y = np.array([x0, v0])
    for i in range(n_points):
        x_values[i] = y[0]
        t = temps[i]
        y = rk4(t, dt, y, deriv, omega)
    
    return temps, x_values


# ========== Paramètres ==========
omega = 1.0
x0 = 1.0
v0 = 0.0
t_max = 100.0  # Temps plus long pour voir l'avantage de RK4

# Deux pas de temps à comparer
pas_temps = [0.01, 0.005]

# ========== Graphe ==========
plt.figure(figsize=(10, 6))

for dt in pas_temps:
    temps, x_num = simuler_rk4(dt, t_max, omega, x0, v0)
    x_theo = solution_analytique(temps, x0, v0, omega)
    erreur = x_num - x_theo
    plt.plot(temps, erreur, label=f'RK4, dt = {dt}')

plt.xlabel('Temps t')
plt.ylabel('x(t) - x_th(t)')
plt.title('Question 8 : Erreur de RK4 sur l\'oscillateur harmonique')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/q08.pdf')
print("✓ Graphe q08.pdf sauvegardé")

plt.show()

print("\n📊 Observation :")
print("- RK4 est beaucoup plus précis qu'Euler")
print("- L'erreur reste très petite même sur de longues durées")
print("- RK4 d'ordre 4 : erreur ~ (dt)⁵")
