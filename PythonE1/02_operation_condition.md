# **Opérations et conditions**

## **Objectifs pédagogiques**

* Comprendre la logique des **décisions** dans un programme.
* Savoir utiliser les **opérateurs arithmétiques et logiques**.
* Écrire des conditions imbriquées avec `if`, `elif`, `else`.
* Manipuler des **expressions booléennes** pour contrôler le flux d'exécution.
* Découvrir la **forme compacte** des tests conditionnels.

---

## **1. Opérateurs arithmétiques**

Les opérateurs arithmétiques permettent de réaliser des calculs sur des valeurs numériques.

| Opérateur | Description      | Exemple  | Résultat |
| --------- | ---------------- | -------- | -------- |
| `+`       | addition         | `5 + 3`  | 8        |
| `-`       | soustraction     | `10 - 2` | 8        |
| `*`       | multiplication   | `4 * 2`  | 8        |
| `/`       | division réelle  | `9 / 2`  | 4.5      |
| `//`      | division entière | `9 // 2` | 4        |
| `%`       | modulo (reste)   | `9 % 2`  | 1        |
| `**`      | puissance        | `3 ** 2` | 9        |

**Exemple :**

```python
a = 9
b = 2
print(a / b)   # 4.5
print(a // b)  # 4
print(a % b)   # 1
```

---

## **2. Conditions : `if`, `elif`, `else`**

Une condition permet d'exécuter une partie du code **seulement si** une expression est vraie (`True`).

**Structure de base :**

```python
if condition:
    # Code exécuté si la condition est vraie
elif autre_condition:
    # Code exécuté si la première est fausse mais celle-ci vraie
else:
    # Code exécuté si aucune condition n'est vraie
```

**Exemple simple :**

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```

**Résultat possible :**

```
Enter your age: 16
You are a teenager.
```

---

## **3. Opérateurs de comparaison**

Les opérateurs de comparaison permettent de **comparer deux valeurs**.
Ils renvoient toujours une valeur booléenne : `True` ou `False`.

| Opérateur | Signification       | Exemple   | Résultat |
| --------- | ------------------- | --------- | -------- |
| `==`      | égal à              | `5 == 5`  | `True`   |
| `!=`      | différent de        | `5 != 3`  | `True`   |
| `<`       | inférieur à         | `2 < 5`   | `True`   |
| `>`       | supérieur à         | `10 > 20` | `False`  |
| `<=`      | inférieur ou égal à | `5 <= 5`  | `True`   |
| `>=`      | supérieur ou égal à | `8 >= 3`  | `True`   |

**Exemple :**

```python
temperature = 22

if temperature > 25:
    print("It's hot.")
elif temperature < 10:
    print("It's cold.")
else:
    print("The weather is mild.")
```

---

## **4. Expressions booléennes composées**

Les conditions peuvent être combinées à l'aide des opérateurs **logiques** :
`and`, `or`, `not`

| Opérateur | Signification                           | Exemple              | Résultat                                          |
| --------- | --------------------------------------- | -------------------- | ------------------------------------------------- |
| `and`     | Les deux conditions doivent être vraies | `(x > 0 and x < 10)` | `True` si `x` est entre 1 et 9                    |
| `or`      | Au moins une condition vraie            | `(x < 0 or x > 10)`  | `True` si `x` est inférieur à 0 ou supérieur à 10 |
| `not`     | Inverse la condition                    | `not(x > 5)`         | `True` si `x <= 5`                                |

**Exemple combiné :**

```python
score = 75
bonus = True

if score > 80 or bonus:
    print("You passed with bonus points!")
else:
    print("You did not pass.")
```

**Exemple avec `and` :**

```python
x = 7
if x > 0 and x < 10:
    print("x is a positive number between 1 and 9.")
```

---

## **5. Syntaxe compacte : l'expression conditionnelle**

Python permet d'écrire une condition sur une seule ligne (forme dite *ternaire*) :

**Syntaxe :**

```python
value_if_true if condition else value_if_false
```

**Exemples :**

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)
```

```
adult
```

Autre exemple :

```python
x = 5
parity = "even" if x % 2 == 0 else "odd"
print(parity)  # odd
```

---

## **Exercices de mise en pratique**

1. **Créer** un programme qui demande la note d'un étudiant et affiche :

   * "Excellent" si la note ≥ 16
   * "Bien" si 12 ≤ note < 16
   * "Passable" si 10 ≤ note < 12
   * "Insuffisant" sinon

2. **Créer** un programme qui demande la température et affiche :

   * "Très froid" si < 0
   * "Froid" entre 0 et 10
   * "Chaud" entre 11 et 25
   * "Très chaud" au-delà de 25

3. **Créer** un programme qui demande un nombre et affiche s'il est **pair** ou **impair** en utilisant la forme compacte (`x if cond else y`).

4. **Créer** un mini jeu :

   * Le programme choisit un nombre entre 1 et 10.
   * L'utilisateur propose un nombre.
   * Le programme indique "Trop petit", "Trop grand" ou "Gagné !".
