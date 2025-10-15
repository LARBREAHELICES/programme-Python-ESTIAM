# **Rappels fondamentaux sur Python**

Ce module introduit les mécanismes internes de Python : comment le langage gère les objets, le typage, les références et la mémoire. Ces notions expliquent la plupart des comportements parfois surprenants observés dans le code.

---

## **1. Modèle d'exécution et typage**

### **1.1. Python comme langage interprété et typé dynamiquement**

Python est un langage **interprété** : le code est lu et exécuté ligne par ligne, sans étape de compilation préalable.
Il est également **dynamiquement typé** : les types sont attribués à l'exécution.

**Exemple :**

```python
x = 10          # x référence un entier
print(type(x))  # <class 'int'>

x = "hello"     # x référence maintenant une chaîne
print(type(x))  # <class 'str'>
```

Ici, le **type est une propriété de l'objet**, pas de la variable.
Une même variable peut successivement référencer des objets de types différents.

---

### **1.2. Typage fort vs typage faible**

Python impose un **typage fort** : il ne convertit pas automatiquement les objets incompatibles.
Les conversions doivent être explicites.

```python
a = "5"
b = 2
# print(a + b)  # Provoque une erreur
print(int(a) + b)  # 7
```

Dans un langage faiblement typé (comme JavaScript), l'opération serait tolérée.
En Python, cela garantit une plus grande sécurité des types.

---

### **1.3. Typage par référence et identité des objets**

Une variable ne contient pas une valeur, mais une **référence vers un objet**.

```python
a = [1, 2, 3]
b = a
b.append(4)

print(a)      # [1, 2, 3, 4]
print(a is b) # True : a et b pointent vers le même objet
```

Les fonctions `id()` et `is` permettent de vérifier cette identité :

```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True  : même contenu
print(x is y)  # False : objets différents
```

* `==` compare le **contenu**.
* `is` compare l'**identité mémoire**.

---

### **1.4. Objets immuables et mutables**

Certains objets peuvent être modifiés, d'autres non.

| Type                           | Mutabilité | Exemple                                 |
| ------------------------------ | ---------- | --------------------------------------- |
| `int`, `float`, `str`, `tuple` | Immuables  | toute modification crée un nouvel objet |
| `list`, `dict`, `set`          | Mutables   | modifiables en place                    |

**Exemples :**

Immuable :

```python
x = 10
print(id(x))
x += 1
print(id(x))  # Identifiant différent
```

Mutable :

```python
lst = [1, 2, 3]
print(id(lst))
lst.append(4)
print(id(lst))  # Identique : l'objet a été modifié
```

---

### **1.5. Implications du modèle mémoire**

1. Les objets **mutables** peuvent être modifiés par inadvertance.

   ```python
   def modify(lst):
       lst.append(100)

   data = [1, 2, 3]
   modify(data)
   print(data)  # [1, 2, 3, 100]
   ```

   → Pour éviter cela, passer une **copie** :

   ```python
   modify(data.copy())
   ```

2. Les objets **immuables** sont sûrs à partager.

3. Les **alias de référence** provoquent des effets en chaîne :

   ```python
   a = [[0] * 3] * 3
   a[0][0] = 1
   print(a)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
   ```

---

### **Exercices**

1. Créer une liste `a`, affecter `b = a`, puis ajouter un élément à `b`.
   Expliquer pourquoi `a` a également changé.
2. Créer deux listes identiques et comparer avec `==` et `is`.
3. Créer une variable `n = 100`, afficher `id(n)`, puis `n += 1`.
   Expliquer la différence entre les identifiants.
4. Tester la fonction suivante sur une liste et sur un tuple :

   ```python
   def add_item(collection, item):
       collection.append(item)
   ```

---

## **2. Références, copies et gestion mémoire**

### **2.1. Compréhension du mécanisme de référence**

Une affectation ne crée pas une copie, mais un **alias** vers le même objet.

