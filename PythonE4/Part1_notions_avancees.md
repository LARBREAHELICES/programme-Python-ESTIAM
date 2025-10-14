# **Plan – Python : Structures, Fonctions, Classes et Tests**

## Plan

## **Rappels fondamentaux sur Python (niveau avancé)**
### **1. Modèle d'exécution et typage**
### **2. Références, copies et gestion mémoire**
### **3. Structures de données complexes**
## **Exceptions, documentation et fonctions avancées**
### **4. Gestion des exceptions et robustesse du code**
### **5. Documentation et docstrings**
### **6. Fonctions avancées et programmation fonctionnelle**
## **Classes, polymorphisme et tests**
### **7. Introduction aux classes et objets**
### **8. Héritage et polymorphisme**
### **9. Tests unitaires avec Pytest**


## **Objectifs pédagogiques**

1. Consolider la compréhension du modèle objet de Python et des structures de données complexes.
2. Approfondir la maîtrise des fonctions, des expressions fonctionnelles et de la documentation technique.
3. Concevoir et manipuler des classes en appliquant les principes de la programmation orientée objet.
4. Comprendre le polymorphisme et la modularité du code orienté objet.
5. Écrire des tests unitaires avec `pytest` pour valider le comportement du code.

---

## **Rappels fondamentaux sur Python (niveau avancé)**

### **1. Modèle d'exécution et typage**

1.1. Python comme langage interprété et typé dynamiquement.
1.2. Typage fort vs typage faible.
1.3. Typage par référence et identité des objets (`id()`, `is`, `==`).
1.4. Objets immuables et mutables :

* Immuables : `int`, `float`, `str`, `tuple`
* Mutables : `list`, `dict`, `set`
  1.5. Implications du modèle mémoire sur la modification d'objets.

**Exercices :**

* Montrer la différence entre deux variables pointant vers le même objet mutable.
* Vérifier l'identité et l'égalité de plusieurs objets à l'aide de `is` et `==`.

---

### **2. Références, copies et gestion mémoire**

2.1. Compréhension du mécanisme de référence.
2.2. Copies superficielles et profondes (`copy`, `deepcopy`).
2.3. Gestion du ramasse-miettes (garbage collector).
2.4. Bonnes pratiques pour éviter les effets de bord.

**Exercices :**

* Créer une liste de listes, modifier une sous-liste et observer l'effet sur l'originale.
* Comparer les comportements de `copy()` et `deepcopy()` sur une structure imbriquée.

---

### **3. Structures de données complexes**

3.1. Listes imbriquées, dictionnaires de listes et tuples composites.
3.2. Compréhensions de listes, sets et dictionnaires (syntaxe et efficacité).
3.3. Tri et filtrage avancés (`sorted`, `key`, `lambda`).
3.4. Approche fonctionnelle : `map`, `filter`, `reduce`.

**Exercices :**

* À partir d'un dictionnaire de données, produire une liste triée selon une clé.
* Filtrer et transformer une structure complexe avec des compréhensions.

---

## **Exceptions, documentation et fonctions avancées**

### **4. Gestion des exceptions et robustesse du code**

4.1. Structure `try / except / else / finally`.
4.2. Levée d'exceptions personnalisées avec `raise`.
4.3. Propagation et capture des erreurs.
4.4. Bonnes pratiques : validation des entrées, messages d'erreur explicites.
4.5. Création d'une hiérarchie d'exceptions propres à un module.

**Exercices :**

* Implémenter une fonction `safe_div(a, b)` qui gère la division par zéro avec une exception dédiée.
* Écrire une fonction `read_file(path)` qui gère proprement les erreurs d'ouverture et de lecture.

---

### **5. Documentation et docstrings**

5.1. Rôle et conventions des docstrings (PEP 257).
5.2. Structure d'une docstring complète (paramètres, retours, exceptions).
5.3. Interaction avec `help()` et génération de documentation automatique (`pdoc`, `Sphinx`).
5.4. Typage statique avec `type hints` et vérification via `mypy`.

**Exercice :**

* Documenter une fonction d'analyse statistique `analyse(liste: list[float]) -> dict[str, float]` avec une docstring structurée et des annotations de types.

---

### **6. Fonctions avancées et programmation fonctionnelle**

6.1. Fonctions anonymes (`lambda`).
6.2. Fonctions d'ordre supérieur : `map`, `filter`, `reduce`.
6.3. Fonctions génératrices (`yield`) et expressions génératrices.
6.4. Portée des variables (règle LEGB) et closures.
6.5. Expressions conditionnelles (`x if cond else y`).

**Exercices :**

* Reproduire le comportement d'un filtrage avec une fonction lambda.
* Créer un générateur produisant les puissances successives d'un entier.
* Implémenter une fonction d'ordre supérieur appliquant un traitement à une liste de fonctions.

---

## **Classes, polymorphisme et tests**

### **7. Introduction aux classes et objets**

7.1. Définition d'une classe, constructeur `__init__`.
7.2. Attributs d'instance et de classe.
7.3. Méthodes d'instance et mot-clé `self`.
7.4. Méthodes spéciales (`__str__`, `__repr__`, `__eq__`, `__len__`).
7.5. Encapsulation et accès contrôlé via `@property`.

**Exercices :**

* Créer une classe `BankAccount` avec dépôt, retrait et affichage du solde.
* Ajouter une méthode `__str__()` pour afficher un résumé de l'état du compte.

---

### **8. Héritage et polymorphisme**

8.1. Héritage simple et redéfinition de méthodes.
8.2. Appel de la classe parente avec `super()`.
8.3. Polymorphisme : méthodes partagées entre classes différentes.
8.4. Introduction aux classes abstraites (`abc.ABC`).
8.5. Utilisation de `isinstance()` et `issubclass()`.

**Exercices :**

* Créer une classe `Shape` avec sous-classes `Rectangle` et `Circle`.
* Implémenter `area()` et `perimeter()` dans chaque sous-classe.
* Afficher les résultats via une boucle polymorphique parcourant une liste de formes.

---

### **9. Tests unitaires avec Pytest**

9.1. Principes du test unitaire et de la validation automatique.
9.2. Installation et exécution de `pytest`.
9.3. Structure d'un test (`assert`, nommage `test_*`).
9.4. Tests paramétrés (`@pytest.mark.parametrize`).
9.5. Tests d'exceptions (`pytest.raises`).
9.6. Organisation d'un dossier de tests (`tests/`, `conftest.py`).

**Exemples :**

```python
# math_utils.py
def safe_div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
```

```python
# tests/test_math_utils.py
import pytest
from math_utils import safe_div

def test_safe_div_valid():
    assert safe_div(10, 2) == 5

def test_safe_div_zero():
    with pytest.raises(ZeroDivisionError):
        safe_div(5, 0)
```

**Exercices :**

* Écrire des tests unitaires pour la classe `BankAccount`.
* Vérifier le bon comportement de la méthode `withdraw()` lorsqu'un retrait dépasse le solde.
* Tester la classe `Shape` et vérifier que chaque sous-classe implémente correctement `area()`.
