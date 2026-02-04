# -*- coding: utf-8 -*-
"""
TP2 - Question 1 : Pendule simple avec approximation des petits angles

On résout l'équation différentielle linéarisée :
    d²θ/dt² + q*dθ/dt + Ω²*θ = 0

pour différentes valeurs de l'amortissement q (régimes pseudo-périodique, 
critique et apériodique).
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Ajouter le chemin pour importer rk4
sys.path.append(os.path.dirname(__file__))
from rk4 import rk4


def deriv_pendule_lineaire(t, y, params):
    """
    Calcule les dérivées pour le pendule linéarisé.
    
    Équation : d²θ/dt² + q*dθ/dt + Ω²*θ = 0
    
    Variables d'état :
        y[0] = θ (angle)
        y[1] = dθ/dt (vitesse angulaire)
    
    Paramètres :
        params = [Ω, q]
    
    Retour :
        dy[0] = dθ/dt = y[1]
        dy[1] = d²θ/dt² = -q*y[1] - Ω²*y[0]
    """
    Omega, q = params
    dy = np.empty(2)
    dy[0] = y[1]                           # dθ/dt
    dy[1] = -q * y[1] - Omega**2 * y[0]    # d²θ/dt²
    return dy


def simuler_pendule(q, Omega=1.0, theta0_deg=10.0, omega0=0.0, dt=0.05, t_max=20.0):
    """
    Simule le pendule linéarisé pour une valeur d'amortissement donnée.
    
    Paramètres :
        q : coefficient d'amortissement (s⁻¹)
        Omega : pulsation propre (rad/s)
        theta0_deg : angle initial en degrés
        omega0 : vitesse angulaire initiale (rad/s)
        dt : pas de temps (s)
        t_max : temps final (s)
    
    Retour :
        t_array : tableau des temps
        theta_array : tableau des angles θ(t)
    """
    # Conversion de l'angle initial en radians
    theta0 = np.radians(theta0_deg)
    
    # Conditions initiales : [θ, dθ/dt]
    y = np.array([theta0, omega0])
    
    # Paramètres physiques
    params = np.array([Omega, q])
    
    # Nombre de pas de temps
    n_steps = int(t_max / dt)
    
    # Tableaux pour stocker les résultats
    t_array = np.zeros(n_steps + 1)
    theta_array = np.zeros(n_steps + 1)
    
    # Conditions initiales
    t_array[0] = 0.0
    theta_array[0] = theta0
    
    # Boucle d'intégration
    t = 0.0
    for i in range(n_steps):
        y = rk4(t, dt, y, deriv_pendule_lineaire, params)
        t += dt
        t_array[i + 1] = t
        theta_array[i + 1] = y[0]
    
    return t_array, theta_array


def main():
    """
    Programme principal : résout l'équation pour q = 1, 2, 5 s⁻¹
    """
    # Paramètres de la simulation
    Omega = 1.0       # rad/s
    theta0_deg = 10.0 # degrés
    omega0 = 0.0      # rad/s
    dt = 0.05         # s
    t_max = 20.0      # s
    
    # Valeurs de l'amortissement à tester
    q_values = [1.0, 2.0, 5.0]
    labels = ['q = 1 s⁻¹ (pseudo-périodique)', 
              'q = 2 s⁻¹ (critique)', 
              'q = 5 s⁻¹ (apériodique)']
    
    # Création de la figure
    plt.figure(figsize=(10, 6))
    
    # Simulation pour chaque valeur de q
    for q, label in zip(q_values, labels):
        t_array, theta_array = simuler_pendule(q, Omega, theta0_deg, omega0, dt, t_max)
        # Conversion en degrés pour l'affichage
        theta_deg = np.degrees(theta_array)
        plt.plot(t_array, theta_deg, label=label, linewidth=1.5)
    
    # Mise en forme du graphique
    plt.xlabel('Temps t (s)', fontsize=12)
    plt.ylabel('Angle θ (degrés)', fontsize=12)
    plt.title('Pendule linéarisé : régimes d\'amortissement', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Sauvegarde de la figure
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'q01.pdf')
    plt.savefig(output_path)
    print(f"Figure sauvegardée : {output_path}")
    
    plt.show()


if __name__ == "__main__":
    main()