```python
a = [1, 2, 3]
b = a
b.append(4)

print(a)  # [1, 2, 3, 4]
print(id(a), id(b))  # même identifiant
```

Pour créer une nouvelle liste :

```python
b = a.copy()  # ou list(a)
```

---

### **2.2. Copies superficielles et profondes**

**Copie superficielle** : seul le premier niveau est copié.
Les sous-objets restent partagés.

```python
import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0].append(99)

print(a)  # [[1, 2, 99], [3, 4]]
```

**Copie profonde** : tout est dupliqué récursivement.

```python
b = copy.deepcopy(a)
b[0].append(42)

print(a)  # inchangé
print(b)  # indépendant
```

---

### **2.3. Gestion du ramasse-miettes (garbage collector)**

Python gère automatiquement la mémoire :

* chaque objet possède un **compteur de références** ;
* lorsqu'il tombe à zéro, l'objet est détruit ;
* le module `gc` traite les cas complexes (références circulaires).

```python
import gc
a = [1, 2, 3]
b = a
del a
del b
gc.collect()  # libère les objets non référencés
```

---

### **2.4. Bonnes pratiques pour éviter les effets de bord**

1. **Toujours identifier les objets mutables** avant de les passer à une fonction.
2. **Privilégier des fonctions pures** : elles ne modifient pas leurs arguments.
3. **Créer explicitement des copies** quand on manipule des structures imbriquées.
4. **Utiliser `deepcopy()`** lorsque la structure contient plusieurs niveaux d'imbrication.
5. **Éviter les constructions piégeuses** :

   ```python
   grid = [[0] * 3 for _ in range(3)]  # correct
   grid = [[0] * 3] * 3                # erreur classique
   ```

---

### **Exercices**

1. Créer une liste `matrix = [[1, 2], [3, 4]]`, puis `matrix_copy = copy.copy(matrix)`.
   Modifier `matrix_copy[0][0]` et observer le résultat.
2. Refaire l'exercice avec `copy.deepcopy()` et comparer.
3. Créer une fonction qui reçoit une liste et ajoute un élément sans modifier l'originale.
4. Créer une liste `a`, supprimer ses références avec `del`, puis forcer le nettoyage avec `gc.collect()`.

---

### **Résumé des notions clés**

| Concept             | Description                                      | Exemple               |
| ------------------- | ------------------------------------------------ | --------------------- |
| Référence           | Un nom pointe vers un objet                      | `b = a`               |
| Copie superficielle | Copie du conteneur, sous-objets partagés         | `copy.copy(a)`        |
| Copie profonde      | Duplication complète de la structure             | `copy.deepcopy(a)`    |
| Objet mutable       | Modifiable sans recréer l'objet                  | `list`, `dict`        |
| Objet immuable      | Création d'un nouvel objet à chaque modification | `int`, `str`, `tuple` |

---

# **3. Structures de données complexes**

Cette partie aborde la manipulation de structures imbriquées et les techniques modernes d'écriture Pythonique pour transformer, trier et filtrer les données efficacement.

---

### **3.1. Listes imbriquées, dictionnaires de listes et tuples composites**

Python permet de structurer les données en combinant plusieurs conteneurs.

**Exemples de structures :**

```python
# Liste de listes
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Dictionnaire de listes
students = {
    "Alice": [15, 17, 14],
    "Bob": [12, 10, 13],
}

# Liste de tuples
records = [
    ("Alice", 15),
    ("Bob", 12),
    ("Charlie", 18)
]
```

Ces structures peuvent être parcourues de manière imbriquée :

```python
for row in matrix:
    for value in row:
        print(value, end=" ")
```

**Cas pratique : moyenne des notes par étudiant**

```python
for name, scores in students.items():
    avg = sum(scores) / len(scores)
    print(name, "->", avg)
```

---

### **3.2. Compréhensions de listes, sets et dictionnaires**

Les compréhensions permettent de **créer ou transformer une structure** en une seule ligne, de manière lisible et efficace.

**Liste :**

