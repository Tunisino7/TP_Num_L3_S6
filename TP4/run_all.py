#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour exécuter tous les programmes du TP4 séquentiellement.
"""

import os
import sys
import subprocess
import time

# Questions à exécuter (dans l'ordre)
QUESTIONS = [
    'q01_q02',  # Potentiels
    'q03',      # Conditions aux limites
    'q04_q05',  # Hamiltonien
    'q06',      # Puits : énergies
    'q07',      # Puits : fonctions d'onde
    'q08',      # Puits : comparaison détaillée
    'q09',      # Harmonique : L=5
    'q10',      # Harmonique : L=20
    'q11',      # Harmonique : fonctions d'onde
    'q12',      # Double puits symétrique a=1
    'q13',      # Double puits symétrique a=400
    'q14',      # Double puits asymétrique
]


def run_question(question):
    """
    Exécute un programme de question.
    
    Paramètres :
        question : nom du fichier sans extension (ex: 'q01_q02')
    
    Retour :
        True si succès, False si erreur
    """
    script_path = os.path.join('python', f'{question}.py')
    
    if not os.path.exists(script_path):
        print(f"❌ Fichier non trouvé : {script_path}")
        return False
    
    print(f"\n{'='*70}")
    print(f"▶️  Exécution : {question}")
    print(f"{'='*70}\n")
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            check=True,
            capture_output=False
        )
        print(f"\n✅ {question} terminé avec succès")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erreur lors de l'exécution de {question}")
        print(f"Code de retour : {e.returncode}")
        return False
    
    except KeyboardInterrupt:
        print(f"\n⚠️  Interruption par l'utilisateur")
        raise
    
    except Exception as e:
        print(f"\n❌ Erreur inattendue : {e}")
        return False


def main():
    """
    Programme principal
    """
    print("=" * 70)
    print("TP4 : Résolution de l'équation de Schrödinger")
    print("=" * 70)
    print(f"\nNombre de questions à exécuter : {len(QUESTIONS)}")
    print(f"Questions : {', '.join(QUESTIONS)}\n")
    
    # Vérifier que le répertoire figures existe
    figures_dir = os.path.join(os.path.dirname(__file__), 'figures')
    if not os.path.exists(figures_dir):
        os.makedirs(figures_dir)
        print(f"📁 Répertoire créé : {figures_dir}\n")
    
    # Exécuter toutes les questions
    start_time = time.time()
    success_count = 0
    failed_questions = []
    
    for i, question in enumerate(QUESTIONS, 1):
        print(f"\n[{i}/{len(QUESTIONS)}] Traitement de {question}...")
        
        if run_question(question):
            success_count += 1
        else:
            failed_questions.append(question)
        
        # Petit délai entre les exécutions
        if i < len(QUESTIONS):
            time.sleep(1)
    
    # Résumé
    elapsed_time = time.time() - start_time
    print(f"\n{'='*70}")
    print("RÉSUMÉ")
    print(f"{'='*70}")
    print(f"✅ Succès : {success_count}/{len(QUESTIONS)}")
    
    if failed_questions:
        print(f"❌ Échecs : {len(failed_questions)}")
        print(f"   Questions échouées : {', '.join(failed_questions)}")
    
    print(f"⏱️  Temps total : {elapsed_time:.1f} secondes")
    print(f"📊 Figures générées dans : {figures_dir}")
    print(f"{'='*70}\n")
    
    return 0 if success_count == len(QUESTIONS) else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Programme interrompu par l'utilisateur")
        sys.exit(130)
