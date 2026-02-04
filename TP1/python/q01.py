# -*- coding: utf-8 -*-
"""
Question 1 : Désintégration radioactive X → Y
Méthode d'Euler pour dx/dt = -kx
"""
import numpy as np
import matplotlib.pyplot as plt

# ========== Paramètres ==========
k = 1.0         # Taux de désintégration
x0 = 1.0        # Densité initiale
dt = 0.1        # Pas de temps
t_max = 10.0    # Temps maximal

# ========== Calcul numérique (Euler) ==========
temps = np.arange(0.0, t_max + dt, dt)
n_points = temps.size

x_numerique = np.empty(n_points)
x = x0

for i in range(n_points):
    x_numerique[i] = x
    v = -k * x  # dx/dt = -kx
    x = x + dt * v

# ========== Solution analytique ==========
x_analytique = x0 * np.exp(-k * temps)
erreur = x_numerique - x_analytique

# ========== Graphe 1 : Comparaison ==========
plt.figure(figsize=(8, 5))
plt.plot(temps, x_numerique, 'o-', label='Solution numérique (Euler)', markersize=4)
plt.plot(temps, x_analytique, '--', label='Solution analytique', linewidth=2)
plt.xlabel('Temps t')
plt.ylabel('Densité x(t)')
plt.title('Question 1 : Désintégration X → Y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/q01a.pdf')
print("✓ Graphe q01a.pdf sauvegardé")

# ========== Graphe 2 : Erreur ==========
plt.figure(figsize=(8, 5))
plt.plot(temps, erreur, 'o-', color='red', markersize=4)
plt.xlabel('Temps t')
plt.ylabel('x_numérique - x_analytique')
plt.title('Question 1 : Erreur numérique')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/q01b.pdf')
print("✓ Graphe q01b.pdf sauvegardé")

plt.show()
