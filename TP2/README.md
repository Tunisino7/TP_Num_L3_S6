# TP2 : Pendule chaotique

## 📁 Structure du projet

```
TP2/
├── python/          # Code source
│   ├── q01.py       # Question 1 - Pendule linéarisé
│   ├── q02.py       # Question 2 - Pendule avec excitation
│   ├── q03.py       # Question 3 - Pendule non-linéaire
│   ├── q04.py       # Question 4 - Exposant de Lyapunov
│   ├── q05.py       # Question 5 - Diagramme de bifurcation
│   └── rk4.py       # Fonction RK4
├── figures/         # Graphiques générés
│   ├── q01.pdf
│   ├── q02.pdf
│   └── ...
├── latex/           # Classe LaTeX
│   └── TP.cls
├── rapport/         # Compte rendu LaTeX
│   ├── compte_rendu.tex
│   └── compile.sh
└── run_all.py       # Script d'exécution
```

## 🚀 Exécution rapide

### Exécuter toutes les questions

```bash
cd TP2
python run_all.py
```

### Exécuter une question spécifique

```bash
python run_all.py 1        # Question 1
python run_all.py 4        # Question 4
```

### Exécuter une plage de questions

```bash
python run_all.py 1-3      # Questions 1 à 3
python run_all.py 2-4      # Questions 2 à 4
```

### Depuis le dossier python/

```bash
cd python
python q01.py
python q02.py
# etc.
```

## 📝 Liste des questions

1. **q01.py** - Pendule linéarisé avec différents régimes d'amortissement (pseudo-périodique, critique, apériodique)
2. **q02.py** - Pendule avec force d'excitation : trajectoires dans l'espace des phases
3. **q03.py** - Pendule non-linéaire : étude du comportement chaotique pour différentes amplitudes Fe
4. **q04.py** - Sensibilité aux conditions initiales et calcul de l'exposant de Lyapunov
5. **q05.py** - Diagramme de bifurcation (pour aller plus loin)

## 📊 Génération du rapport

Le compte rendu est dans `rapport/compte_rendu.tex`.

⚠️ **Important** : Utilisez l'option `-shell-escape` pour que le code s'affiche correctement avec le package `minted`.

### Compilation automatique

```bash
cd TP2/rapport
./compile.sh
```

### Compilation manuelle

```bash
cd TP2/rapport
pdflatex -shell-escape compte_rendu.tex
pdflatex -shell-escape compte_rendu.tex  # 2× pour la table des matières
```

Ou avec latexmk :

```bash
cd TP2/rapport
latexmk -pdf -shell-escape compte_rendu.tex
```

### Dépendances LaTeX

Le package `minted` nécessite Pygments :

```bash
pip install Pygments
```

## 🔬 Contenu scientifique

### Question 1 : Régimes d'amortissement

Résolution de l'équation linéarisée avec RK4 :
$$\frac{d^2\theta}{dt^2} + q\frac{d\theta}{dt} + \Omega^2\theta = 0$$

Pour q = 1, 2, 5 s⁻¹ (régimes pseudo-périodique, critique, apériodique).

### Question 2 : Force d'excitation

Ajout d'une force excitatrice :
$$\frac{d^2\theta}{dt^2} + q\frac{d\theta}{dt} + \Omega^2\theta = F_e\sin(\Omega_e t)$$

Analyse dans l'espace des phases (θ, dθ/dt).

### Question 3 : Pendule non-linéaire

Équation complète sans approximation :
$$\frac{d^2\theta}{dt^2} + q\frac{d\theta}{dt} + \Omega^2\sin\theta = F_e\sin(\Omega_e t)$$

Étude du comportement chaotique pour Fe = 1.4, 1.44, 1.465, 1.5 rad/s².

### Question 4 : Exposant de Lyapunov

Mesure de la sensibilité aux conditions initiales en comparant deux trajectoires avec θ(0) = 10° et θ(0) = 9.999°.

Calcul de l'exposant de Lyapunov λ par ajustement linéaire de ln(|Δθ|).

### Question 5 : Diagramme de bifurcation

Observation stroboscopique du système à des instants tn = 2πn/Ωe pour mettre en évidence la route vers le chaos.

## 📦 Dépendances Python

```bash
pip install numpy matplotlib
```

Pour de meilleures performances (optionnel) :

```bash
pip install numba
```

## 💡 Conseils d'utilisation

- **Question 5** : Le calcul du diagramme de bifurcation peut prendre plusieurs minutes (normal).
- **Figures** : Les graphiques sont automatiquement sauvegardés dans `figures/` au format PDF.
- **Paramètres** : Vous pouvez modifier les paramètres physiques directement dans les fichiers Python.

## 🎯 Concepts physiques abordés

- Équations différentielles non-linéaires
- Régimes d'amortissement
- Espace des phases
- Chaos déterministe
- Sensibilité aux conditions initiales
- Exposant de Lyapunov
- Diagramme de bifurcation
- Route vers le chaos

## 📚 Références

- Edward Lorenz (1963) - Deterministic Nonperiodic Flow
- Robert May (1976) - Simple mathematical models with very complicated dynamics
- Feigenbaum (1978) - Quantitative universality for a class of nonlinear transformations

## 🐛 Dépannage

### Erreur d'import de rk4

Assurez-vous d'exécuter les scripts depuis le dossier `python/` ou utilisez `run_all.py`.

### Graphiques ne s'affichent pas

Vérifiez que matplotlib est installé et configuré correctement.

### LaTeX : erreur avec minted

Installez Pygments et utilisez l'option `-shell-escape`.

## 👥 Auteurs

TP réalisé dans le cadre de l'UE LU3PY126 - Physique numérique  
Sorbonne Université - L3 Physique

## 📄 Licence

Code pédagogique à usage académique.
