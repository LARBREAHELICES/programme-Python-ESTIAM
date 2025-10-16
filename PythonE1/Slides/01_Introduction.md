---
marp: true
theme: default
paginate: true
class: lead
---


# **Python – Concepts intermédiaires**

---

## **Chapitre 1 – Rappel sur la portée des variables : la règle LEGB**

### **1.1. Définition**

En Python, lorsqu'un nom (variable, fonction, etc.) est utilisé, l'interpréteur le cherche selon la règle **LEGB** :

* **L – Local** : dans la fonction courante.
* **E – Enclosing** : dans les fonctions englobantes (fonctions imbriquées).
* **G – Global** : dans le module principal.
* **B – Built-in** : dans les fonctions et noms prédéfinis de Python (`len`, `print`, etc.).

Cette hiérarchie permet à Python de savoir quelle variable utiliser à un instant donné.

---

### **1.2. Exemple simple**

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Dans inner :", x)
    inner()

outer()
print("Dans le module :", x)
```

---

**Résultat :**

```
Dans inner : local
Dans le module : global
```

Python cherche `x` d'abord dans la portée locale (`inner`), puis dans `outer`, ensuite dans la portée globale.

---

### **1.3. Exercices**

1. Écrire une fonction increment(count) qui retourne count + 1.
Initialiser une variable count = 0, puis appeler la fonction plusieurs fois dans une boucle pour icnrémenter count.

2. Créer une fonction `make_counter()` qui incrémente une valeur de +1.
Utilisez une liste (ou un dictionnaire) pour stocker l'état de cette valeur.
Vous pouvez également initialiser cette liste en la passant en paramètre à la fonction.
Rappelez-vous qu'une liste est un objet mutable, c'est-à-dire qu'elle conserve l'état de ses valeurs en mémoire entre plusieurs appels.

---

## **Chapitre 2 – Introduction aux types primitifs et aux objets**

### **2.1. Typage dynamique**

Python est **dynamiquement typé** :
le type d'une variable est défini à l'exécution, pas à la déclaration.

```python
x = 10       # entier (int)
x = "texte"  # devient une chaîne (str)
```

---

### **2.2. Types primitifs**

Les **types primitifs** sont les plus simples, directement gérés par l'interpréteur.

| Type    | Exemple         | Description           |
| ------- | --------------- | --------------------- |
| `int`   | `x = 5`         | Entiers               |
| `float` | `x = 3.14`      | Nombres décimaux      |
| `bool`  | `x = True`      | Booléens              |
| `str`   | `x = "Bonjour"` | Chaînes de caractères |

Ces objets sont **immuables** : leur valeur ne peut pas être modifiée en place.

---

Exemple :

```python
x = 5
print(id(x))
x += 1
print(id(x))  # nouvelle adresse mémoire
```

---

### **2.3. Types objets (collections)**

Python propose aussi des types **complexes et mutables**, appelés objets de collection.

| Type    | Exemple            | Mutabilité | Description             |
| ------- | ------------------ | ---------- | ----------------------- |
| `list`  | `[1, 2, 3]`        | Mutable    | Liste ordonnée          |
| `tuple` | `(1, 2, 3)`        | Immuable   | Liste non modifiable    |
| `dict`  | `{"a": 1, "b": 2}` | Mutable    | Dictionnaire clé-valeur |
| `set`   | `{1, 2, 3}`        | Mutable    | Ensemble sans doublons  |

---

### **2.4. Exemple de manipulation d'objets**

```python
person = {"name": "Alice", "age": 20}
person["age"] += 1
print(person)  # {'name': 'Alice', 'age': 21}
```

```python
fruits = ["pomme", "poire"]
fruits.append("banane")
print(fruits)  # ['pomme', 'poire', 'banane']
```

---

### **2.5. Typage fort et conversion**

Python ne convertit pas automatiquement les types :

```python
x = "5"
y = 2
# print(x + y)  # Erreur
print(int(x) + y)  # 7
```

---

### **Exercices**

1. Créer une liste de nombres, calculer leur moyenne à l'aide de `sum()` et `len()`.
2. Transformer un dictionnaire `{nom: age}` en ajoutant +1 à chaque âge.
3. Expliquer ce qui se passe en mémoire quand on écrit `x += 1` pour un entier.
4. Comparer le comportement de += sur un entier et sur une liste.
Observer ce qui change en mémoire avant et après l'opération.

---

## **Chapitre 3 – Les compréhensions de liste**

### **3.1. Définition**

Une **compréhension de liste** permet de créer une nouvelle liste à partir d'une séquence existante, en une seule ligne.

Forme générale :

```python
[expression for element in iterable if condition]
```

---

### **3.2. Exemple simple**

```python
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]
```

Équivalent à :

```python
squares = []
for n in numbers:
    squares.append(n**2)
