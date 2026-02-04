# TP4 : Valeurs propres et vecteurs propres - Résolution de l'équation de Schrödinger

## Description

Ce TP porte sur la résolution numérique de l'équation de Schrödinger stationnaire unidimensionnelle à l'aide de la méthode des différences finies. On étudie trois types de potentiels : puits infini, oscillateur harmonique et double puits.

### Équation de Schrödinger

L'équation de Schrödinger stationnaire s'écrit :

```
Ĥψ(x) = Eψ(x)
```

avec l'hamiltonien :

```
Ĥ = -ℏ²/(2m) d²/dx² + V(x)
```

### Méthode numérique

On discrétise l'espace en `n` points sur l'intervalle `[-L/2, L/2]` :

- `x_i = -L/2 + i·δx` avec `δx = L/(n-1)` et `i = 0, 1, ..., n-1`
- Conditions aux limites : `ψ(-L/2) = ψ(L/2) = 0` (murs infinis)

La dérivée seconde est approchée par :

```
d²ψ/dx² ≈ (ψ_{i+1} - 2ψ_i + ψ_{i-1}) / δx²
```

L'équation devient un problème de valeurs propres matriciel :

```
H·Ψ = E·Ψ
```

où `H` est une matrice tridiagonale.

## Structure

```
TP4/
├── python/           # Scripts Python
│   ├── q01_q02.py   # Définition et tracé des potentiels
│   ├── q03.py       # Interprétation conditions aux limites
│   ├── q04_q05.py   # Construction et diagonalisation hamiltonien
│   ├── q06.py       # Puits infini : comparaison énergies
│   ├── q07.py       # Normalisation et visualisation fonctions d'onde
│   ├── q08.py       # Comparaison détaillée ψ_num vs ψ_theo (p=1, p=55)
│   ├── q09.py       # Oscillateur harmonique : énergies (L=5)
│   ├── q10.py       # Oscillateur harmonique : énergies (L=20)
│   ├── q11.py       # Oscillateur harmonique : fonctions d'onde
│   ├── q12.py       # Double puits symétrique (a=1)
│   ├── q13.py       # Double puits symétrique profond (a=400)
│   └── q14.py       # Double puits asymétrique
├── figures/          # Graphiques générés
├── latex/           # Classe LaTeX personnalisée
├── rapport/         # Compte-rendu LaTeX
│   ├── compte_rendu.tex
│   └── compile.sh
├── README.md        # Ce fichier
└── run_all.py       # Script pour exécuter tous les programmes

```

## Questions

### Partie I : Configuration initiale (Q1-Q2)

**Q1-Q2** : Définir trois potentiels et les tracer sur `[-L/2, L/2]` avec `L=5`, `n=100` :

- Puits infini : `V(x) = 0`
- Oscillateur harmonique : `V(x) = x²/2`
- Double puits : polynôme degré 4 avec 4 racines

### Partie II : Conditions aux limites (Q3)

**Q3** : Interpréter physiquement les conditions `ψ(-L/2) = ψ(L/2) = 0`.

### Partie III : Méthode numérique (Q4-Q5)

**Q4** : Construire l'hamiltonien matriciel tridiagonal.

**Q5** : Diagonaliser avec `scipy.linalg.eigh_tridiagonal`.

### Partie IV : Puits infini (Q6-Q8)

**Q6** : Comparer les énergies numériques avec la solution théorique :

```
E_p = π²(p+1)²/L²
```

**Q7** : Normaliser et tracer `|ψ_p|²` décalées de `E_p` pour `p=0,1,2`.

**Q8** : Comparer en détail `ψ_num` et `ψ_theo` pour :

- `p=1` (bon accord)
- `p=55` (mauvais accord → δx trop grand)

### Partie V : Oscillateur harmonique (Q9-Q11)

**Q9** : Étudier `V(x) = x²/2` avec `L=5`, `n=100`. Comparer avec :

```
E_p = (p + 1/2)√2
```

**Q10** : Refaire avec `L=20` pour analyser l'effet des conditions aux limites.

**Q11** : Tracer `V(x)` et `|ψ_p|²` pour `p=0,1,2`.

### Partie VI : Double puits (Q12-Q14)

**Q12** : Double puits symétrique avec `a=1`, `L=20`, `n=1000` :

- Observer les doublets quasi-dégénérés
- États symétriques/antisymétriques

**Q13** : Refaire avec `a=400` (barrière haute) :

- Suppression de l'effet tunnel
- Quasi-dégénérescence parfaite

**Q14** : Briser la symétrie avec `r3=0` au lieu de `0.5` :

- Plus de symétrie/antisymétrie
- Levée de dégénérescence

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

### Exécuter tous les programmes

```bash
python run_all.py
```

### Exécuter un programme spécifique

```bash
cd python
python q01_q02.py
python q06.py
# etc.
```

### Compiler le rapport LaTeX

```bash
cd rapport
./compile.sh
```

## Dépendances

- Python 3.x
- NumPy : calculs numériques
- SciPy : diagonalisation tridiagonale
- Matplotlib : visualisation

## Résultats attendus

- Figures PDF dans `figures/`
- Rapport PDF compilé dans `rapport/`
- Analyse comparative numérique vs théorique
- Étude de l'effet tunnel dans le double puits
- Impact de la discrétisation spatiale

## Notes physiques

### Puits infini

- Solution exacte connue : `ψ_p(x) = √(2/L) sin(π(p+1)(x+L/2)/L)`
- Limitation : δx doit être petit devant la longueur d'onde

### Oscillateur harmonique

- `ℏω = √2` dans nos unités
- Fonctions d'onde gaussiennes pour les bas niveaux
- Conditions aux limites artificielles : L doit être grand

### Double puits

- Doublets : effet tunnel entre les deux puits
- Barrière haute → découplage
- Brisure de symétrie → levée de dégénérescence

## Auteur

TP de Physique Numérique - Master de Physique

## Licence

Usage académique uniquement.
