# -*- coding: utf-8 -*-
"""
Question 9 : Accélération avec numba
Comparaison des performances entre code standard et code optimisé
"""
import time
import numpy as np

try:
    from numba import njit
    NUMBA_DISPONIBLE = True
except ImportError:
    print("⚠️  numba n'est pas installé. Installation recommandée : pip install numba")
    NUMBA_DISPONIBLE = False
    # Fallback : décorateur vide
    def njit(func):
        return func


# ========== Fonctions standard (sans numba) ==========
def deriv_standard(t, y, params):
    """Dérivées standard."""
    omega = params
    dy = np.zeros(2)
    dy[0] = y[1]
    dy[1] = -omega**2 * y[0]
    return dy


def rk4_standard(t, dt, y, deriv, params):
    """RK4 standard."""
    demi_pas = dt / 2.0
    d1 = deriv(t, y, params)
    yp = y + d1 * demi_pas
    d2 = deriv(t + demi_pas, yp, params)
    yp = y + d2 * demi_pas
    d3 = deriv(t + demi_pas, yp, params)
    yp = y + d3 * dt
    d4 = deriv(t + dt, yp, params)
    return y + dt * (d1 + 2 * d2 + 2 * d3 + d4) / 6.0


def integrer_standard(t_max, dt, y_init, omega):
    """Boucle d'intégration standard."""
    temps = np.arange(0.0, t_max, dt)
    n_points = temps.size
    y = np.copy(y_init)
    
    for i in range(n_points):
        t = temps[i]
        y = rk4_standard(t, dt, y, deriv_standard, omega)
    
    return y


# ========== Fonctions numba (si disponible) ==========
@njit
def deriv_numba(t, y, params):
    """Dérivées avec numba."""
    omega = params
    dy = np.zeros(2)
    dy[0] = y[1]
    dy[1] = -omega**2 * y[0]
    return dy


@njit
def rk4_numba(t, dt, y, deriv, params):
    """RK4 avec numba."""
    demi_pas = dt / 2.0
    d1 = deriv(t, y, params)
    yp = y + d1 * demi_pas
    d2 = deriv(t + demi_pas, yp, params)
    yp = y + d2 * demi_pas
    d3 = deriv(t + demi_pas, yp, params)
    yp = y + d3 * dt
    d4 = deriv(t + dt, yp, params)
    return y + dt * (d1 + 2 * d2 + 2 * d3 + d4) / 6.0


@njit
def integrer_numba(t_max, dt, y_init, omega):
    """Boucle d'intégration avec numba."""
    temps = np.arange(0.0, t_max, dt)
    n_points = temps.size
    y = np.copy(y_init)
    
    for i in range(n_points):
        t = temps[i]
        y = rk4_numba(t, dt, y, deriv_numba, omega)
    
    return y


# ========== Tests de performance ==========
if __name__ == "__main__":
    # Paramètres
    omega = 1.0
    dt = 0.001
    t_max = 100.0
    y_init = np.array([1.0, 0.0])
    
    print("=" * 60)
    print("Question 9 : Comparaison des performances")
    print("=" * 60)
    
    # Test 1 : Code standard
    print("\n📊 Test 1 : Code Python standard")
    start = time.time()
    y_standard = integrer_standard(t_max, dt, y_init, omega)
    temps_standard = time.time() - start
    print(f"   Temps d'exécution : {temps_standard:.3f} s")
    
    # Test 2 : Code numba (si disponible)
    if NUMBA_DISPONIBLE:
        # Pré-compilation (premier appel)
        print("\n📊 Test 2 : Code avec numba")
        print("   Compilation en cours...")
        _ = integrer_numba(1.0, dt, y_init, omega)
        
        # Mesure réelle
        start = time.time()
        y_numba = integrer_numba(t_max * 10, dt, y_init, omega)  # 10x plus long
        temps_numba = time.time() - start
        print(f"   Temps d'exécution (t_max × 10) : {temps_numba:.3f} s")
        
        # Calcul du gain
        facteur = (temps_standard * 10) / temps_numba
        print(f"\n✨ Gain de performance : {facteur:.1f}x plus rapide avec numba")
    else:
        print("\n⚠️  numba non disponible : impossible de comparer les performances")
    
    print("\n" + "=" * 60)
