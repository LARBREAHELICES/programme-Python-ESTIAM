# Python – Structures, Fonctions et Classes 

## Objectifs pédagogiques

1. Produire un guide d'installation et d'environnement (Python, venv, FastAPI, Uvicorn avec la virtualisation Python ).

2. Organisation du cours sur deux jours.

Jour 1, 2

* Comprendre et manipuler les structures de données avancées en Python ( pas trop long ce sont théoriquement des rappels)
* Maîtriser les fonctions, leur portée et les expressions lambda.
* Concevoir des classes simples et comprendre les principes de la programmation orientée objet

- Jour 3 Fast API - Introduction

* Mettre en pratique ces notions dans un mini projet concret (TP FastAPI)

---

## **Sommaire – Formation Python : Structures, Fonctions et Classes (2 jours)**

### **Jour 1 – Manipulation de données et logique algorithmique**

### 1. Introduction à Python et à la logique algorithmique

1.1. Objectifs du module
1.2. Concepts fondamentaux : types, variables, expressions
1.3. Structure d'un script Python
1.4. Règles de style et bonnes pratiques de code

### 2. Les fichiers

2.1. Lecture et écriture de fichiers
2.2. Formats courants (texte, CSV, JSON)
2.3. Manipulation de fichiers avec `pathlib`, `os`, `csv`, `json`
2.4. Exercices : analyse et transformation de données stockées dans des fichiers

### 3. Les tuples et l'unpacking

3.1. Définition et propriétés des tuples
3.2. Affectation multiple et itération parallèle
3.3. Retour multiple de fonctions
3.4. Exercices : traitement de données avec tuples et unpacking

### 4. Les dictionnaires et tables de hash

4.1. Dictionnaires : définition, syntaxe, opérations
4.2. Clés immuables et gestion des collisions
4.3. Dictionnaires imbriqués et compréhension de dictionnaires
4.4. Exercices : fusion et agrégation de données par clé

### 5. Les ensembles (sets)

5.1. Notion d'unicité et d'opérations ensemblistes
5.2. Utilisation algorithmique des ensembles
5.3. Exercices : détection de doublons et filtrage de données

### 6. Les exceptions et la gestion d'erreurs

6.1. Structure `try / except / else / finally`
6.2. Exceptions standards et personnalisées
6.3. Stratégies de gestion d'erreurs dans les scripts
6.4. Exercices : sécurisation des traitements de fichiers

### 7. Les références partagées et la gestion mémoire

7.1. Références et alias
7.2. Différence entre `is` et `==`
7.3. Copie superficielle et profonde (`copy`, `deepcopy`)
7.4. Exercices : gestion des effets de bord dans des structures complexes

---

## **Jour 2 – Fonctions, portée et programmation orientée objet**

### 8. Les fonctions et la portée des variables

8.1. Définition et appel de fonctions
8.2. Passage d'arguments, valeurs par défaut
8.3. Règle LEGB (Local, Enclosing, Global, Builtin)
8.4. Variables globales et `nonlocal`
8.5. Documentation et typage des fonctions (`type hints`, docstrings)
8.6. Exercices : fonctions analytiques et validation de paramètres

### 9. Fonctions anonymes et programmation fonctionnelle (introduction)

9.1. Fonctions lambda
9.2. Fonctions d'ordre supérieur : `map`, `filter`, `reduce`
9.3. Compréhensions de listes, sets et dictionnaires
9.4. Générateurs et expressions génératrices (`yield`)
9.5. Exercices : transformation et agrégation fonctionnelle de données

### 10. Modules et espaces de nommage

10.1. Organisation du code en modules et packages
10.2. Importation (`import`, `from … import …`, `as`)
10.3. Construction d'un module réutilisable (`utils.py`)
10.4. Exercices : refactorisation du code en modules

### 11. Introduction aux classes

