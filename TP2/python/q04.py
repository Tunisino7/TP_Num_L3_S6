# -*- coding: utf-8 -*-
"""
TP2 - Question 4 : Sensibilité aux conditions initiales et exposant de Lyapunov

On compare l'évolution du pendule pour deux conditions initiales très proches :
    θ(0) = 10° et θ(0) = 9.999°

On calcule l'exposant de Lyapunov λ qui caractérise la vitesse de divergence
des trajectoires dans un système chaotique.
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
    """
    Omega, q, Fe, Omega_e = params
    dy = np.empty(2)
    dy[0] = y[1]
    dy[1] = -q * y[1] - Omega**2 * np.sin(y[0]) + Fe * np.sin(Omega_e * t)
    return dy


def maintenir_angle_dans_intervalle(theta):
    """
    Maintient l'angle dans l'intervalle [-π, π].
    """
    while theta > np.pi:
        theta -= 2 * np.pi
    while theta < -np.pi:
        theta += 2 * np.pi
    return theta


def simuler_pendule_deux_conditions(theta0_1_deg, theta0_2_deg, Fe=1.5, 
                                     q=0.5, Omega=1.0, Omega_e=None, 
                                     omega0=0.0, dt=0.05, t_max=100.0):
    """
    Simule le pendule pour deux conditions initiales différentes.
    
    Paramètres :
        theta0_1_deg : premier angle initial (degrés)
        theta0_2_deg : second angle initial (degrés)
        Fe : amplitude de la force excitatrice (rad/s²)
        q : coefficient d'amortissement (s⁻¹)
        Omega : pulsation propre (rad/s)
        Omega_e : pulsation de la force excitatrice (rad/s)
        omega0 : vitesse angulaire initiale (rad/s)
        dt : pas de temps (s)
        t_max : temps final (s)
    
    Retour :
        t_array : tableau des temps
        theta1_array : angles pour la première condition initiale
        theta2_array : angles pour la seconde condition initiale
    """
    # Pulsation excitatrice par défaut
    if Omega_e is None:
        Omega_e = 2.0 * Omega / 3.0
    
    # Conversion des angles initiaux en radians
    theta0_1 = np.radians(theta0_1_deg)
    theta0_2 = np.radians(theta0_2_deg)
    
    # Conditions initiales pour les deux simulations
    y1 = np.array([theta0_1, omega0])
    y2 = np.array([theta0_2, omega0])
    
    # Paramètres physiques
    params = np.array([Omega, q, Fe, Omega_e])
    
    # Nombre de pas de temps
    n_steps = int(t_max / dt)
    
    # Tableaux pour stocker les résultats
    t_array = np.zeros(n_steps + 1)
    theta1_array = np.zeros(n_steps + 1)
    theta2_array = np.zeros(n_steps + 1)
    
    # Conditions initiales
    t_array[0] = 0.0
    theta1_array[0] = theta0_1
    theta2_array[0] = theta0_2
    
    # Boucle d'intégration
    t = 0.0
    for i in range(n_steps):
        # Intégration des deux systèmes
        y1 = rk4(t, dt, y1, deriv_pendule_non_lineaire, params)
        y2 = rk4(t, dt, y2, deriv_pendule_non_lineaire, params)
        t += dt
        
        # Maintenir θ dans [-π, π] pour les deux systèmes
        y1[0] = maintenir_angle_dans_intervalle(y1[0])
        y2[0] = maintenir_angle_dans_intervalle(y2[0])
        
        t_array[i + 1] = t
        theta1_array[i + 1] = y1[0]
        theta2_array[i + 1] = y2[0]
    
    return t_array, theta1_array, theta2_array