```

---

### **3.3. Avec condition**

```python
even = [n for n in range(10) if n % 2 == 0]
print(even)  # [0, 2, 4, 6, 8]
```

---

### **3.4. Compréhensions imbriquées**

```python
pairs = [(x, y) for x in range(2) for y in range(3)]
print(pairs)  # [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)]
```

---

### **3.5. Transformation d'objets**

```python
names = ["Alice", "Bob", "Charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']
```

---

### **3.6. Application pratique**

Filtrage et transformation d'un dictionnaire :

```python
students = {"Alice": 15, "Bob": 8, "Charlie": 12}
passed = [name for name, grade in students.items() if grade >= 10]
print(passed)  # ['Alice', 'Charlie']
```

---

### **Exercices**

1. Créer une liste contenant les carrés des nombres pairs de 0 à 20.
2. Transformer une liste de chaînes en leur longueur (`["chat", "chien"] → [4, 5]`).
3. Créer une liste des voyelles présentes dans une phrase sans doublons.
4. À partir d'un dictionnaire `{nom: note}`, générer une liste des élèves admis (note >= 10).

```python
students = {
    "Alice": 15,
    "Bob": 9,
    "Charlie": 12,
    "Diana": 18,
    "Ethan": 7
}
```

--- 

## **Chapitre 4 – Le slicing (découpage de séquences)**

### **4.1. Définition**

Le **slicing** (ou découpage) est une manière compacte d'accéder à une **portion** d'une séquence en Python.
Il fonctionne sur tous les objets **indexables et itérables** : `list`, `tuple`, `str`, etc.

Syntaxe générale :

```python
sequence[start:stop:step]
```

* `start` : position de départ (incluse)
* `stop` : position de fin (exclue)
* `step` : pas (incrément, facultatif)

---

### **4.2. Exemples de base**

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])   # [2, 3, 4]
print(numbers[:4])    # [0, 1, 2, 3]
print(numbers[6:])    # [6, 7, 8, 9]
print(numbers[::2])   # [0, 2, 4, 6, 8]
```

---

### **4.3. Slicing négatif**

Python autorise des **indices négatifs** : `-1` correspond au dernier élément, `-2` à l'avant-dernier, etc.

```python
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[-3:])     # ['c', 'd', 'e']
print(letters[:-2])     # ['a', 'b', 'c']
print(letters[::-1])    # ['e', 'd', 'c', 'b', 'a'] (inversion)
```

---

### **4.4. Slicing sur les chaînes**

Les chaînes (`str`) se comportent comme des séquences de caractères.

```python
word = "Python"
print(word[0:3])    # 'Pyt'
print(word[-3:])    # 'hon'
print(word[::-1])   # 'nohtyP'
```

---

### **4.5. Slicing sur les tuples**

Le slicing s'applique aussi sur les tuples, mais comme ils sont immuables, le résultat est toujours **un nouveau tuple**.

```python
values = (10, 20, 30, 40, 50)
print(values[1:4])  # (20, 30, 40)
```

---

### **4.6. Modification partielle d'une liste**

Contrairement aux chaînes ou tuples, les **listes sont mutables** :
on peut remplacer une portion par une autre.

```python
numbers = [0, 1, 2, 3, 4, 5]
numbers[2:4] = [20, 30]
print(numbers)  # [0, 1, 20, 30, 4, 5]
```

On peut même **supprimer** des éléments par slicing :

```python
numbers[1:3] = []
print(numbers)  # [0, 30, 4, 5]
```

---

### **4.7. Copie rapide d'une liste**

Une copie complète d'une séquence peut se faire via `[:]` :

```python
a = [1, 2, 3]
b = a[:]         # nouvelle liste
b.append(4)
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]
```

Cela crée une **copie superficielle**, si vous avez des références dans des références, cela ne copiera pas les références imbriquées.

---

### **4.8. Slicing et compréhension**

On peut combiner slicing et compréhension pour manipuler facilement des sous-listes.

```python
numbers = list(range(10))
even_squares = [x**2 for x in numbers[::2]]
print(even_squares)  # [0, 4, 16, 36, 64]
```

---

### **Exercices**

1. À partir d'une liste de 10 éléments, afficher :

   * les 3 premiers éléments,
   * les 3 derniers,
   * un élément sur deux.

---

```python
students = [
    ("Alice", 15),
    ("Bob", 9),
    ("Charlie", 12),
    ("Diana", 18),
    ("Ethan", 7),
    ("Fiona", 14),
    ("Gabriel", 11),
    ("Hugo", 8),
    ("Inès", 16),
    ("Jules", 10)
]
```

---

2. Inverser une chaîne de caractères en une ligne grâce au slicing.
3. Extraire le mot `"Python"` de la chaîne `"Je code en Python tous les jours"`.
4. Supprimer les éléments d'indice pair d'une liste donnée.
5. Créer une copie d'une liste, modifier la copie, et vérifier que l'originale n'est pas affectée.

---

# **Chapitre 5 – Fonctions lambda et application aux compréhensions**

---

### **5.1. Qu'est-ce qu'une fonction lambda ?**

Une **lambda** est une fonction **anonyme** (sans nom explicite), utile pour écrire des opérations simples et courtes.

Syntaxe :

```python
lambda arguments: expression
```

Elle retourne **automatiquement** le résultat de l'expression (pas besoin de `return`).

**Exemple :**

```python
add = lambda a, b: a + b
print(add(2, 3))  # 5
```

---

### **5.2. Lambdas et fonctions d'ordre supérieur**

Les lambdas sont souvent utilisées avec des fonctions comme :

* `map()` pour transformer des éléments,
* `filter()` pour en filtrer certains,
* `sorted()` pour trier selon un critère.

---

**Exemples :**

```python
numbers = [1, 2, 3, 4, 5]

# Doubler chaque élément
doubles = list(map(lambda x: x * 2, numbers))
print(doubles)  # [2, 4, 6, 8, 10]

# Garder uniquement les pairs
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
```

---

### **5.3. Lambdas dans les compréhensions**

On peut utiliser une lambda **à l'intérieur d'une compréhension de liste** pour appliquer un traitement léger à chaque élément.

**Exemple :**

```python
names = ["alice", "bob", "charlie"]
upper_names = [(lambda n: n.capitalize())(name) for name in names]
print(upper_names)  # ['Alice', 'Bob', 'Charlie']
```

---

Autre exemple plus calculatoire :

```python
numbers = range(6)
squares_even = [(lambda x: x**2)(n) for n in numbers if n % 2 == 0]
print(squares_even)  # [0, 4, 16, 36]
```

---

### **5.4. Comparaison avec une fonction classique**

Les lambdas sont utiles pour les **fonctions temporaires**, mais il est préférable d'utiliser une fonction classique (`def`)
quand la logique devient plus complexe.

```python
# Lambda (simple)
triple = lambda x: x * 3

# Fonction classique (plus claire pour des traitements longs)
def triple(x):
    return x * 3
```

---

### **5.5. Exercices**

1. Utiliser une lambda avec `map()` pour transformer une liste de températures Celsius en Fahrenheit.
2. Créer une lambda pour vérifier si une chaîne commence par une majuscule.
3. À partir d'une liste de nombres, générer avec une **compréhension** et une **lambda** une nouvelle liste des cubes pairs.
4. Trier une liste de tuples `(nom, âge)` selon l'âge avec `sorted()` et une lambda.

