# TP1 : Méthode d'Euler et RK4

## 📁 Structure du projet

```
TP1/
├── python/          # Code source
│   ├── q01.py       # Question 1
│   ├── q02.py       # Question 2
│   ├── ...
│   ├── q09.py       # Question 9
│   └── rk4.py       # Fonction RK4
├── figures/         # Graphiques générés
│   ├── q01a.pdf
│   ├── q01b.pdf
│   └── ...
├── latex/           # Classe LaTeX
│   └── TP.cls
├── rapport/         # Compte rendu LaTeX
│   └── compte_rendu.tex
└── run_all.py       # Script d'exécution
```

## 🚀 Exécution rapide

### Exécuter toutes les questions

```bash
cd TP1
python run_all.py
```

### Exécuter une question spécifique

```bash
python run_all.py 1        # Question 1
python run_all.py 5        # Question 5
```

### Exécuter une plage de questions

```bash
python run_all.py 1-5      # Questions 1 à 5
python run_all.py 7-9      # Questions 7 à 9
```

### Depuis le dossier python/

```bash
cd python
python q01.py
python q02.py
# etc.
```

## 📝 Liste des questions

1. **q01.py** - Désintégration radioactive X → Y (Euler)
2. **q02.py** - Chaîne X → Y → Z
3. **q03.py** - Oscillateur harmonique (effet du dt)
4. **q04.py** - Fonction deriv()
5. **q05.py** - Fonction euler()
6. **q06.py** - Particule chargée dans E et B
7. **q07.py** - Erreur d'Euler
8. **q08.py** - Utilisation de RK4
9. **q09.py** - Accélération avec numba

## 📊 Génération du rapport

Le compte rendu est dans `rapport/compte_rendu.tex`.

⚠️ **Important** : Utilisez l'option `-shell-escape` pour que le code s'affiche correctement.

### Compilation automatique

```bash
cd TP1/rapport
./compile.sh
```

### Compilation manuelle

```bash
cd TP1/rapport
pdflatex -shell-escape compte_rendu.tex
pdflatex -shell-escape compte_rendu.tex  # 2× pour la table des matières
```

Ou avec latexmk :

```bash
cd TP1/rapport
latexmk -pdf -shell-escape compte_rendu.tex
```

### Dépendances LaTeX

Le package `minted` nécessite Pygments :

```bash
pip install Pygments
```

Le PDF généré sera dans `rapport/compte_rendu.pdf`.

## 🎨 Style des graphiques

- Graphiques en **couleur** (pas noir et blanc)
- Format PDF haute qualité
- Sauvegardés automatiquement dans `figures/`
- Affichage interactif avec `plt.show()`

## 📦 Dépendances

```bash
pip install numpy matplotlib
pip install numba  # optionnel pour q09.py
```

## 💡 Astuces

- Les fichiers génèrent automatiquement les PDF dans `figures/`
- Chaque script affiche un message de confirmation
- Les graphiques s'affichent à l'écran puis sont fermés
- Pas besoin de configMatplotlib (couleurs par défaut)

## 🔧 Convention de nommage

- **q01.py, q02.py...** : code Python (cohérent avec le template)
- **q01a.pdf, q01b.pdf** : graphiques (a, b pour les sous-parties)
- **Commentaires en français** dans tout le code
