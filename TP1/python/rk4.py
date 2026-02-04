# -*- coding: utf-8 -*-
"""
Fonction RK4 pour la résolution d'équations différentielles.
"""
import numpy as np


def rk4(t, dt, y, deriv, params):
    """
    Sous-programme de résolution d'équations différentielles du premier ordre
    par la méthode de Runge-Kutta d'ordre 4.

    Paramètres
    ----------
    t : float
        Temps actuel (abscisse).
    dt : float
        Pas de temps.
    y : ndarray
        Tableau des valeurs des fonctions au temps t (taille n).
    deriv : callable
        Fonction qui calcule les dérivées : deriv(t, y, params) -> dy.
    params : float ou ndarray
        Paramètres physiques nécessaires au calcul.

    Retour
    ------
    ndarray
        Nouvelles valeurs de y au temps t + dt.
    """
    demi_pas = dt / 2.0

    # Première estimation
    d1 = deriv(t, y, params)
    yp = y + d1 * demi_pas

    # Deuxième estimation (demi-pas)
    d2 = deriv(t + demi_pas, yp, params)
    yp = y + d2 * demi_pas

    # Troisième estimation (demi-pas)
    d3 = deriv(t + demi_pas, yp, params)
    yp = y + d3 * dt

    # Quatrième estimation (pas complet)
    d4 = deriv(t + dt, yp, params)

    # Moyenne pondérée : 1/6 + 1/3 + 1/3 + 1/6 = 1
    return y + dt * (d1 + 2 * d2 + 2 * d3 + d4) / 6.0
