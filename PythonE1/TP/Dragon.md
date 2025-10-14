# **TP d'évaluation – Jeu : Dragon vs Chevalier**

## **Objectif du TP**

Concevoir un petit **jeu tour par tour** en console où un **Chevalier** affronte un **Dragon**.
Le joueur incarne le chevalier et choisit ses actions à chaque tour. Le dragon, lui, attaque automatiquement.
Le jeu se poursuit jusqu'à la victoire ou la défaite.

---

## **Compétences évaluées**

* Utiliser les **structures de contrôle** (`if`, `while`, `for`)
* Créer et manipuler des **fonctions**
* Concevoir et instancier des **classes**
* Gérer des **valeurs aléatoires** avec le module `random`
* Écrire un **programme complet et structuré**

---

## **Structure conseillée du programme**

```
dragon_vs_knight/
│
├── main.py         # programme principal du jeu
├── models.py       # classes du jeu (Character, Knight, Dragon)
└── utils.py        # fonctions de calcul des dégâts et d'affichage
```

*(Pour le TP d'évaluation, tout le code peut être regroupé dans un seul fichier `main.py` si besoin.)*


---

## **Prolongements possibles (bonus)**

* Ajouter une **attaque spéciale** disponible tous les 3 tours.
* Introduire un **niveau de difficulté** (facile, normal, difficile).
* Sauvegarder les résultats du combat dans un **fichier texte**.
* Créer une **interface graphique** simple avec `tkinter` ou `pygame`.

---

## **Barème d'évaluation (sur 20 points)**

| Critère                                                  | Points |
| -------------------------------------------------------- | ------ |
| Organisation du code et clarté                           | 4      |
| Bonne utilisation des classes et héritage                | 4      |
| Logique de jeu fonctionnelle (boucle, tours, conditions) | 6      |
| Gestion d'entrées utilisateur et erreurs                 | 2      |
| Cohérence des affichages console                         | 2      |
| Bonus (créativité, extensions, propreté du code)         | +2     |


--- 
