# -*- coding: utf-8 -*-
"""
TP2 - Question 3 : Pendule chaotique (équation non-linéaire)

On résout l'équation différentielle non-linéaire :
    d²θ/dt² + q*dθ/dt + Ω²*sin(θ) = Fe*sin(Ωe*t)

On étudie le comportement pour différentes amplitudes d'excitation Fe.
L'angle θ est maintenu dans l'intervalle [-π, π].
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Ajouter le chemin pour importer rk4
sys.path.append(os.path.dirname(__file__))
from rk4 import rk4


def deriv_pendule_non_lineaire(t, y, params):
    """
    Calcule les dérivées pour le pendule non-linéaire avec excitation.
    
    Équation : d²θ/dt² + q*dθ/dt + Ω²*sin(θ) = Fe*sin(Ωe*t)
    
    Variables d'état :
        y[0] = θ (angle)
        y[1] = dθ/dt (vitesse angulaire)
    
    Paramètres :
        params = [Ω, q, Fe, Ωe]
    
    Retour :
        dy[0] = dθ/dt = y[1]
        dy[1] = d²θ/dt² = -q*y[1] - Ω²*sin(y[0]) + Fe*sin(Ωe*t)
    """
    Omega, q, Fe, Omega_e = params
    dy = np.empty(2)
    dy[0] = y[1]                                                          # dθ/dt
    dy[1] = -q * y[1] - Omega**2 * np.sin(y[0]) + Fe * np.sin(Omega_e * t)  # d²θ/dt²
    return dy


def maintenir_angle_dans_intervalle(theta):
    """
    Maintient l'angle dans l'intervalle [-π, π].
    
    Paramètre :
        theta : angle (rad)
    
    Retour :
        angle normalisé dans [-π, π]
    """
    while theta > np.pi:
        theta -= 2 * np.pi
    while theta < -np.pi:
        theta += 2 * np.pi
    return theta


def simuler_pendule_non_lineaire(Fe, q=0.5, Omega=1.0, Omega_e=None, 
                                  theta0_deg=10.0, omega0=0.0, 
                                  dt=0.05, t_max=100.0):
    """
    Simule le pendule non-linéaire avec excitation.
    
    Paramètres :
        Fe : amplitude de la force excitatrice (rad/s²)
        q : coefficient d'amortissement (s⁻¹)
        Omega : pulsation propre (rad/s)
        Omega_e : pulsation de la force excitatrice (rad/s)
        theta0_deg : angle initial en degrés
        omega0 : vitesse angulaire initiale (rad/s)
        dt : pas de temps (s)
        t_max : temps final (s)
    
    Retour :
        t_array : tableau des temps
        theta_array : tableau des angles θ(t)
    """
    # Pulsation excitatrice par défaut
    if Omega_e is None:
        Omega_e = 2.0 * Omega / 3.0
    
    # Conversion de l'angle initial en radians
    theta0 = np.radians(theta0_deg)
    
    # Conditions initiales : [θ, dθ/dt]
    y = np.array([theta0, omega0])
    
    # Paramètres physiques
    params = np.array([Omega, q, Fe, Omega_e])
    
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
        y = rk4(t, dt, y, deriv_pendule_non_lineaire, params)
        t += dt
        
        # Maintenir θ dans [-π, π]
        y[0] = maintenir_angle_dans_intervalle(y[0])
        
        t_array[i + 1] = t
        theta_array[i + 1] = y[0]
    
    return t_array, theta_array


def main():
    """
    Programme principal : étudie le comportement chaotique pour différents Fe
    """
    # Paramètres de la simulation
    Omega = 1.0       # rad/s
    Omega_e = 2.0 * Omega / 3.0  # rad/s
    q = 0.5           # s⁻¹
    theta0_deg = 10.0 # degrés
    omega0 = 0.0      # rad/s
    dt = 0.05         # s
    t_max = 100.0     # s
    
    # Valeurs de Fe à tester
    Fe_values = [1.4, 1.44, 1.465, 1.5]
    
    # Création de 4 sous-graphiques
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    # Simulation pour chaque valeur de Fe
    for idx, Fe in enumerate(Fe_values):
        print(f"Simulation pour Fe = {Fe} rad/s²...")
        
        t_array, theta_array = simuler_pendule_non_lineaire(
            Fe=Fe, q=q, Omega=Omega, Omega_e=Omega_e,
            theta0_deg=theta0_deg, omega0=omega0, dt=dt, t_max=t_max
        )
        
        # Conversion en degrés pour l'affichage
        theta_deg = np.degrees(theta_array)
        
        # Tracer sur le sous-graphique correspondant
        axes[idx].plot(t_array, theta_deg, linewidth=0.8, color='darkblue')
        axes[idx].set_xlabel('Temps t (s)', fontsize=11)
        axes[idx].set_ylabel('Angle θ (degrés)', fontsize=11)
        axes[idx].set_title(f'Fe = {Fe} rad/s²', fontsize=12, fontweight='bold')
        axes[idx].grid(True, alpha=0.3)
        axes[idx].axhline(y=0, color='red', linestyle='--', linewidth=0.8, alpha=0.5)
    
    # Titre général
    fig.suptitle('Pendule non-linéaire : comportement chaotique\n' + 
                 f'(Ω = {Omega} rad/s, Ωe = {Omega_e:.3f} rad/s, q = {q} s⁻¹)', 
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    # Sauvegarde de la figure
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'q03.pdf')
    plt.savefig(output_path)
    print(f"\nFigure sauvegardée : {output_path}")
    
    plt.show()
    
    # Observations
    print("\n=== Observations ===")
    print("• Fe = 1.4 rad/s²   : mouvement périodique régulier")
    print("• Fe = 1.44 rad/s²  : début de comportement complexe")
    print("• Fe = 1.465 rad/s² : comportement transitoire vers le chaos")
    print("• Fe = 1.5 rad/s²   : comportement chaotique marqué")
    print("\nLa période du mouvement change avec Fe et devient irrégulière (non sinusoïdale)")
    print("pour les valeurs élevées, caractéristique d'un système chaotique.")


if __name__ == "__main__":
    main()
