
# **Chapitre – Introduction à la Programmation Orientée Objet**

---

### **1. Pourquoi l'objet ?**

Jusqu'ici, nous avons manipulé des **données et fonctions séparées**.
La programmation orientée objet (POO) permet de **regrouper données et comportements** dans une seule entité : **la classe**.

Une classe définit **le modèle** d'un objet.
Un objet est **une instance** de cette classe.

---

### **2. Exemple de classe simple**

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"{self.name} a obtenu la note de {self.grade}")
```

**Utilisation :**

```python
s1 = Student("Alice", 15)
s2 = Student("Bob", 12)

s1.display()
s2.display()
```

---

### **3. Variables et méthodes d'instance**

* Les **attributs** sont les données propres à chaque objet.
* Les **méthodes** sont les fonctions qui agissent sur ces données.

Chaque méthode reçoit automatiquement le paramètre `self`,
qui représente **l'instance courante**.

---

### **4. Responsabilité unique (Single Responsibility Principle)**

Une **classe doit avoir une seule raison de changer**.
Elle ne doit remplir **qu'un seul rôle cohérent**.

C'est un des principes fondamentaux du développement structuré (principe SOLID).

**Exemple à éviter :**

```python
class Student:
    def __init__(self, name):
        self.name = name

    def save_to_file(self):
        with open("students.txt", "a") as f:
            f.write(self.name)
```

Cette classe mélange **modèle de données** et **accès au stockage**.

---

### **5. Exemple corrigé avec responsabilité séparée**

```python
class Student:
    def __init__(self, name):
        self.name = name

class StudentRepository:
    def save(self, student: Student):
        with open("students.txt", "a") as f:
            f.write(student.name + "\n")
```

* `Student` s'occupe uniquement de **représenter un élève**.
* `StudentRepository` gère la **sauvegarde**.
* Si demain on change le format de stockage (base de données, API, etc.), on ne modifie que `StudentRepository`.

---

### **6. Illustration par un exemple plus concret**

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        self.price -= self.price * percent / 100

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product: Product):
        self.items.append(product)

    def total(self):
        return sum(p.price for p in self.items)
```

```python
p1 = Product("Livre", 20)
p2 = Product("Stylo", 2)
p1.apply_discount(10)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
print(cart.total())  # 20.0
```

Chaque classe a un rôle précis :

* `Product` gère la logique métier d'un produit.
* `Cart` gère la composition et le calcul du total.

---

### **7. Exercices**

1. Créer une classe `Book` avec titre, auteur et méthode `display()`.
2. Créer une classe `Library` qui contient une liste de livres et une méthode `add_book(book)`.
3. Appliquer le principe de responsabilité unique : la classe `Book` ne doit pas gérer l'affichage ni la sauvegarde.
4. Ajouter une méthode dans `Library` pour compter le nombre total de livres.

---

# **Introduction au polymorphisme**

---

### **1. Définition**

Le **polymorphisme** (du grec *"plusieurs formes"*) désigne la capacité de différents objets à **répondre à la même méthode**, même si leur implémentation diffère.

En Python, le polymorphisme repose sur le **typage dynamique** :
si deux objets possèdent une méthode du même nom, ils peuvent être utilisés de manière interchangeable.

---

### **2. Exemple simple**

```python
class Dog:
    def speak(self):
        return "Wouf !"

class Cat:
    def speak(self):
        return "Miaou !"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
```

**Sortie :**

```
Wouf !
Miaou !
```

Ici, la même méthode `speak()` existe dans les deux classes,
mais son comportement dépend du type réel de l'objet.

---

### **3. Polymorphisme et héritage**

Le polymorphisme devient particulièrement clair avec **l'héritage**.

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
        return 3.1416 * self.radius**2

shapes = [Rectangle(4, 5), Circle(3)]

for s in shapes:
    print(s.area())
```

**Sortie :**

```
20
28.2744
```

Chaque classe dérivée implémente la méthode `area()` selon sa logique propre.
Le programme principal ne se soucie pas du type concret : il appelle `area()` sur chaque forme.

---

### **4. Polymorphisme par “duck typing”**

Python n'exige pas de relation d'héritage explicite :
ce qui compte, c'est que l'objet **possède la méthode attendue**.

> “If it walks like a duck and quacks like a duck, it's a duck.”

```python
class Duck:
    def quack(self):
        print("Coin coin")

class Person:
    def quack(self):
        print("Je fais le canard !")

for obj in [Duck(), Person()]:
    obj.quack()
```

Même sans héritage, les deux objets sont **compatibles** car ils exposent la même interface (`quack()`).

---

### **5. Exemple d'application**

Une fonction qui manipule des objets “imprimables”, sans connaître leur type :

```python
def print_description(obj):
    print(obj.describe())

class Car:
    def describe(self):
        return "Une voiture à 4 roues"

class Plane:
    def describe(self):
        return "Un avion à 2 ailes"

for o in [Car(), Plane()]:
    print_description(o)
```

---

### **Exercices**

1. Créer une classe `Animal` avec une méthode `speak()`, et deux sous-classes `Dog` et `Bird` qui redéfinissent cette méthode.
2. Écrire une fonction `make_sound(animals)` qui appelle `speak()` sur chaque objet d'une liste d'animaux.
3. Implémenter un polymorphisme sans héritage : une classe `Printer` et une classe `Screen`, toutes deux avec une méthode `display()`.
4. Ajouter une fonction `show_all(objects)` qui affiche le résultat de `display()` pour chaque élément.

---