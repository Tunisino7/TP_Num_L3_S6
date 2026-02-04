# -*- coding: utf-8 -*-
"""
TP2 - Question 2 : Pendule avec force d'excitation

On résout l'équation différentielle linéarisée avec une force excitatrice :
    d²θ/dt² + q*dθ/dt + Ω²*θ = Fe*sin(Ωe*t)

On trace les trajectoires dans l'espace des phases (θ, dθ/dt) pour :
    - Pendule libre (q=0, Fe=0)
    - Pendule amorti (q=1, Fe=0)
    - Pendule amorti avec excitation (q=1, Fe=1)
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Ajouter le chemin pour importer rk4
sys.path.append(os.path.dirname(__file__))
from rk4 import rk4


def deriv_pendule_excite(t, y, params):
    """
    Calcule les dérivées pour le pendule linéarisé avec excitation.
    
    Équation : d²θ/dt² + q*dθ/dt + Ω²*θ = Fe*sin(Ωe*t)
    
    Variables d'état :
        y[0] = θ (angle)
        y[1] = dθ/dt (vitesse angulaire)
    
    Paramètres :
        params = [Ω, q, Fe, Ωe]
    
    Retour :
        dy[0] = dθ/dt = y[1]
        dy[1] = d²θ/dt² = -q*y[1] - Ω²*y[0] + Fe*sin(Ωe*t)
    """
    Omega, q, Fe, Omega_e = params
    dy = np.empty(2)
    dy[0] = y[1]                                                    # dθ/dt
    dy[1] = -q * y[1] - Omega**2 * y[0] + Fe * np.sin(Omega_e * t)  # d²θ/dt²
    return dy


def simuler_pendule_excite(q, Fe, Omega=1.0, Omega_e=None, theta0_deg=10.0, 
                           omega0=0.0, dt=0.05, t_max=50.0):
    """
    Simule le pendule linéarisé avec excitation.
    
    Paramètres :
        q : coefficient d'amortissement (s⁻¹)
        Fe : amplitude de la force excitatrice (rad/s²)
        Omega : pulsation propre (rad/s)
        Omega_e : pulsation de la force excitatrice (rad/s)
        theta0_deg : angle initial en degrés
        omega0 : vitesse angulaire initiale (rad/s)
        dt : pas de temps (s)
        t_max : temps final (s)
    
    Retour :
        theta_array : tableau des angles θ(t)
        omega_array : tableau des vitesses angulaires dθ/dt
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
    theta_array = np.zeros(n_steps + 1)
    omega_array = np.zeros(n_steps + 1)
    
    # Conditions initiales
    theta_array[0] = theta0
    omega_array[0] = omega0
    
    # Boucle d'intégration
    t = 0.0
    for i in range(n_steps):
        y = rk4(t, dt, y, deriv_pendule_excite, params)
        t += dt
        theta_array[i + 1] = y[0]
        omega_array[i + 1] = y[1]
    
    return theta_array, omega_array


def main():
    """
    Programme principal : compare les trajectoires dans l'espace des phases
    """
    # Paramètres de la simulation
    Omega = 1.0       # rad/s
    Omega_e = 2.0 * Omega / 3.0  # rad/s
    theta0_deg = 10.0 # degrés
    omega0 = 0.0      # rad/s
    dt = 0.05         # s
    t_max = 50.0      # s
    
    # Paramètres des trois cas
    configs = [
        {'q': 0.0, 'Fe': 0.0, 'label': 'Pendule libre (q=0, Fe=0)', 'color': 'blue'},
        {'q': 1.0, 'Fe': 0.0, 'label': 'Pendule amorti (q=1, Fe=0)', 'color': 'red'},
        {'q': 1.0, 'Fe': 1.0, 'label': 'Pendule amorti avec excitation (q=1, Fe=1)', 'color': 'green'}
    ]
    
    # Création de la figure
    plt.figure(figsize=(10, 8))
    
    # Simulation pour chaque configuration
    for config in configs:
        theta, omega = simuler_pendule_excite(
            q=config['q'], 
            Fe=config['Fe'], 
            Omega=Omega, 
            Omega_e=Omega_e,
            theta0_deg=theta0_deg, 
            omega0=omega0, 
            dt=dt, 
            t_max=t_max
        )
        
        # Conversion en degrés pour l'affichage
        theta_deg = np.degrees(theta)
        
        plt.plot(theta_deg, omega, label=config['label'], 
                color=config['color'], linewidth=1.2, alpha=0.8)
        
        # Marquer le point initial
        plt.plot(theta_deg[0], omega[0], 'o', color=config['color'], 
                markersize=6, label=f"Début {config['label']}")
    
    # Mise en forme du graphique
    plt.xlabel('Angle θ (degrés)', fontsize=12)
    plt.ylabel('Vitesse angulaire dθ/dt (rad/s)', fontsize=12)
    plt.title('Espace des phases : trajectoires du pendule linéarisé', fontsize=14)
    plt.legend(fontsize=9, loc='best')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Sauvegarde de la figure
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'q02.pdf')
    plt.savefig(output_path)
    print(f"Figure sauvegardée : {output_path}")
    
    plt.show()
    
    # Commentaire sur les trajectoires observées
    print("\n=== Observations ===")
    print("• Pendule libre : trajectoire fermée (ellipse) → mouvement périodique conservatif")
    print("• Pendule amorti : spirale convergeant vers l'origine → dissipation d'énergie")
    print("• Pendule amorti excité : trajectoire complexe → régime permanent forcé")


if __name__ == "__main__":
    main()
