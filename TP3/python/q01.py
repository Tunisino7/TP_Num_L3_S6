# -*- coding: utf-8 -*-
"""
TP3 - Question 1 : Adsorption de particules sur une surface homogène

Simulation de l'adsorption de particules de gaz sur une surface cristalline.
Les particules sont modélisées par des disques impénétrables qui ne peuvent
pas se chevaucher.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections
import os


def coord(L, R):
    """
    Génère une coordonnée aléatoire valide pour le centre d'une particule.
    
    Paramètres :
        L : côté du carré (surface d'adsorption)
        R : rayon des particules
    
    Retour :
        coordonnée aléatoire dans [R, L-R]
    """
    return R + np.random.rand() * (L - 2*R)


def place_libre(n, x, y, x_new, y_new, R):
    """
    Vérifie si la place est libre pour une nouvelle particule.
    
    Paramètres :
        n : nombre de particules déjà adsorbées
        x, y : tableaux des coordonnées des particules existantes
        x_new, y_new : coordonnées de la nouvelle particule à tester
        R : rayon des particules
    
    Retour :
        1 si la place est libre, 0 sinon
    """
    if n == 0:
        return 1
    
    # Vérifier le chevauchement avec toutes les particules existantes
    for i in range(n):
        distance = np.sqrt((x[i] - x_new)**2 + (y[i] - y_new)**2)
        if distance < 2 * R:
            return 0  # Chevauchement détecté
    
    return 1  # Aucun chevauchement


def remplissage(L, R, MAX_TRIES):
    """
    Simule le remplissage de la surface par adsorption de particules.
    
    Paramètres :
        L : côté du carré
        R : rayon des particules
        MAX_TRIES : nombre maximum d'échecs consécutifs avant arrêt
    
    Retour :
        x : tableau des abscisses des particules adsorbées
        y : tableau des ordonnées des particules adsorbées
        n : nombre de particules adsorbées
    """
    # Borne supérieure du nombre de particules
    N_MAX = int(L**2 / (np.pi * R**2))
    
    # Tableaux pour stocker les coordonnées
    x = np.empty(N_MAX)
    y = np.empty(N_MAX)
    
    n = 0  # Nombre de particules adsorbées
    echecs = 0  # Compteur d'échecs consécutifs
    
    while echecs < MAX_TRIES:
        # Tirage aléatoire de coordonnées
        x_new = coord(L, R)
        y_new = coord(L, R)
        
        # Test si l'emplacement est libre
        libre = place_libre(n, x, y, x_new, y_new, R)
        
        if libre == 1:
            # Ajout de la nouvelle particule
            x[n] = x_new
            y[n] = y_new
            n += 1
            echecs = 0  # Réinitialiser le compteur
        else:
            echecs += 1  # Incrémenter le compteur d'échecs
    
    # Retourner seulement la partie remplie des tableaux
    return x[:n], y[:n], n


def visualiser_adsorption(x, y, R, L, filename="q01.pdf"):
    """
    Visualise la configuration finale de l'adsorption.
    
    Paramètres :
        x, y : coordonnées des particules
        R : rayon des particules
        L : côté du carré
        filename : nom du fichier de sortie
    """
    # Créer une liste de cercles matplotlib
    circles = [plt.Circle((xi, yi), radius=R, linewidth=0, color='b', alpha=0.7) 
               for xi, yi in zip(x, y)]
    
    # Créer une collection de cercles
    c = matplotlib.collections.PatchCollection(circles, match_original=True)
    
    # Configuration du graphique
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(x, y, s=1, color='red')  # Points centraux (pour les axes)
    ax.add_collection(c)
    
    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_aspect('equal')
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(f'Adsorption de particules sur surface homogène\n' + 
                 f'({len(x)} particules adsorbées)', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Sauvegarde
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Figure sauvegardée : {output_path}")
    
    plt.show()


def main():
    """
    Programme principal
    """
    # Paramètres de la simulation
    L = 20.0          # Côté du carré
    R = 0.4           # Rayon des particules
    MAX_TRIES = 1000  # Nombre d'échecs consécutifs maximum
    
    # Fixer la graine pour la reproductibilité
    np.random.seed(42)
    
    print("=== Simulation d'adsorption sur surface homogène ===")
    print(f"Paramètres :")
    print(f"  L = {L}")
    print(f"  R = {R}")
    print(f"  MAX_TRIES = {MAX_TRIES}")
    print(f"  Surface totale = {L**2:.2f}")
    print(f"  N_MAX théorique = {int(L**2 / (np.pi * R**2))}")
    print("\nSimulation en cours...")
    
    # Simulation
    x, y, n = remplissage(L, R, MAX_TRIES)
    
    # Calcul de la fraction de surface occupée
    surface_particules = n * np.pi * R**2
    fraction_surface = surface_particules / L**2
    
    print(f"\n=== Résultats ===")
    print(f"Nombre de particules adsorbées : {n}")
    print(f"Surface occupée : {surface_particules:.2f}")
    print(f"Fraction de surface occupée : {fraction_surface:.4f} ({fraction_surface*100:.2f}%)")
    
    # Visualisation
    visualiser_adsorption(x, y, R, L)


if __name__ == "__main__":
    main()
