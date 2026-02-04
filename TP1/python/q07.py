# -*- coding: utf-8 -*-
"""
Question 7 : Erreur de la méthode d'Euler
Comparaison avec la solution analytique pour l'oscillateur harmonique
"""
import numpy as np
import matplotlib.pyplot as plt


def deriv(t, y, params):
    """Dérivées pour l'oscillateur harmonique."""
    omega = params
    dy = np.zeros(2)
    dy[0] = y[1]
    dy[1] = -omega**2 * y[0]
    return dy


def euler(t, dt, y, deriv, params):
    """Un pas d'Euler."""
    dy = deriv(t, y, params)
    return y + dt * dy


def solution_analytique(t, x0, v0, omega):
    """Solution exacte : x(t) = x0*cos(ωt) + (v0/ω)*sin(ωt)"""
    return x0 * np.cos(omega * t) + (v0 / omega) * np.sin(omega * t)


def simuler_euler(dt, t_max, omega, x0, v0):
    """Simule l'oscillateur avec Euler et retourne t, x."""
    temps = np.arange(0.0, t_max + dt, dt)
    n_points = temps.size
    x_values = np.empty(n_points)
    
    y = np.array([x0, v0])
    for i in range(n_points):
        x_values[i] = y[0]
        t = temps[i]
        y = euler(t, dt, y, deriv, omega)
    
    return temps, x_values


# ========== Paramètres ==========
omega = 1.0
x0 = 1.0
v0 = 0.0
t_max = 50.0

# Deux pas de temps à comparer
pas_temps = [0.01, 0.005]

# ========== Graphe ==========
plt.figure(figsize=(10, 6))

for dt in pas_temps:
    temps, x_num = simuler_euler(dt, t_max, omega, x0, v0)
    x_theo = solution_analytique(temps, x0, v0, omega)
    erreur = x_num - x_theo
    plt.plot(temps, erreur, label=f'dt = {dt}')

plt.xlabel('Temps t')
plt.ylabel('x(t) - x_th(t)')
plt.title('Question 7 : Erreur d\'Euler sur l\'oscillateur harmonique')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/q07.pdf')
print("✓ Graphe q07.pdf sauvegardé")

plt.show()

print("\n📊 Observation :")
print("- L'erreur croît avec le temps")
print("- Réduire dt diminue l'erreur mais ne la supprime pas complètement")
print("- Euler n'est pas adapté pour de longues simulations")
