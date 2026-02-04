# -*- coding: utf-8 -*-
"""
Question 4 : Fonction deriv() pour l'oscillateur harmonique
Définition de la fonction générique pour calculer les dérivées
"""
import numpy as np


def deriv(t, y, params):
    """
    Calcule les dérivées pour l'oscillateur harmonique.
    
    Le système est :
    dx/dt = v
    dv/dt = -ω² x
    
    Paramètres
    ----------
    t : float
        Temps actuel (non utilisé ici, mais conservé pour l'interface générique).
    y : ndarray
        Tableau [x, v] contenant position et vitesse.
    params : float
        Pulsation propre ω₀.
    
    Retour
    ------
    ndarray
        Tableau [dx/dt, dv/dt] des dérivées.
    """
    omega = params
    dy = np.zeros(2)
    dy[0] = y[1]                # dx/dt = v
    dy[1] = -omega**2 * y[0]    # dv/dt = -ω² x
    return dy


# ========== Test de la fonction ==========
if __name__ == "__main__":
    print("Test de la fonction deriv() :\n")
    
    # État initial : x = 1, v = 0
    y_test = np.array([1.0, 0.0])
    omega_test = 1.0
    
    dy_test = deriv(0.0, y_test, omega_test)
    
    print(f"État initial : x = {y_test[0]}, v = {y_test[1]}")
    print(f"Dérivées : dx/dt = {dy_test[0]}, dv/dt = {dy_test[1]}")
    print("\n✓ Fonction deriv() définie correctement")
