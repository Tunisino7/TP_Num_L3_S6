#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TP3 - Script d'exécution de toutes les questions

Ce script exécute toutes les questions du TP3 dans l'ordre.
"""

import os
import sys
import subprocess

# Liste des questions à exécuter
QUESTIONS = ['q01', 'q02', 'q03', 'q04', 'q05', 'q06', 'q07', 'q08', 'q09', 'q10', 'q11']

def run_question(question):
    """
    Exécute une question.
    
    Paramètres :
        question : nom de la question (sans extension)
    """
    print(f"\n{'='*70}")
    print(f"Exécution de {question}.py")
    print(f"{'='*70}\n")
    
    script_path = os.path.join('python', f'{question}.py')
    
    try:
        result = subprocess.run([sys.executable, script_path], check=True)
        print(f"\n✓ {question}.py terminé avec succès")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Erreur lors de l'exécution de {question}.py")
        print(f"Code de retour : {e.returncode}")
        return False
    except FileNotFoundError:
        print(f"\n✗ Fichier {script_path} introuvable")
        return False


def main():
    """
    Programme principal
    """
    print("╔" + "═"*68 + "╗")
    print("║" + " "*22 + "TP3 - Exécution complète" + " "*22 + "║")
    print("║" + " "*15 + "Adsorption de particules sur surface" + " "*16 + "║")
    print("╚" + "═"*68 + "╝")
    
    # S'assurer d'être dans le bon répertoire
    if not os.path.exists('python'):
        print("\n✗ Erreur : répertoire 'python' introuvable")
        print("Assurez-vous d'exécuter ce script depuis le répertoire TP3/")
        sys.exit(1)
    
    # Créer le répertoire figures s'il n'existe pas
    if not os.path.exists('figures'):
        os.makedirs('figures')
        print("\n✓ Répertoire 'figures' créé")
    
    # Exécuter toutes les questions
    success_count = 0
    for question in QUESTIONS:
        if run_question(question):
            success_count += 1
    
    # Résumé
    print(f"\n{'='*70}")
    print(f"RÉSUMÉ")
    print(f"{'='*70}")
    print(f"Questions réussies : {success_count}/{len(QUESTIONS)}")
    
    if success_count == len(QUESTIONS):
        print("\n✓ Toutes les questions ont été exécutées avec succès !")
        print("✓ Les figures sont disponibles dans le répertoire 'figures/'")
    else:
        print(f"\n✗ {len(QUESTIONS) - success_count} question(s) en erreur")
        sys.exit(1)


if __name__ == "__main__":
    main()
