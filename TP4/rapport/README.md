# Compilation du rapport TP4

## Prérequis

- LaTeX (distribution complète : TeXLive, MiKTeX, MacTeX)
- Package `minted` pour la coloration syntaxique
- Python avec Pygments (`pip install Pygments`)

## Compilation

### Méthode automatique (recommandée)

```bash
./compile.sh
```

Le script compile automatiquement avec les options nécessaires pour `minted`.

### Méthode manuelle

```bash
pdflatex -shell-escape compte_rendu.tex
pdflatex -shell-escape compte_rendu.tex
```

L'option `-shell-escape` est nécessaire pour que `minted` puisse appeler Pygments.

## Structure

- `compte_rendu.tex` : fichier source principal
- `../latex/TP.cls` : classe LaTeX personnalisée
- `../python/*.py` : codes source inclus via `\progLong{}`
- `../figures/*.pdf` : graphiques générés
- `_minted/` : fichiers temporaires de coloration syntaxique

## Notes

- Compiler deux fois pour générer la table des matières
- Les fichiers `.aux`, `.fls`, `.fdb_latexmk`, `.toc` sont temporaires
- Le PDF final : `compte_rendu.pdf`

## Nettoyage

```bash
rm -rf _minted/ *.aux *.fls *.fdb_latexmk *.toc *.log
```
