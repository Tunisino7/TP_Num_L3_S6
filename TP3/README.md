# TP3 : Adsorption de particules sur une surface

## Description

Ce TP étudie l'adsorption de particules circulaires sur une surface par simulation de Monte Carlo. On explore différents scénarios : surface homogène, analyse statistique, surface structurée avec interaction énergétique, et études paramétriques.

## Structure du projet

```
TP3/
├── README.md                 # Ce fichier
├── run_all.py               # Script d'exécution de toutes les questions
├── python/                  # Scripts Python
│   ├── q01.py              # Surface homogène (algorithme RSA)
│   ├── q02.py              # Visualisation de la configuration finale
│   ├── q03.py              # Analyse statistique (M simulations)
│   ├── q04.py              # Comparaison avec empilement ordonné
│   ├── q05.py              # Limites en température
│   ├── q06.py              # Surface structurée (Metropolis)
│   ├── q07.py              # Configurations pour T = 0,1,2,5,10
│   ├── q08.py              # Courbe η(T) avec M=100 (numba)
│   ├── q09.py              # Interprétation de η(T)
│   ├── q10.py              # Convergence avec MAX_TRIES
│   └── q11.py              # Accélération numba et extension MAX_TRIES
├── figures/                 # Figures générées (PDF)
├── latex/                   # Classe LaTeX personnalisée
│   └── TP.cls
└── rapport/                 # Rapport LaTeX
    ├── compte_rendu.tex
    ├── compile.sh
    └── _minted/            # Fichiers minted (générés)
```

## Questions traitées

### Question 1 : Surface homogène

- **Fichier** : `python/q01.py`
- **Description** : Simulation d'adsorption RSA (Random Sequential Adsorption) sur surface homogène
- **Fonctions** :
  - `coord(L, R)` : Génère coordonnées aléatoires
  - `place_libre(n, x, y, x_new, y_new, R)` : Teste absence de chevauchement
  - `remplissage(L, R, MAX_TRIES)` : Algorithme de remplissage
- **Paramètres** : L=20, R=0.4, MAX_TRIES=10000
- **Sortie** : Figure avec configuration finale et fraction de surface

### Question 2 : Visualisation

- **Fichier** : `python/q02.py`
- **Description** : Affichage de la configuration finale RSA et vérification visuelle
- **Sortie** : Figure avec la configuration finale

### Question 3 : Analyse statistique

- **Fichier** : `python/q03.py`
- **Description** : Répétition de M=20 simulations pour analyser variabilité statistique
- **Calculs** :
  - Nombre moyen de particules ⟨n⟩
  - Écart-type σ_n
  - Fraction moyenne de surface ⟨η⟩

### Question 4 : Comparaison avec empilement ordonné

- **Fichier** : `python/q04.py`
- **Description** : Calcul des fractions pour empilements carré et hexagonal

### Question 5 : Limites en température

- **Fichier** : `python/q05.py`
- **Description** : Cas T→∞ et T=0 (modèle homogène vs sites préférentiels)

### Question 6 : Surface structurée

- **Fichier** : `python/q06.py`
- **Description** : Adsorption avec réseau d'atomes et critère de Metropolis
- **Algorithme** :
  - Atomes aux positions entières (i, j)
  - Énergie d'interaction U si d > r_surf
  - Probabilité d'acceptation : P = exp(-U/T)
- **Paramètres** : r_surf=0.05, U=10, T variable
- **Sortie** : Configurations avec réseau atomique visible

### Question 7 : Configurations à différentes températures

- **Fichier** : `python/q07.py`
- **Description** : Configurations finales pour T = 0, 1, 2, 5, 10

### Question 8 : Courbe η(T)

- **Fichier** : `python/q08.py`
- **Description** : Étude de η(T) pour T ∈ [0, 10] avec ΔT = 0,5
- **Calcul** : M=100 simulations par température (numba si disponible)

### Question 9 : Interprétation

- **Fichier** : `python/q09.py`
- **Description** : Discussion qualitative de la courbe η(T)

### Question 10 : Convergence avec MAX_TRIES

- **Fichier** : `python/q10.py`
- **Description** : Étude de l'influence de MAX_TRIES sur η
- **Valeurs testées** : 1000, 2000, 4000, 8000, 16000, 32000
- **Analyse** : M=20 simulations par valeur
- **Graphe** : η(MAX_TRIES) en échelle semi-log avec barres d'erreur
- **Conclusion** : Convergence autour 10000-16000 tentatives

### Question 11 : Accélération numba

- **Fichier** : `python/q11.py`
- **Description** : Extension jusqu'à MAX_TRIES = 512000 avec M=100

## Installation

### Dépendances Python

```bash
pip install numpy matplotlib
```

Ou avec conda :

```bash
conda install numpy matplotlib
```

### LaTeX

Pour compiler le rapport, installer :

- `pdflatex`
- Package `minted` (coloration syntaxique)
- `pygments` (requis par minted) : `pip install pygments`

## Utilisation

### Exécution complète

Pour exécuter toutes les questions d'un coup :

```bash
cd TP3
python3 run_all.py
```

Les figures seront générées dans `figures/`.

### Exécution individuelle

Pour exécuter une question spécifique :

```bash
cd TP3/python
python3 q01.py  # Par exemple
```

### Compilation du rapport

```bash
cd TP3/rapport
./compile.sh
```

Ou manuellement :

```bash
pdflatex -shell-escape compte_rendu.tex
```

**Note** : L'option `-shell-escape` est requise pour `minted`.

## Résultats attendus

### Figures générées

- `q01.pdf` : Configuration RSA finale (Q1)
- `q02.pdf` : Configuration finale (Q2)
- `q06.pdf` : Configuration avec réseau atomique (Q6)
- `q07_T0.pdf`, ..., `q07_T10.pdf` : Configurations pour différentes T (Q7)
- `q08.pdf` : Courbe η(T) (Q8)
- `q10.pdf` : Convergence avec MAX_TRIES (Q10)
- `q11.pdf` : Extension MAX_TRIES avec numba (Q11)

### Valeurs typiques

- **RSA (Q1)** : η ≈ 0.54-0.55 (limite théorique ≈ 0.547)
- **Avec atomes T→0 (Q3)** : η plus élevée (empilement ordonné)
- **Avec atomes T élevée (Q4)** : η ≈ RSA (perte d'ordre)
- **Convergence (Q5)** : Stabilisation pour MAX_TRIES ≥ 10000

## Paramètres par défaut

```python
L = 20.0          # Longueur du côté de la surface
R = 0.4           # Rayon des particules
MAX_TRIES = 10000 # Nombre max de tentatives consécutives
r_surf = 0.05     # Rayon d'interaction avec atomes
U = 10.0          # Énergie d'interaction (en unités kT)
M = 20            # Nombre de simulations (sauf Q4: M=100)
```

## Concepts physiques

### Random Sequential Adsorption (RSA)

- Placement séquentiel de particules
- Sans chevauchement (sphères dures)
- État "jamming" à η ≈ 0.547 en 2D

### Algorithme de Metropolis

- Acceptation probabiliste basée sur l'énergie
- P_accept = min(1, exp(-ΔE/kT))
- Monte Carlo à température finie

### Transition de phase

- Ordre → désordre avec température
- Température critique T_c
- Analogue des transitions vitreuses

## Auteur

Lotfi Bentaleb

## Notes

- Toutes les distances sont en unités arbitraires
- L'énergie U est en unités de kT
- Utilisation de `np.random.seed()` pour reproductibilité
