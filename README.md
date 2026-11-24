# Projet 1 — Analyse numérique en Python

## Objectif
Comparer quatre méthodes de résolution de `f(x)=0` : dichotomie, fausse position,
Newton-Raphson et point fixe.

## Exécution
Python 3.9+ :
```bash
python numerical_methods.py
python -m unittest -v
```
Graphique facultatif :
```bash
python -m pip install matplotlib
python numerical_methods.py
```

L'exemple résout `x^3 - x - 2 = 0` sur `[1,2]`. La racine est proche de
`1.5213797068`.

## Notions théoriques abordées
Hypothèses de la dichotomie/fausse position, critère d'arrêt, convergence locale
de Newton, condition de contraction pour le point fixe, distinction entre
résidu `|f(x_n)|` et erreur sur la racine.

## Limites
Un critère d'arrêt numérique n'est pas une preuve de convergence. Les méthodes
peuvent échouer si leurs hypothèses ne sont pas satisfaites.