```python
squares = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

**Filtrage :**

```python
even = [x for x in range(10) if x % 2 == 0]
```

**Ensemble :**

```python
unique_lengths = {len(name) for name in ["Alice", "Bob", "Anna"]}
```

**Dictionnaire :**

```python
squares_dict = {x: x ** 2 for x in range(5)}
```

**Compréhensions imbriquées :**

```python
matrix = [[i * j for j in range(3)] for i in range(3)]
```

Ces constructions remplacent avantageusement les boucles longues et rendent le code plus concis.

---

### **3.3. Tri et filtrage avancés (`sorted`, `key`, `lambda`)**

La fonction `sorted()` accepte un paramètre `key` qui permet de définir une logique de tri personnalisée.

**Exemples :**

```python
names = ["Bob", "Alice", "Charlie"]
print(sorted(names))  # Tri alphabétique

# Tri par longueur
print(sorted(names, key=len))
```

**Tri d'une liste de tuples :**

```python
students = [("Alice", 15), ("Bob", 12), ("Charlie", 18)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_by_score)
```

---

### **3.4. Approche fonctionnelle : `map`, `filter`, `reduce`**

Ces fonctions permettent d'appliquer des transformations sans boucles explicites.

**`map()` – appliquer une fonction :**

```python
nums = [1, 2, 3, 4]
doubles = list(map(lambda x: x * 2, nums))
```

**`filter()` – sélectionner des éléments :**

```python
evens = list(filter(lambda x: x % 2 == 0, nums))
```

**`reduce()` – réduire une séquence à une seule valeur :**

```python
from functools import reduce
total = reduce(lambda acc, x: acc + x, nums, 0)
```

---

### **Exercices**

1. À partir du dictionnaire :

   ```python
   data = {
       "Alice": 15,
       "Bob": 12,
       "Charlie": 18,
       "David": 10
   }
   ```

   Créer une liste triée des noms selon la note décroissante.

2. À partir de la liste :

   ```python
   scores = [8, 15, 12, 19, 6, 13]
   ```

   Filtrer les notes supérieures à 10, puis calculer leur carré avec une compréhension.

3. Créer un dictionnaire `{nom: moyenne}` à partir d'un dictionnaire d'étudiants contenant leurs listes de notes.

---

# **4. Exceptions, documentation et fonctions avancées**

Cette section présente la gestion des erreurs, la création d'exceptions personnalisées et les bonnes pratiques pour rendre le code robuste et maintenable.

---

### **4.1. Structure `try / except / else / finally`**

Le bloc `try` permet de capturer les erreurs et d'éviter les interruptions brutales.

**Exemple simple :**

```python
try:
    x = int(input("Entrez un nombre : "))
    print(10 / x)
except ZeroDivisionError:
    print("Erreur : division par zéro.")
except ValueError:
    print("Erreur : saisie invalide.")
else:
    print("Calcul réussi.")
finally:
    print("Fin du programme.")
```

* `try` : code principal.
* `except` : gère les erreurs spécifiques.
* `else` : exécuté si aucune exception ne survient.
* `finally` : exécuté quoi qu'il arrive (fermeture de fichier, nettoyage, etc.).

---

### **4.2. Levée d'exceptions personnalisées**

On peut **déclencher** une exception avec `raise`, et définir ses propres classes d'erreurs.

**Exemple :**

```python
class NegativeNumberError(Exception):
    """Exception levée quand un nombre négatif est fourni."""
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Le nombre doit être positif.")
    return x ** 0.5
```

```python
try:
    print(square_root(-9))
except NegativeNumberError as e:
    print("Erreur :", e)
```

---

### **4.3. Propagation et capture des erreurs**

Une exception non gérée remonte la pile d'appels jusqu'à être interceptée, sinon elle provoque l'arrêt du programme.

**Exemple :**

```python
def division(a, b):
    return a / b

def compute():
    return division(10, 0)

try:
    compute()
except ZeroDivisionError:
    print("Erreur détectée dans compute()")
