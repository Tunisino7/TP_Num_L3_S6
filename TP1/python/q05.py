# -*- coding: utf-8 -*-
"""
Question 5 : Fonction euler() générique
Implémentation et test sur l'oscillateur harmonique
"""
import numpy as np
import matplotlib.pyplot as plt


def deriv(t, y, params):
    """Calcule les dérivées pour l'oscillateur harmonique."""
    omega = params
    dy = np.zeros(2)
    dy[0] = y[1]
    dy[1] = -omega**2 * y[0]
    return dy


def euler(t, dt, y, deriv, params):
    """
    Effectue un pas d'intégration par la méthode d'Euler.
    
    Paramètres
    ----------
    t : float
        Temps actuel.
    dt : float
        Pas de temps.
    y : ndarray
        Tableau des valeurs au temps t.
    deriv : callable
        Fonction qui calcule les dérivées.
    params : float ou ndarray
        Paramètres physiques.
    
    Retour
    ------
    ndarray
        Nouvelles valeurs au temps t + dt.
    """
    dy = deriv(t, y, params)
    return y + dt * dy


# ========== Simulation complète ==========
if __name__ == "__main__":
    # Paramètres
    omega = 1.0
    dt = 0.1
    t_max = 50.0
    
    # Grille temporelle
    temps = np.arange(0.0, t_max + dt, dt)
    n_points = temps.size
    
    # Tableaux pour x(t) et v(t)
    x_tab = np.empty(n_points)
    v_tab = np.empty(n_points)
    
    # Conditions initiales
    y = np.array([1.0, 0.0])  # [x0, v0]
    
    # Boucle d'intégration
    for i in range(n_points):
        x_tab[i] = y[0]
        v_tab[i] = y[1]
        t = temps[i]
        y = euler(t, dt, y, deriv, omega)
    
    # ========== Graphe ==========
    plt.figure(figsize=(10, 6))
    plt.plot(temps, x_tab, 'o-', label='x(t) - Position', markersize=3)
    plt.plot(temps, v_tab, 's-', label='v(t) - Vitesse', markersize=3)
    plt.xlabel('Temps t')
    plt.ylabel('x(t), v(t)')
    plt.title('Question 5 : Oscillateur avec fonction euler()')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../figures/q05.pdf')
    print("✓ Graphe q05.pdf sauvegardé")
    
    plt.show()