def main():
    """
    Programme principal : étudie la sensibilité aux conditions initiales
    """
    # Paramètres de la simulation
    Omega = 1.0       # rad/s
    Omega_e = 2.0 * Omega / 3.0  # rad/s
    q = 0.5           # s⁻¹
    Fe = 1.5          # rad/s²
    theta0_1_deg = 10.0     # degrés
    theta0_2_deg = 9.999    # degrés
    omega0 = 0.0      # rad/s
    dt = 0.05         # s
    t_max = 100.0     # s
    
    print(f"Simulation pour deux conditions initiales :")
    print(f"  θ₁(0) = {theta0_1_deg}°")
    print(f"  θ₂(0) = {theta0_2_deg}°")
    print(f"  Écart initial : {theta0_1_deg - theta0_2_deg}°")
    
    # Simulation
    t_array, theta1, theta2 = simuler_pendule_deux_conditions(
        theta0_1_deg, theta0_2_deg, Fe, q, Omega, Omega_e, omega0, dt, t_max
    )
    
    # Conversion en degrés
    theta1_deg = np.degrees(theta1)
    theta2_deg = np.degrees(theta2)
    
    # Calcul de l'écart
    ecart = theta1 - theta2
    ecart_abs = np.abs(ecart)
    
    # Pour éviter les problèmes de log(0), on remplace les zéros par une petite valeur
    ecart_abs_safe = np.where(ecart_abs > 1e-10, ecart_abs, 1e-10)
    log_ecart = np.log(ecart_abs_safe)
    
    # Création de la figure avec 2 sous-graphiques
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # --- Graphique 1 : Trajectoires θ(t) ---
    ax1.plot(t_array, theta1_deg, label=f'θ₁(0) = {theta0_1_deg}°', 
            linewidth=1.2, color='blue')
    ax1.plot(t_array, theta2_deg, label=f'θ₂(0) = {theta0_2_deg}°', 
            linewidth=1.2, color='red', linestyle='--')
    ax1.set_xlabel('Temps t (s)', fontsize=12)
    ax1.set_ylabel('Angle θ (degrés)', fontsize=12)
    ax1.set_title('Comparaison des trajectoires pour deux conditions initiales proches', 
                 fontsize=13, fontweight='bold')
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3)
    
    # --- Graphique 2 : Logarithme de l'écart ---
    ax2.plot(t_array, log_ecart, linewidth=1.5, color='purple', label='ln(|θ₁ - θ₂|)')
    
    # Ajustement linéaire pour déterminer l'exposant de Lyapunov
    # On utilise la région où la croissance est approximativement linéaire (par ex. t ∈ [10, 40])
    idx_fit = (t_array >= 10) & (t_array <= 40)
    if np.sum(idx_fit) > 0:
        # Régression linéaire : log(écart) = λ*t + b
        coeffs = np.polyfit(t_array[idx_fit], log_ecart[idx_fit], 1)
        lambda_lyapunov = coeffs[0]
        b = coeffs[1]
        
        # Droite d'ajustement
        fit_line = lambda_lyapunov * t_array + b
        ax2.plot(t_array, fit_line, '--', linewidth=2, color='orange', 
                label=f'Ajustement linéaire : λ ≈ {lambda_lyapunov:.4f} s⁻¹')
        
        print(f"\n=== Exposant de Lyapunov ===")
        print(f"λ ≈ {lambda_lyapunov:.4f} s⁻¹")
        print(f"\nInterprétation :")
        print(f"  • λ > 0 : le système est chaotique")
        print(f"  • L'écart entre les trajectoires croît exponentiellement comme e^(λt)")
        print(f"  • Temps caractéristique : τ = 1/λ ≈ {1/lambda_lyapunov:.2f} s")
        print(f"\nConclusion :")
        print(f"  Les capacités de prédiction à long terme sont limitées car une petite")
        print(f"  incertitude sur les conditions initiales est amplifiée exponentiellement.")
        print(f"  Après environ {3/lambda_lyapunov:.1f} s, l'erreur devient significative.")
    
    ax2.set_xlabel('Temps t (s)', fontsize=12)
    ax2.set_ylabel('ln(|θ₁ - θ₂|)', fontsize=12)
    ax2.set_title('Logarithme de l\'écart absolu entre les deux trajectoires', 
                 fontsize=13, fontweight='bold')
    ax2.legend(fontsize=11)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Sauvegarde de la figure
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'q04.pdf')
    plt.savefig(output_path)
    print(f"\nFigure sauvegardée : {output_path}")
    
    plt.show()


if __name__ == "__main__":
    main()
