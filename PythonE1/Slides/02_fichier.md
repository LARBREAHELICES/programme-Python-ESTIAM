---
marp: true
theme: default
paginate: true
class: lead
---


# **Chapitre – Manipulation de fichiers en Python**

---

### **1. Introduction**

Les fichiers permettent de **stocker des données de manière persistante** (texte, CSV, JSON, etc.).
Python fournit des fonctions intégrées pour lire et écrire dans des fichiers via la fonction `open()`.

---

### **2. Ouvrir un fichier**

Syntaxe de base :

```python
f = open("data.txt", "r")  # "r" pour lecture (read)
content = f.read()
f.close()
```

Mais il est **recommandé** d’utiliser le mot-clé `with`,
qui ferme automatiquement le fichier même en cas d’erreur.

```python
with open("data.txt", "r") as f:
    content = f.read()
print(content)
```

---

### **3. Modes d’ouverture**

| Mode  | Signification                                     | Exemple                 |
| ----- | ------------------------------------------------- | ----------------------- |
| `"r"` | Lecture seule (erreur si le fichier n’existe pas) | `open("f.txt", "r")`    |
| `"w"` | Écriture (écrase le contenu existant)             | `open("f.txt", "w")`    |
| `"a"` | Ajout en fin de fichier                           | `open("f.txt", "a")`    |
| `"b"` | Mode binaire (images, PDF, etc.)                  | `open("img.png", "rb")` |

Vous pouvez combiner les modes : `"wb"`, `"ab"`, etc.

---

### **4. Lecture de fichier texte**

#### Lire tout le contenu :

```python
with open("notes.txt", "r") as f:
    data = f.read()
print(data)
```

---

#### Lire ligne par ligne :

```python
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())  # strip() retire le saut de ligne
```

---

#### Lire toutes les lignes en liste :

```python
with open("notes.txt") as f:
    lines = f.readlines()
print(lines)
```

---

### **5. Écrire dans un fichier**

#### Écraser un fichier :

```python
with open("output.txt", "w") as f:
    f.write("Première ligne\n")
    f.write("Deuxième ligne\n")
```

#### Ajouter du texte à la fin :

```python
with open("output.txt", "a") as f:
    f.write("Nouvelle ligne ajoutée\n")
```

---

### **6. Exemple complet**

```python
# Crée un fichier avec des notes d’étudiants
with open("notes.txt", "w") as f:
    f.write("Alice: 15\nBob: 12\nCharlie: 17\n")

# Lecture et calcul de la moyenne
total = 0
count = 0
with open("notes.txt", "r") as f:
    for line in f:
        name, score = line.strip().split(": ")
        total += int(score)
        count += 1

print("Moyenne :", total / count)
```

---

### **7. Bonnes pratiques**

1. Toujours utiliser `with open(...)` pour éviter les oublis de `close()`.
2. Bien choisir le mode d’ouverture (`"r"`, `"w"`, `"a"`, `"b"`).
3. Penser à **l’encodage** (`encoding="utf-8"`) pour les fichiers texte :

   ```python
   with open("data.txt", "r", encoding="utf-8") as f:
       ...
   ```

---

### **Exercices**

1. **Créer un fichier `journal.txt`** et y écrire trois lignes de texte.
2. **Lire et afficher** chaque ligne précédée de son numéro (`Ligne 1 : ...`).
3. **Écrire un programme** qui lit un fichier contenant des nombres (un par ligne) et affiche la somme totale.
4. **Ajouter** une ligne de texte à un fichier existant sans effacer son contenu.