11.1. Concepts : classes, instances, attributs, méthodes
11.2. Constructeur `__init__`, méthodes spéciales (`__str__`, `__repr__`)
11.3. Encapsulation, propriétés et getters/setters
11.4. Exercices : classe `DataSet` et manipulation de données

### 12. Héritage et polymorphisme

12.1. Héritage simple et redéfinition de méthodes
12.2. Polymorphisme et typage dynamique
12.3. Énumérations (`Enum`) et typage de classes
12.4. Exercices : classes `Shape`, `Rectangle`, `Circle` ( par exemple )

### 13. Travaux pratiques finaux – Mini API d'analyse

13.1. Présentation de FastAPI
13.2. Structure d'un projet FastAPI
13.3. Création des endpoints d'analyse de données
13.4. Validation des entrées avec Pydantic
13.5. Test des routes via `requests` ou Swagger
13.6. Évaluation du projet : robustesse, modularité, documentation

---


# Jour 1 – Structures de données et logique algorithmique

## Objectifs

Savoir manipuler les fichiers, tuples, dictionnaires, ensembles et exceptions. Comprendre les implications mémoire (références partagées) et préparer la base des traitements de données.

---

## Séquence 1. Les fichiers

**Contenu théorique :**

* Ouvrir et fermer un fichier : `open`, `with`, modes (`'r'`, `'w'`, `'a'`, `'b'`)
* Lire un fichier texte (`read`, `readlines`, itération ligne à ligne)
* Écrire dans un fichier
* Notions sur les formats courants : texte, CSV, JSON
* Utilitaires : `os`, `pathlib`, `csv`, `json`

**Exercice :**

* Lire un fichier CSV de ventes et calculer le total des ventes par produit.
* Sauvegarder le résultat dans un fichier JSON.

---

## Séquence 2. Les tuples et l'unpacking

**Contenu :**

* Création de tuples, immuabilité
* Affectation multiple : `a, b = 1, 2`
* Boucles avec unpacking : `for nom, valeur in liste_de_tuples`
* Fonctions retournant plusieurs valeurs

**Exercice :**

* Écrire une fonction `min_max(liste)` qui retourne un tuple `(min, max)`
* Utiliser l'unpacking pour afficher ces deux valeurs.

---

## Séquence 3. Dictionnaires (tables de hash)

**Contenu :**

* Définition, ajout, suppression, accès aux clés
* Clés immuables, itération avec `.items()`
* Fusion de dictionnaires (`|` ou `update`)
* Dictionnaires imbriqués
* Utilisation comme enregistrements

**Exercice :**

* Fusionner deux fichiers CSV en un dictionnaire unique indexé par une clé commune (ex. identifiant client).
* Sauvegarder le résultat en JSON.

---

## Séquence 4. Ensembles (sets)

**Contenu :**

* Création, opérations d'union, intersection, différence
* Vérification d'appartenance (`in`)
* Cas d'usage : détection de doublons, suppression de valeurs répétées

**Exercice :**

* À partir d'une liste de valeurs contenant des doublons, créer un ensemble pour obtenir la liste des valeurs uniques.
* Comparer les performances avec une boucle classique.

---

## Séquence 5. Exceptions et gestion d'erreurs

**Contenu :**

* Syntaxe `try / except / else / finally`
* Lever une exception (`raise`)
* Création d'exceptions personnalisées
* Bonnes pratiques : validation des entrées utilisateur

**Exercice :**

* Écrire une fonction `safe_div(a, b)` qui retourne la division et gère la division par zéro avec une exception personnalisée.
* Utiliser `try / finally` pour consigner les erreurs dans un fichier log.

---

## Séquence 6. Références partagées et copies

**Contenu :**

* Compréhension des références en Python
* Différence entre `is` et `==`
* Copies : `copy.copy` et `copy.deepcopy`
* Effets de bord, alias de liste, références circulaires
* L'instruction `del`

**Exercice :**