```

---

### **4.4. Bonnes pratiques**

* Toujours **valider les entrées** avant de traiter.
* **Limiter la portée du bloc try** : ne pas envelopper tout le code.
* Utiliser des **messages explicites** :

  ```python
  raise ValueError("Le paramètre 'age' doit être un entier positif.")
  ```
* **Journaliser les erreurs** (module `logging`) plutôt que d'afficher avec `print()`.

---

### **4.5. Hiérarchie d'exceptions propres à un module**

Créer des exceptions spécifiques améliore la lisibilité et la maintenance du code.

**Exemple :**

```python
class AppError(Exception):
    pass

class DataError(AppError):
    pass

class NetworkError(AppError):
    pass
```

Les blocs `except` peuvent ensuite cibler les sous-classes :

```python
try:
    raise DataError("Problème de données.")
except AppError as e:
    print("Erreur de l'application :", e)
```

---

### **Exercices**

1. Écrire une fonction `safe_div(a, b)` qui :

   * renvoie le résultat de `a / b`,
   * lève une exception personnalisée `DivisionByZeroError` si `b == 0`.

2. Écrire une fonction `read_file(path)` qui :

   * ouvre un fichier texte,
   * renvoie son contenu,
   * gère les erreurs de fichier introuvable ou de permission refusée.

3. Créer une hiérarchie d'exceptions pour un module `data_processing` :

   * `DataError`, `FileFormatError`, `EmptyDataError`.
     Simuler une levée et un traitement de ces erreurs dans un bloc `try/except`.

---

# **5. Documentation et docstrings**

Documenter le code est une composante essentielle du développement professionnel.
Les *docstrings* (chaînes de documentation) décrivent le rôle, les paramètres et le comportement d'une fonction, classe ou module.

---

### **5.1. Rôle et conventions des docstrings (PEP 257)**

Une *docstring* est une chaîne de caractères placée **immédiatement après la définition** d'une fonction, classe ou module.
Elle est utilisée par Python pour générer la documentation accessible via `help()` ou les outils d'analyse.

**Exemple :**

```python
def add(a, b):
    """Retourne la somme de deux nombres."""
    return a + b
