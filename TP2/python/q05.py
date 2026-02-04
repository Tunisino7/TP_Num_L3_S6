# -*- coding: utf-8 -*-
"""
TP2 - Question 5 : Diagramme de bifurcation (Pour aller plus loin)

On trace le diagramme de bifurcation pour mettre en évidence la transition
vers le régime chaotique. On observe l'état du système à des instants 
tn = 2πn/Ωe (en phase avec la fréquence excitatrice), comme avec un stroboscope.
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


def calculer_diagramme_bifurcation(Fe_min, Fe_max, n_Fe, q=0.5, Omega=1.0, 
                                    Omega_e=None, theta0_deg=10.0, omega0=0.0, 
                                    dt=None, n_transitoire=200, n_mesure=100):
    """
    Calcule le diagramme de bifurcation en variant Fe.
    
    Paramètres :
        Fe_min : valeur minimale de Fe (rad/s²)
        Fe_max : valeur maximale de Fe (rad/s²)
        n_Fe : nombre de valeurs de Fe à tester
        q : coefficient d'amortissement (s⁻¹)
        Omega : pulsation propre (rad/s)
        Omega_e : pulsation de la force excitatrice (rad/s)
        theta0_deg : angle initial (degrés)
        omega0 : vitesse angulaire initiale (rad/s)
        dt : pas de temps (s), si None, calculé à partir de Omega_e
        n_transitoire : nombre de périodes à ignorer (régime transitoire)
        n_mesure : nombre de points à mesurer après le transitoire
    
    Retour :
        Fe_list : liste des valeurs de Fe
        theta_list : liste des angles mesurés (correspondants à chaque Fe)
    """
    # Pulsation excitatrice par défaut
    if Omega_e is None:
        Omega_e = 2.0 * Omega / 3.0
    
    # Période d'excitation
    T_e = 2 * np.pi / Omega_e
    
    # Pas de temps adapté pour faciliter les calculs
    if dt is None:
        dt = T_e / 200.0  # 200 points par période
    
    # Conversion de l'angle initial en radians
    theta0 = np.radians(theta0_deg)
    
    # Valeurs de Fe à tester
    Fe_array = np.linspace(Fe_min, Fe_max, n_Fe)
    
    # Listes pour stocker les résultats
    Fe_list = []
    theta_list = []
    
    # Boucle sur les valeurs de Fe
    for idx, Fe in enumerate(Fe_array):
        if (idx + 1) % 10 == 0:
            print(f"Progression : {idx + 1}/{n_Fe} (Fe = {Fe:.4f})")
        
        # Conditions initiales
        y = np.array([theta0, omega0])
        params = np.array([Omega, q, Fe, Omega_e])
        
        # Phase 1 : Éliminer le régime transitoire
        t = 0.0
        n_steps_transitoire = int(n_transitoire * T_e / dt)
        for _ in range(n_steps_transitoire):
            y = rk4(t, dt, y, deriv_pendule_non_lineaire, params)
            t += dt
            y[0] = maintenir_angle_dans_intervalle(y[0])
        
        # Phase 2 : Mesurer θ à des instants multiples de la période T_e
        # On cherche à mesurer quand t ≈ n*T_e (n entier)
        n_steps_per_period = int(T_e / dt)
        
        for _ in range(n_mesure):
            # Intégrer sur une période complète
            for _ in range(n_steps_per_period):
                y = rk4(t, dt, y, deriv_pendule_non_lineaire, params)
                t += dt
                y[0] = maintenir_angle_dans_intervalle(y[0])
            
            # Enregistrer la valeur de θ à cet instant "stroboscopique"
            Fe_list.append(Fe)
            theta_list.append(y[0])
    
    return np.array(Fe_list), np.array(theta_list)


def main():
    """
    Programme principal : trace le diagramme de bifurcation
    """
    # Paramètres de la simulation
    Omega = 1.0       # rad/s
    Omega_e = 2.0 * Omega / 3.0  # rad/s
    q = 0.5           # s⁻¹
    theta0_deg = 10.0 # degrés
    omega0 = 0.0      # rad/s
    
    # Paramètres pour le diagramme de bifurcation
    # Vous pouvez tester différents intervalles :
    # - Option 1 : Fe ∈ [1.41, 1.50]
    # - Option 2 : Fe ∈ [2.55, 2.90]
    Fe_min = 2.55
    Fe_max = 2.90
    n_Fe = 90  # Nombre de valeurs de Fe (augmenter pour plus de détails)
    
    n_transitoire = 200  # Nombre de périodes pour le transitoire
    n_mesure = 100       # Nombre de points à mesurer par valeur de Fe
    
    print("=== Calcul du diagramme de bifurcation ===")
    print(f"Fe ∈ [{Fe_min}, {Fe_max}] avec {n_Fe} valeurs")
    print(f"Régime transitoire : {n_transitoire} périodes")
    print(f"Mesures : {n_mesure} points par Fe")
    print("\nCalcul en cours...\n")
    
    # Calcul du diagramme
    Fe_list, theta_list = calculer_diagramme_bifurcation(
        Fe_min, Fe_max, n_Fe, q, Omega, Omega_e, 
        theta0_deg, omega0, None, n_transitoire, n_mesure
    )
    
    # Garder θ en radians pour l'affichage
    
    # Création de la figure
    plt.figure(figsize=(12, 8))
    
    # Tracer le diagramme de bifurcation
    # On utilise des points pour voir la structure
    plt.plot(Fe_list, theta_list, '.', color='darkblue', markersize=1.0, alpha=0.7)
    
    # Mise en forme du graphique
    plt.xlabel('Amplitude d\'excitation Fe (rad/s²)', fontsize=13)
    plt.ylabel('Angle θ (rad)', fontsize=13)
    plt.title(f'Diagramme de bifurcation du pendule chaotique\n' + 
              f'(Ω = {Omega} rad/s, Ωe = {Omega_e:.3f} rad/s, q = {q} s⁻¹)', 
              fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.xlim(Fe_min, Fe_max)
    plt.ylim(-3, 3)
    plt.tight_layout()
    
    # Sauvegarde de la figure
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'q05.pdf')
    plt.savefig(output_path, dpi=300)  # Haute résolution pour voir les détails
    print(f"\nFigure sauvegardée : {output_path}")
    
    plt.show()
    
    # Observations
    print("\n=== Observations ===")
    print("Le diagramme de bifurcation montre la transition progressive vers le chaos :")
    print("  • Régions avec peu de points : comportement périodique (régime stationnaire)")
    print("  • Régions avec bifurcations : doublement de période")
    print("  • Régions denses : comportement chaotique (trajectoires apériodiques)")
    print("\nCe diagramme est un outil puissant pour identifier les valeurs de Fe")
    print("qui conduisent à un comportement chaotique du pendule.")


if __name__ == "__main__":
    main()