* Montrer la différence entre deux listes liées par référence et deux listes indépendantes.
* Expérimenter l'effet de `copy()` et `deepcopy()` sur des structures imbriquées.

---

# Jour 2 – Fonctions, portée et programmation orientée objet

## Objectifs

Approfondir la logique fonctionnelle, comprendre la portée des variables, utiliser les lambda et comprehensions, puis aborder les classes et leur utilisation algorithmique. Application finale : création d'une mini API avec FastAPI.

---

## Séquence 1. Fonctions et portée des variables

**Contenu :**

* Définir une fonction avec `def`
* Passage d'arguments, valeurs par défaut
* Règle LEGB (Local, Enclosing, Global, Builtin)
* Variables globales et `nonlocal`
* Docstrings et `type hints` (`def f(a: int) -> int:`)

**Exercice :**

* Écrire une fonction `analyse(liste)` qui retourne la moyenne, la médiane et la variance d'une liste numérique.
* Utiliser des annotations de type et une docstring complète.

---

## Séquence 2. Fonctions lambda, map, filter et comprehensions

**Contenu :**

* Fonctions anonymes : `lambda x: x * 2`
* Fonctions d'ordre supérieur : `map`, `filter`, `reduce`
* Compréhensions de listes, sets et dictionnaires
* Expressions génératrices et `yield`

**Exercice :**

* Reprendre une liste de ventes et produire :

  * Une liste des ventes supérieures à une valeur donnée (filter)
  * Une liste des montants avec taxe ajoutée (map)
  * Une somme totale avec `reduce`
* Transformer la solution finale en une compréhension de liste.

---

## Séquence 3. Modules et espaces de nommage

**Contenu :**

* Création et importation de modules (`import`, `from … import …`)
* Espaces de nommage et packages
* Organisation du code en plusieurs fichiers

**Exercice :**

* Réorganiser les fonctions des exercices précédents dans un module `utils.py`
* Tester l'import et l'appel depuis un autre script.

---

## Séquence 4. Introduction aux classes

**Contenu :**

* Définition de classe, constructeur `__init__`
* Attributs d'instance et de classe
* Méthodes spéciales : `__str__`, `__repr__`, `__eq__`
* Notion de `property` et encapsulation

**Exercice :**

* Créer une classe `DataSet` capable de :

  * Charger un fichier CSV
  * Calculer des statistiques de base (moyenne, variance)
  * Fournir une représentation lisible avec `__str__`

---

## Séquence 5. Héritage et typage

**Contenu :**

* Héritage simple, polymorphisme
* Redéfinition de méthodes
* Typage et classes génériques (`Generic`, `TypeVar`)
* Exemple d'enumérations

**Exercice :**

* Créer une classe `Shape` et deux sous-classes `Rectangle` et `Circle`
* Implémenter `area()` et `perimeter()` selon le type de figure.
* Démontrer le polymorphisme via une liste d'objets de formes différentes.

---

## Séquence 6. Travaux pratiques finaux – Mini API d'analyse

**Objectif :**
Publier sous forme d'API REST les fonctions et classes conçues dans le cours.

**Étapes :**

1. Installer et configurer FastAPI et Uvicorn.
2. Créer un projet `tp_fastapi` contenant :

   * `main.py` (point d'entrée de l'API)
   * `models.py` (classes `DataSet`, `Shape`)
   * `utils.py` (fonctions analytiques)
3. Définir des endpoints :

   * `/analys` : calcule moyenne et variance à partir d'une liste passée en JSON
   * `/shapes/area` : calcule l'aire d'une figure donnée
4. Tester les routes avec `curl` ou `requests`.

**Critères d'évaluation :**

* Code structuré et commenté
* Gestion correcte des erreurs d'entrée
* Documentation automatique Swagger opérationnelle

---

# Évaluation et prolongements

Évaluation dans la partie Fast API.

Elle se fera avec le mini-projet Fast API, voir la suite du programme du cours : [Fast API](./Part2_FastAPI.md)