```

La *PEP 257* recommande :

* D'utiliser des triples guillemets (`"""`).
* De commencer par une **phrase descriptive courte**.
* D'ajouter des détails ou exemples sur plusieurs lignes si nécessaire.

---

### **5.2. Structure d'une docstring complète**

Une docstring claire doit décrire :

* le **rôle** de la fonction ;
* les **paramètres** et leurs types ;
* la **valeur de retour** ;
* les **exceptions** levées (le cas échéant).

**Exemple structuré (style Google) :**

```python
def divide(a: float, b: float) -> float:
    """
    Calcule la division de deux nombres.

    Args:
        a (float): Numérateur.
        b (float): Dénominateur (doit être non nul).

    Returns:
        float: Résultat de la division.

    Raises:
        ValueError: Si b est égal à zéro.
    """
    if b == 0:
        raise ValueError("Division par zéro interdite.")
    return a / b
```

D'autres styles existent (NumPy, reStructuredText), mais le style Google est souvent préféré pour sa lisibilité.

---

### **5.3. Interaction avec `help()` et outils de documentation**

Python permet d'accéder directement à la docstring :

```python
help(divide)
print(divide.__doc__)
```

Pour générer une documentation automatisée :

* **`pdoc`** : génère des pages HTML simples à partir du code.
* **`Sphinx`** : outil plus complet, utilisé pour documenter des bibliothèques professionnelles.

Commandes d'installation :

```bash
pip install pdoc sphinx
```

---

### **5.4. Typage statique et vérification (`type hints` et `mypy`)**

Python reste dynamiquement typé, mais il supporte les **annotations de type** depuis la PEP 484.
Elles facilitent la lecture, la validation et les vérifications automatiques.

**Exemple :**

```python
def greet(name: str, times: int = 1) -> str:
    return ("Bonjour " + name + " ! ") * times
```

Les types ne sont **pas vérifiés à l'exécution**, mais peuvent être analysés avec :

```bash
mypy fichier.py
```

---

### **Exercice**

Écrire et documenter la fonction suivante :

```python
def analyse(liste: list[float]) -> dict[str, float]:
    """
    Calcule les statistiques principales d'une liste de nombres.

    Args:
        liste (list[float]): Ensemble de valeurs numériques.

    Returns:
        dict[str, float]: Dictionnaire contenant la moyenne, la médiane et la variance.

    Raises:
        ValueError: Si la liste est vide.
    """
```

Implémenter la fonction puis vérifier la documentation avec `help(analyse)`.

---

# **6. Fonctions avancées et programmation fonctionnelle**

Cette partie approfondit les capacités de Python à manipuler les fonctions comme des objets : création, transmission et composition.

---

### **6.1. Fonctions anonymes (`lambda`)**

Les fonctions `lambda` sont des fonctions **courtes et sans nom**, souvent utilisées pour des opérations simples.

**Exemples :**

```python
square = lambda x: x ** 2
print(square(5))  # 25

add = lambda a, b: a + b
```

Elles sont utiles dans les fonctions d'ordre supérieur (`map`, `filter`, `sorted`, etc.) :

```python
nums = [1, 2, 3, 4]
doubles = list(map(lambda x: x * 2, nums))
```

---

### **6.2. Fonctions d'ordre supérieur : `map`, `filter`, `reduce`**

Ces fonctions prennent **d'autres fonctions en argument**.

```python
nums = [1, 2, 3, 4, 5]

# map : transformation
squares = list(map(lambda x: x ** 2, nums))

# filter : sélection
evens = list(filter(lambda x: x % 2 == 0, nums))

# reduce : agrégation
from functools import reduce
product = reduce(lambda a, b: a * b, nums)
```

---

### **6.3. Fonctions génératrices (`yield`) et expressions génératrices**

Une fonction génératrice produit une **suite de valeurs** sans tout charger en mémoire.
Elles utilisent le mot-clé `yield` au lieu de `return`.

**Exemple :**

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)
```

Les **expressions génératrices** offrent une syntaxe compacte :

```python
squares = (x ** 2 for x in range(5))
print(sum(squares))
```

---

### **6.4. Portée des variables et règle LEGB**

Python détermine la portée d'un nom selon la règle **LEGB** :

* **L**ocal : variables définies dans une fonction.
* **E**nclosing : portées englobantes (fonctions imbriquées).
* **G**lobal : variables du module.
* **B**uiltin : fonctions Python (`len`, `print`, etc.).

**Exemple :**

```python
x = 10

def outer():
    x = 5
    def inner():
        print(x)  # utilise la variable de outer()
    inner()

outer()
```

---

### **6.5. Closures et expressions conditionnelles**

Une *closure* est une fonction qui retient une variable définie dans un contexte englobant.

**Exemple :**

```python
def multiplier(n):
    def inner(x):
        return x * n
    return inner

times3 = multiplier(3)
print(times3(5))  # 15
```

**Expressions conditionnelles :**

```python
result = "pair" if 4 % 2 == 0 else "impair"
```

---

### **Exercices**

1. Reproduire un filtrage avec une fonction `lambda` :

   ```python
   # Extraire les mots de plus de 4 lettres
   words = ["chat", "voiture", "arbre", "eau"]
   ```

   Utiliser `filter` et une `lambda`.

2. Créer un générateur `powers(base, limit)` qui produit les puissances successives d'un nombre jusqu'à une limite donnée :

   ```python
   for val in powers(2, 5):
       print(val)
   # 1, 2, 4, 8, 16
   ```

3. Écrire une fonction `apply_all(functions, value)` :

   * `functions` est une liste de fonctions,
   * `value` est la donnée d'entrée,
   * la fonction retourne la liste des résultats.

   **Exemple :**

   ```python
   funcs = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
   print(apply_all(funcs, 3))  # [4, 6, 9]
   ```
