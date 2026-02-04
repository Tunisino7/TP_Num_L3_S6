# -*- coding: utf-8 -*-
"""
Question 3 : Oscillateur harmonique avec Euler
Étude de l'influence du pas de temps dt
"""
import numpy as np
import matplotlib.pyplot as plt

# ========== Paramètres ==========
omega = 1.0
x0 = 1.0
v0 = 0.0
t_max = 100.0

# Liste de pas de temps à tester
pas_temps = [0.2, 0.1, 0.05, 0.01]

# ========== Fonction de simulation ==========
def simuler_euler(dt, t_max, omega, x0, v0):
    """Simule l'oscillateur harmonique avec Euler."""
    temps = np.arange(0.0, t_max + dt, dt)
    n_points = temps.size
    
    x_values = np.empty(n_points)
    
    x = x0
    v = v0
    
    for i in range(n_points):
        x_values[i] = x
        dx = v
        dv = -omega**2 * x
        x = x + dt * dx
        v = v + dt * dv
    
    return temps, x_values

# ========== Graphe avec plusieurs dt ==========
plt.figure(figsize=(10, 6))

for dt in pas_temps:
    temps, x_values = simuler_euler(dt, t_max, omega, x0, v0)
    plt.plot(temps, x_values, label=f'dt = {dt}', alpha=0.8)

plt.xlabel('Temps t')
plt.ylabel('Position x(t)')
plt.title('Question 3 : Oscillateur harmonique - Effet du pas de temps (Euler)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/q03.pdf')
print("✓ Graphe q03.pdf sauvegardé")

plt.show()

print("\n📊 Observation :")
print("Avec un pas de temps trop grand, l'amplitude diverge.")
print("L'erreur s'accumule et l'énergie n'est pas conservée.")
