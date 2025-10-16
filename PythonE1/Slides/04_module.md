---
marp: true
theme: default
paginate: true
class: lead
---

# **Les modules en Python**

---

### **1. Qu'est-ce qu'un module ?**

Un **module** est un **fichier Python (.py)** contenant du code (fonctions, classes, variables) que l'on peut **réutiliser** dans d'autres programmes.

Créer un module permet de **structurer** un projet, **éviter la duplication** et **favoriser la maintenance**.

---

### **2. Création d'un module**

Exemple d'un module `math_utils.py` :

```python
# math_utils.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

Et dans un autre fichier :

```python
# main.py
import math_utils

print(math_utils.add(3, 5))       # 8
print(math_utils.multiply(2, 4))  # 8
```

---

### **3. Import sélectif**

On peut importer uniquement les éléments nécessaires :

```python
from math_utils import add
print(add(10, 20))
```

On peut aussi renommer pour plus de clarté :

```python
import math_utils as mu
print(mu.add(1, 2))
```

---

### **4. Structure de projet (modules et packages)**

Un **package** est un dossier contenant un fichier `__init__.py` (même vide).
Il permet de regrouper plusieurs modules.

```
project/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── utils.py
│
└── main.py
```

```python
# main.py
from app.utils import add_user
```

---

### **5. Import relatif et absolu**

* **Import absolu :**

  ```python
  from app.utils import add_user
  ```
* **Import relatif (à éviter hors packages internes) :**

  ```python
  from .utils import add_user
  ```

Depuis **Python 3.13**, la gestion des imports reste identique,
mais les imports relatifs sont **mieux vérifiés** au moment de l'exécution,
et les messages d'erreurs sont plus explicites.

---

### **6. Nouveau comportement Python 3.13 : isolation des modules compilés**

Python 3.13 renforce la gestion des modules via :

* un **cache d'importation plus strict** (`__pycache__` isolé par version),
* une **meilleure séparation entre environnement utilisateur et système**,
* la possibilité d'utiliser des **modules natifs compilés** (`.pyd` / `.so`) isolés par architecture.

Cela garantit que chaque environnement virtuel ne charge que **ses propres dépendances**.

---

### **7. Modules standards à connaître**

Quelques modules intégrés couramment utilisés :

| Module     | Utilité principale                         |
| ---------- | ------------------------------------------ |
| `math`     | Fonctions mathématiques                    |
| `random`   | Génération de nombres aléatoires           |
| `datetime` | Gestion des dates et heures                |
| `os`       | Interaction avec le système d'exploitation |
| `pathlib`  | Manipulation de chemins de fichiers        |
| `json`     | Lecture/écriture de fichiers JSON          |

---

### **Exemple pratique**

```python
import os
from datetime import datetime
import json

# Création d'un dossier
os.makedirs("logs", exist_ok=True)

# Création d'un fichier de log au format JSON
log = {"timestamp": datetime.now().isoformat(), "event": "start"}
with open("logs/log.json", "w") as f:
    json.dump(log, f, indent=2)
```

---

### **Exercices**

1. Créer un module `geometry.py` avec les fonctions `area_circle(r)` et `area_square(cote)`.
   L'importer et l'utiliser dans un fichier principal `main.py`.

2. Créer un package `school/` contenant :

   * `students.py` avec une classe `Student`
   * `teachers.py` avec une classe `Teacher`
   * et un `__init__.py` qui les expose.

---

3. Écrire un script qui :

   * importe `datetime` et affiche la date du jour,
   * crée un dossier `backup/` avec `os.makedirs()`,
   * sauvegarde un fichier JSON contenant la date et l'heure de sauvegarde.


---

# **Chapitre – Éviter les imports circulaires en Python**

---

### **Définition**

Un **import circulaire** se produit lorsque **deux modules s'importent mutuellement**,
soit directement, soit indirectement.
Cela provoque une erreur au moment du chargement, car Python ne peut pas terminer l'initialisation des modules.

---

### **Exemple du problème**

```
project/
├── a.py
└── b.py
```

```python
# a.py
from b import hello_b

def hello_a():
    print("Bonjour depuis A")

hello_b()
```

```python
# b.py
from a import hello_a

def hello_b():
    print("Bonjour depuis B")

hello_a()
```

Lancer `python a.py` provoque :

```
ImportError: cannot import name 'hello_a' from partially initialized module 'a'
```

---

### **Pourquoi cela arrive**

Lorsqu'un module est importé :

1. Python crée une **entrée vide** dans `sys.modules`.
2. Il **exécute le code** du module.
3. Il **enregistre** le module comme “chargé”.

Si un autre module tente d'importer le premier avant la fin de cette phase,
il obtient une version **partiellement initialisée**, donc inutilisable.

---

### **Bonnes pratiques pour éviter les imports circulaires**

#### **1. Réorganiser les imports**

Importer uniquement là où c'est nécessaire (souvent à l'intérieur d'une fonction plutôt qu'en haut du fichier).

```python
# b.py
def hello_b():
    from a import hello_a  # import local
    print("Bonjour depuis B")
    hello_a()
```

---

#### **2. Centraliser les dépendances communes**

Créer un module tiers pour contenir les éléments utilisés par plusieurs modules.

```
project/
├── common.py
├── a.py
└── b.py
```

---

```python
# common.py
def shared_function():
    print("Fonction partagée")
```

Puis :

```python
# a.py
from common import shared_function
```

```python
# b.py
from common import shared_function
```

---

#### **3. Retarder la résolution des types**

Depuis **Python 3.7+** (et toujours valide en 3.13),
on peut activer les **annotations différées** pour éviter d'importer des classes trop tôt :

```python
from __future__ import annotations

class User:
    def __init__(self, name: str, group: Group):  # Group n'est pas encore défini
        self.name = name
        self.group = group

class Group:
    def __init__(self, title: str):
        self.title = title
```

---

### **En résumé**

| Mauvaise pratique                      | Bonne alternative                                  |
| -------------------------------------- | -------------------------------------------------- |
| Imports croisés en haut de fichiers    | Imports locaux dans les fonctions                  |
| Dépendances réciproques entre classes  | Extraire la logique commune dans un module partagé |
| Référence directe dans les annotations | Utiliser `from __future__ import annotations`      |

---

### **Exercice**

Créer deux modules `user.py` et `group.py` :

* `user.py` contient une classe `User` qui référence un `Group`
* `group.py` contient une classe `Group` qui référence une liste de `User`

* Questions avancées

Provoquer une erreur d'import, puis la corriger :

1. en utilisant `from __future__ import annotations`
2. ou en créant un module `models/shared.py` contenant les types communs.
