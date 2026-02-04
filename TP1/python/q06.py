# -*- coding: utf-8 -*-
"""
Question 6 : Particule chargée dans des champs E et B uniformes
Trajectoire dans le plan x-y avec E = E ux et B = B uz
"""
import numpy as np
import matplotlib.pyplot as plt


def deriv(t, y, params):
    """
    Dérivées pour une particule chargée dans E et B.
    
    Vecteur d'état : y = [x, y, vx, vy]
    Équations : m dv/dt = q(E + v × B)
    Unités choisies : q/m = E = B = 1
    
    E = Ex ux → force qE dans direction x
    B = B uz → force de Lorentz v × B
    
    dvx/dt = E + vy*B
    dvy/dt = -vx*B
    """
    dy = np.zeros(4)
    dy[0] = y[2]        # dx/dt = vx
    dy[1] = y[3]        # dy/dt = vy
    dy[2] = 1.0 + y[3]  # dvx/dt = E + vy*B (avec E=B=1)
    dy[3] = -y[2]       # dvy/dt = -vx*B
    return dy


def euler(t, dt, y, deriv, params):
    """Un pas d'Euler."""
    dy = deriv(t, y, params)
    return y + dt * dy


# ========== Paramètres ==========
# Unités : q/m = E = B = 1
x0, y0 = 0.0, 0.0
vx0, vy0 = 0.0, 1.0
dt = 0.01
t_max = 50.0

# ========== Simulation ==========
temps = np.arange(0.0, t_max + dt, dt)
n_points = temps.size

x_traj = np.empty(n_points)
y_traj = np.empty(n_points)

y = np.array([x0, y0, vx0, vy0])

for i in range(n_points):
    x_traj[i] = y[0]
    y_traj[i] = y[1]
    t = temps[i]
    y = euler(t, dt, y, deriv, None)

# ========== Graphe ==========
plt.figure(figsize=(10, 6))
plt.plot(x_traj, y_traj, '-', linewidth=1.5)
plt.xlabel('Position x')
plt.ylabel('Position y')
plt.title('Question 6 : Trajectoire d\'une particule chargée (E et B uniformes)')
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.tight_layout()
plt.savefig('../figures/q06.pdf')
print("✓ Graphe q06.pdf sauvegardé")

plt.show()

print("\n📊 Analyse :")
print("La trajectoire combine une dérive (due à E) et une rotation cyclotron (due à B).")
print("Le mouvement est périodique avec déplacement dans la direction x.")
