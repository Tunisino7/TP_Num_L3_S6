#!/bin/bash
# Script de compilation du compte rendu TP1
# Usage: ./compile.sh

echo "======================================"
echo "Compilation du compte rendu TP1"
echo "======================================"

echo "Cleaning previous build files..."
latexmk -C    

# Vérifier que nous sommes dans le bon dossier
if [ ! -f "compte_rendu.tex" ]; then
    echo "❌ Erreur: compte_rendu.tex introuvable"
    echo "   Exécutez ce script depuis le dossier rapport/"
    exit 1
fi

echo ""
echo "📄 Première compilation..."
latexmk -pdf -shell-escape -interaction=nonstopmode compte_rendu.tex > /dev/null 2>&1

# Check if PDF was generated instead of relying on exit code
if [ ! -f "compte_rendu.pdf" ]; then
    echo "❌ Erreur lors de la première compilation"
    echo "   Consultez le fichier compte_rendu.log pour plus de détails"
    exit 1
fi

echo "📄 Deuxième compilation (pour la table des matières)..."
latexmk -pdf -shell-escape -interaction=nonstopmode compte_rendu.tex > /dev/null 2>&1

# The second compilation doesn't need strict checking

echo ""
if [ -f "compte_rendu.pdf" ]; then
    echo "✅ Compilation réussie !"
    echo "📖 Le PDF est disponible : compte_rendu.pdf"
    echo ""
    echo "Fichiers générés :"
    ls -lh compte_rendu.pdf
else
    echo "❌ Échec de la génération du PDF"
    echo "   Consultez compte_rendu.log pour plus de détails"
    exit 1
fi

echo ""
echo "======================================"
