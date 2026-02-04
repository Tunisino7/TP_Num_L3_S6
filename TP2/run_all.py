#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour exécuter toutes les questions du TP2
Usage : python run_all.py [numéro]
        python run_all.py        # exécute tout
        python run_all.py 1      # exécute question1.py uniquement
        python run_all.py 1-3    # exécute question1.py à question3.py
"""
import sys
import os
import subprocess
from pathlib import Path

# Chemin vers le dossier python
PYTHON_DIR = Path(__file__).parent / "python"

# Liste de tous les fichiers de questions
QUESTIONS = [
    ("q01.py", "Pendule linéarisé - régimes d'amortissement"),
    ("q02.py", "Pendule avec force d'excitation - espace des phases"),
    ("q03.py", "Pendule non-linéaire - comportement chaotique"),
    ("q04.py", "Sensibilité aux conditions initiales - exposant de Lyapunov"),
    ("q05.py", "Diagramme de bifurcation (pour aller plus loin)"),
]


def executer_question(numero):
    """Exécute une question spécifique."""
    if numero < 1 or numero > len(QUESTIONS):
        print(f"❌ Question {numero} n'existe pas")
        return False
    
    fichier, description = QUESTIONS[numero - 1]
    chemin = PYTHON_DIR / fichier
    
    print(f"\n{'=' * 70}")
    print(f"📝 Question {numero} : {description}")
    print(f"{'=' * 70}")
    
    if not chemin.exists():
        print(f"❌ Fichier {fichier} introuvable")
        return False
    
    try:
        # Change le répertoire de travail vers python/
        # Utilise python3 explicitement
        python_cmd = 'python3' if os.system('which python3 > /dev/null 2>&1') == 0 else sys.executable
        result = subprocess.run(
            [python_cmd, fichier],
            cwd=PYTHON_DIR,
            check=True,
            capture_output=False
        )
        print(f"\n✅ Question {numero} exécutée avec succès")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erreur lors de l'exécution de la question {numero}")
        return False
    except KeyboardInterrupt:
        print(f"\n⚠️  Exécution interrompue par l'utilisateur")
        return False


def executer_toutes():
    """Exécute toutes les questions."""
    print("\n" + "=" * 70)
    print("🚀 Exécution de toutes les questions du TP2")
    print("=" * 70)
    
    succes = []
    echecs = []
    
    for i in range(1, len(QUESTIONS) + 1):
        if executer_question(i):
            succes.append(i)
        else:
            echecs.append(i)
        
        # Pause entre les questions pour laisser voir les graphiques
        if i < len(QUESTIONS):
            input("\n⏸️  Appuyez sur Entrée pour continuer...")
    
    # Résumé final
    print("\n" + "=" * 70)
    print("📊 RÉSUMÉ")
    print("=" * 70)
    print(f"✅ Réussies : {len(succes)}/{len(QUESTIONS)}")
    if echecs:
        print(f"❌ Échouées : {', '.join(map(str, echecs))}")
    print("=" * 70)


def afficher_aide():
    """Affiche l'aide."""
    print("\n" + "=" * 70)
    print("📚 AIDE - Script d'exécution TP2")
    print("=" * 70)
    print("\nUsage :")
    print("  python run_all.py              # Exécute toutes les questions")
    print("  python run_all.py <n>          # Exécute la question n")
    print("  python run_all.py <n1>-<n2>    # Exécute les questions de n1 à n2")
    print("\nExemples :")
    print("  python run_all.py 1            # Question 1 uniquement")
    print("  python run_all.py 1-3          # Questions 1 à 3")
    print("\nQuestions disponibles :")
    for i, (fichier, description) in enumerate(QUESTIONS, 1):
        print(f"  {i}. {description}")
    print("=" * 70 + "\n")


def main():
    """Point d'entrée principal."""
    if len(sys.argv) == 1:
        # Aucun argument : exécuter tout
        executer_toutes()
    elif sys.argv[1] in ["-h", "--help", "help"]:
        afficher_aide()
    elif "-" in sys.argv[1]:
        # Plage : 1-3
        try:
            debut, fin = map(int, sys.argv[1].split("-"))
            for i in range(debut, fin + 1):
                executer_question(i)
                if i < fin:
                    input("\n⏸️  Appuyez sur Entrée pour continuer...")
        except ValueError:
            print("❌ Format invalide. Utilisez : python run_all.py 1-3")
            afficher_aide()
    else:
        # Numéro unique
        try:
            numero = int(sys.argv[1])
            executer_question(numero)
        except ValueError:
            print(f"❌ '{sys.argv[1]}' n'est pas un numéro valide")
            afficher_aide()


if __name__ == "__main__":
    main()
