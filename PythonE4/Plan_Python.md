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

1. Consolider la compréhension du modèle objet de Python et des structures de données.
2. Approfondir la maîtrise des fonctions, des expressions fonctionnelles et de la documentation technique.
3. Concevoir et manipuler des classes en appliquant les principes de la programmation orientée objet.
4. Comprendre le polymorphisme et la modularité du code orienté objet.
5. Écrire des tests unitaires avec `pytest` pour valider le comportement du code.

---

## **Rappels fondamentaux sur Python**

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

--- 

# **8. Héritage et polymorphisme**

Cette section introduit la logique de **réutilisation** et d’**extension** du code avec les classes dérivées.
L’héritage permet de définir une hiérarchie d’objets partageant des comportements communs, tandis que le polymorphisme permet d’utiliser des objets différents de manière interchangeable.

---

### **8.1. Héritage simple et redéfinition de méthodes**

Une classe peut hériter d’une autre pour **réutiliser** ou **modifier** son comportement.

**Exemple :**

```python
class Animal:
    def speak(self):
        return "Un animal fait un son."

class Dog(Animal):
    def speak(self):
        return "Le chien aboie."

class Cat(Animal):
    def speak(self):
        return "Le chat miaule."
```

L’héritage simple permet de redéfinir les méthodes de la classe parente.
On peut alors itérer sur différents objets partageant la même interface :

```python
animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.speak())
```

---

### **8.2. Appel de la classe parente avec `super()`**

La fonction `super()` permet d’appeler la méthode de la classe parente sans la nommer explicitement.
Cela facilite la maintenance et le chaînage dans des hiérarchies complexes.

**Exemple :**

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
```

L’appel à `super()` initialise la partie héritée (`name`) avant d’ajouter les attributs spécifiques (`school`).

---

### **8.3. Polymorphisme**

Le polymorphisme permet d’appeler la même méthode sur des objets de classes différentes, **sans connaître leur type exact**.
Chaque classe définit sa propre implémentation.

**Exemple :**

```python
class Shape:
    def area(self):
        raise NotImplementedError("La méthode area() doit être redéfinie.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        from math import pi
        return pi * self.radius ** 2
```

```python
shapes = [Rectangle(4, 3), Circle(2)]
for shape in shapes:
    print(shape.area())
```

➡️ Le polymorphisme permet ici d’invoquer `area()` sur différents types sans distinction.

---

### **8.4. Classes abstraites avec `abc.ABC`**

Les classes abstraites définissent une **interface commune** que les sous-classes doivent implémenter.
Elles ne peuvent pas être instanciées directement.

**Exemple :**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (self.base * self.height) / 2
```

```python
t = Triangle(10, 5)
print(t.area())
```

➡️ Toute classe dérivant de `Shape` doit implémenter la méthode `area()`, sinon une erreur est levée à l’instanciation.

---

### **8.5. Vérification des relations de classe**

Python offre deux fonctions intégrées pour inspecter les hiérarchies :

```python
isinstance(obj, Class)   # Vérifie si obj est une instance de Class ou de ses sous-classes
issubclass(Sub, Base)    # Vérifie si une classe hérite d'une autre
```

**Exemple :**

```python
print(isinstance(Rectangle(2, 3), Shape))  # True
print(issubclass(Circle, Shape))           # True
```

---

### **Exercices**

1. Créer une classe `Shape` avec sous-classes `Rectangle` et `Circle`.

   * Implémenter `area()` et `perimeter()` dans chaque sous-classe.
   * Créer une boucle polymorphique parcourant une liste de formes et affichant leurs aires et périmètres.

2. Ajouter une classe `Triangle` dérivée de `Shape`, et vérifier que l’héritage est correctement reconnu avec `isinstance()` et `issubclass()`.

3. Rendre `Shape` abstraite en utilisant `abc.ABC` et `@abstractmethod`.
   Vérifier qu’elle ne peut plus être instanciée directement.

---

# **9. Tests unitaires avec Pytest**

Les tests unitaires permettent de **valider automatiquement le comportement du code**.
`pytest` est l’outil standard de test en Python, apprécié pour sa simplicité et sa puissance.

---

### **9.1. Principes du test unitaire**

Un test unitaire vérifie le comportement **d’une fonction ou classe isolée**.
Chaque test doit être :

* **indépendant**,
* **répétable**,
* **automatisable**.

L’objectif : détecter rapidement les régressions lors de modifications du code.

---

### **9.2. Installation et exécution**

Installation :

```bash
pip install pytest
```

Exécution :

```bash
pytest
```

`pytest` recherche automatiquement les fichiers et fonctions dont le nom commence par `test_`.

---

### **9.3. Structure d’un test**

Un test est une simple fonction utilisant des **assertions**.

**Exemple :**

```python
# fichier test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

Exécution :

```bash
pytest -v
```

Le drapeau `-v` affiche le détail des tests exécutés.

---

### **9.4. Tests paramétrés**

Les tests peuvent être exécutés avec plusieurs jeux de valeurs grâce à `@pytest.mark.parametrize`.

```python
import pytest

@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add(a, b, result):
    assert add(a, b) == result
```

---

### **9.5. Tests d’exceptions**

Vérifie qu’une erreur spécifique est bien levée dans un contexte donné.

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Division par zéro.")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

---

### **9.6. Organisation du dossier de tests**

Structure standard d’un projet Python avec `pytest` :

```
project/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── conftest.py
```

* `tests/` contient tous les tests unitaires.
* `conftest.py` permet de définir des **fixtures** (valeurs ou objets réutilisables dans plusieurs tests).

**Exemple de fixture :**

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_sum(sample_data):
    assert sum(sample_data) == 6
```

---

### **Exercices**

1. Écrire des tests unitaires pour les classes `Rectangle` et `Circle` :

   * Vérifier la validité des aires et périmètres.
   * Ajouter un test de type : `isinstance(obj, Shape)`.

2. Créer un test paramétré pour valider le calcul de l’aire avec plusieurs dimensions.

3. Écrire un test vérifiant qu’une erreur est levée pour un rayon négatif dans `Circle`.

4. Organiser les tests dans un dossier `tests/` et exécuter `pytest -v`.
