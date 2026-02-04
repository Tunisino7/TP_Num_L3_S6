# -*- coding: utf-8 -*-
"""
Question 2 : Désintégration en chaîne X → Y → Z
Système d'EDO : dx/dt = -kx, dy/dt = kx - k2*y
"""
import numpy as np
import matplotlib.pyplot as plt

# ========== Paramètres ==========
k = 1.0
k2 = 0.1 * k
x0 = 1.0
y0 = 0.0
dt = 0.05
t_max = 20.0

# ========== Calcul numérique (Euler) ==========
temps = np.arange(0.0, t_max + dt, dt)
n_points = temps.size

x_values = np.empty(n_points)
y_values = np.empty(n_points)

x = x0
y = y0

for i in range(n_points):
    x_values[i] = x
    y_values[i] = y
    
    dx = -k * x
    dy = k * x - k2 * y
    
    x = x + dt * dx
    y = y + dt * dy

# ========== Graphe ==========
plt.figure(figsize=(8, 5))
plt.plot(temps, x_values, 'o-', label='x(t) - élément X', markersize=3)
plt.plot(temps, y_values, 's-', label='y(t) - élément Y', markersize=3)
plt.xlabel('Temps t')
plt.ylabel('Densité')
plt.title('Question 2 : Désintégration X → Y → Z')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/q02.pdf')
print("✓ Graphe q02.pdf sauvegardé")

plt.show()
