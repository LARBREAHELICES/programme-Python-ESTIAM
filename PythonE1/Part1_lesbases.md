# **Plan de formation – Apprentissage de Python (niveau débutant – première année)**

Organisation du cours 

supports/  <--  slides
exercices/ <-- exercices corrigés
tp/ <-- sujet du tp 

---

## **Objectifs généraux**

* Comprendre la logique algorithmique et les bases de la programmation.
* Maîtriser les structures fondamentales du langage Python.
* Être capable d'écrire, organiser et tester des programmes simples.
* Découvrir la notion d'objet, de module et de manipulation de données.

---

## **Introduction et premiers pas**

**Objectifs :**
Installer Python, comprendre ce qu'est un langage interprété et exécuter ses premiers scripts.

### Contenu :

1. Présentation de Python et de ses usages.
2. Installation et configuration de l'environnement :

   * Python, VS Code, terminal
   * création d'un environnement virtuel (`venv`)
3. Premier script :

   * `print()`, commentaires, indentation
4. Variables, types de base (`int`, `float`, `str`, `bool`)
5. Entrée utilisateur : `input()`
6. Conversion de types (`int()`, `float()`, `str()`)

**Exercices :**

* Calculer la somme et la moyenne de deux nombres saisis.
* Créer un petit script interactif "Bonjour [nom] !".

---

## **Opérations et conditions**

**Objectifs :**
Découvrir la logique des décisions et les expressions booléennes.

### Contenu :

1. Opérateurs arithmétiques et logiques
2. Conditions : `if`, `elif`, `else`
3. Opérateurs de comparaison (`==`, `<`, `>`, `!=`)
4. Expressions booléennes composées (`and`, `or`, `not`)
5. Syntaxe compacte : expressions conditionnelles (`x if cond else y`)

**Exercices :**

* Vérifier la parité d'un nombre.
* Simuler un mini système de notes ("admis / ajourné").
* Calculer le plus grand de trois nombres saisis par l'utilisateur.

---

## **Boucles et itérations**

**Objectifs :**
Comprendre la répétition d'instructions et les itérations sur des séquences.

### Contenu :

1. Boucle `while` : conditions d'arrêt, compteurs
2. Boucle `for` et fonction `range()`
3. Instructions `break` et `continue`
4. Notion d'itérable et de séquence
5. Applications : calculs répétitifs, tables de multiplication

**Exercices :**

* Afficher les dix premiers nombres pairs.
* Compter le nombre de voyelles dans une phrase.
* Calculer le PGCD de deux nombres (algorithme d'Euclide).

---

## **Les structures de données**

**Objectifs :**
Découvrir les conteneurs Python et savoir les manipuler.

### Contenu :

1. Listes (`list`) : création, ajout, suppression, tranches (`slicing`)
2. Tuples (`tuple`) : immuabilité et usage
3. Dictionnaires (`dict`) : clé/valeur, itération sur `.items()`
4. Ensembles (`set`) : unicité, opérations d'union/intersection
5. Compréhensions de listes et dictionnaires

**Exercices :**

* Calculer la moyenne d'une liste de notes.
* Créer un dictionnaire associant un prénom à une note.
* Supprimer les doublons dans une liste à l'aide d'un `set`.

---

## **Fonctions**

**Objectifs :**
Modulariser le code et comprendre la portée des variables.

### Contenu :

1. Définition de fonction avec `def`
2. Arguments, valeurs par défaut, retour de valeurs
3. Passage par référence / par valeur
4. Variables locales et globales
5. Documentation (`docstring`) et typage (`type hints`)
6. Fonctions anonymes (`lambda`)

**Exercices :**

* Écrire une fonction qui calcule le factoriel d'un nombre.
* Créer une fonction de conversion Celsius ↔ Fahrenheit.
* Écrire une fonction `analys(dataset)` retournant moyenne et variance.
* Jeu de chiffoumi

---

## **Fichiers et exceptions**

**Objectifs :**
Lire et écrire des fichiers, gérer les erreurs d'exécution.

### Contenu :

1. Lecture et écriture de fichiers texte (`open`, `with`)
2. Formats CSV et JSON

**Exercices :**

* Charger un fichier CSV et afficher son contenu.
* Créer une fonction qui enregistre des résultats dans un fichier texte.
* Écrire une fonction de lecture sécurisée avec gestion d'erreur.

---

## **Introduction à la programmation orientée objet**

**Objectifs :**
Découvrir la logique objet et la création de classes.

### Contenu :

1. Définition d'une classe, constructeur `__init__`
2. Attributs d'instance et de classe
3. Méthodes et `self`

**Exercices :**

* Créer une classe Car avec les attributs brand, model et year.
Ajouter une méthode display_info() qui affiche les informations du véhicule dans la console.

* Créer une classe Student avec les attributs name, age et grade.
Ajouter une méthode is_passed() qui affiche "Passed" si la note est supérieure ou égale à 10, sinon "Failed”.

* Créer une classe Rectangle avec les attributs width et height.
Ajouter une méthode area() qui retourne l’aire du rectangle, et une méthode perimeter() qui retourne son périmètre.

* Créer une classe BankAccount avec les attributs owner et balance (initialisé à 0).
Ajouter les méthodes deposit(amount) et withdraw(amount) pour gérer le solde, avec vérification que le retrait ne rend pas le solde négatif.

---

## **Modules, packages**

**Objectifs :**
Organiser un projet et créer un programme complet.

### Contenu :

1. Modules et importation (`import`, `from … import …`)
2. Espaces de nommage et `__main__`
3. Organisation du code en plusieurs fichiers
4. Gestion des dépendances avec `requirements.txt`

**Mini-projet :**

* Créer une petite application console :

  * Exercice 1 : gestion de notes d'étudiants (ajout, recherche, moyenne)
  * Exercice 2 : simulateur de calcul statistique simple, lancer d'un dé non pipé.

---
