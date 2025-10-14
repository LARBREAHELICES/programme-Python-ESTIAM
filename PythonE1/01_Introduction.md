# **Introduction à Python**

## 1. Présentation de Python et de ses usages

**Python** est un langage de programmation :

* **interprété** : il s'exécute ligne par ligne, sans compilation préalable.
* **multi-usage** : il sert aussi bien à la programmation web, à la data science, à l'intelligence artificielle qu'à la robotique.
* **lisible et simple** : sa syntaxe proche du langage naturel en fait un langage accessible aux débutants.

**Exemples d'usages courants :**

* Développement web : *FastAPI, Django, Flask*
* Analyse de données : *pandas, NumPy, matplotlib*
* Intelligence artificielle : *TensorFlow, PyTorch*
* Automatisation / scripts systèmes
* Prototypage rapide et enseignement

---

## 2. Installation et configuration de l'environnement

### a. Installation de Python

* Rendez-vous sur le site officiel : [https://www.python.org/downloads/](https://www.python.org/downloads/)
* Téléchargez la dernière version stable (ex. 3.13).
* Lors de l'installation sur Windows, cochez impérativement la case "Add Python to PATH".
Cette option permet de rendre Python accessible directement depuis la console et d'exécuter vos programmes sur votre machine sans configuration supplémentaire.

* Vérifiez l'installation dans le terminal :

  ```bash
  python --version
  ```

  ou

  ```bash
  python3 --version
  ```

---

### b. Installation de VS Code

VS Code est un éditeur léger et polyvalent. Mais vous avez aussi `Pycharm` un éditeur plus complet mais payant.

1. Télécharger sur : [https://code.visualstudio.com](https://code.visualstudio.com)
2. Installer l'**extension Python** (éditeur de Microsoft).
3. Ouvrir un nouveau dossier de travail pour vos projets.
4. Créer un fichier `main.py` pour vos premiers scripts.

---

### c. Utilisation du terminal

Le terminal permet d'exécuter directement vos scripts :

```bash
python main.py
```

ou selon votre système :

```bash
python3 main.py
```

---

### d. Création d'un environnement virtuel (`venv`)

Chaque projet Python doit fonctionner dans un **environnement isolé**, pour éviter les conflits de dépendances.

1. Créez un environnement virtuel :

   ```bash
   python -m venv env
   ```
2. Activez-le :

   * **Windows :**

     ```bash
     env\Scripts\activate
     ```
   * **macOS / Linux :**

     ```bash
     source env/bin/activate
     ```
3. Installez les dépendances :

   ```bash
   pip install fastapi uvicorn
   ```
4. Désactivez l'environnement après usage :

   ```bash
   deactivate
   ```

---

## 3. Premier script Python

Créer un fichier nommé `main.py` et écrire :

```python
# This is a comment: it is ignored by Python

# Display a message in the console
print("Hello, world!")
```

Exécuter le script :

```bash
python main.py
```

**Résultat :**

```
Hello, world!
```

### Points essentiels :

* `#` sert à écrire un **commentaire** (non exécuté).
* L'**indentation** (espaces en début de ligne) est obligatoire pour structurer le code.
* `print()` affiche du texte ou une valeur dans la console.

---

## 4. Variables et types de base

Une **variable** est un espace mémoire qui contient une valeur.
En Python, le type est **déduit automatiquement** (typage dynamique).

Exemples :

```python
name = "Alice"       # str (string)
age = 20             # int (integer)
height = 1.68        # float (decimal number)
is_student = True    # bool (boolean)
```

Afficher leur contenu :

```python
print(name, age, height, is_student)
```

Python fournit des fonctions utiles :

```python
print(type(name))   # affiche <class 'str'>
```

---

## 5. Entrée utilisateur : `input()`

La fonction `input()` permet de **récupérer une donnée saisie au clavier** :

```python
user_name = input("Enter your name: ")
print("Hello", user_name + "!")
```

> ⚠️ Par défaut, la valeur renvoyée par `input()` est une **chaîne de caractères (`str`)**, même si l'utilisateur saisit un nombre.

---

## 6. Conversion de types

Pour effectuer des calculs, il faut **convertir les chaînes** en nombres avec les fonctions `int()` ou `float()` :

```python
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# Convert strings to floats
num1 = float(num1)
num2 = float(num2)

result = num1 + num2
print("The sum is:", result)
```

Conversion inverse (vers une chaîne) :

```python
age = 20
print("You are " + str(age) + " years old.")
```

---

## **Résumé de la séquence**

| Concept            | Exemple                       | Objectif                |
| ------------------ | ----------------------------- | ----------------------- |
| `print()`          | `print("Hello")`              | Afficher un texte       |
| Commentaire        | `# This is a comment`         | Expliquer le code       |
| Variable           | `x = 5`                       | Stocker une valeur      |
| Type de base       | `int`, `float`, `str`, `bool` | Manipuler des données   |
| Entrée utilisateur | `input()`                     | Lire une valeur clavier |
| Conversion         | `int()`, `float()`, `str()`   | Adapter les types       |
