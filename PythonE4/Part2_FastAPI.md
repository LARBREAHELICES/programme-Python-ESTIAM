# **Formation FastAPI – Découverte et mise en pratique (1 journée)**

## **Objectifs pédagogiques**

* Comprendre les principes de base de FastAPI et du développement d'API REST
* Structurer un petit projet FastAPI propre et modulaire
* Manipuler les requêtes et réponses JSON, la validation de données avec Pydantic
* Mettre en œuvre un mini projet API complet (analyse de données ou gestion d'objets)

---

## **Matinée – Introduction et fondations**

### **1. Introduction à FastAPI (≈ 45 min)**

**Objectifs :** comprendre le cadre général et le positionnement de FastAPI.

* Qu'est-ce qu'une API REST
* Pourquoi FastAPI (asynchronisme, validation, documentation automatique)
* Installation et mise en route (`pip install fastapi uvicorn`)
* Structure minimale d'un projet :

  ```
  main.py
  └── app/
      ├── models.py
      ├── routers/
      └── utils.py
  ```

**Démonstration :**

* Création d'un premier endpoint “Hello World”

  ```python
  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/")
  def read_root():
      return {"message": "Bienvenue sur mon API"}
  ```

* Lancer le serveur avec :

  ```
  uvicorn main:app --reload
  ```

---

### **2. Les routes et les méthodes HTTP (≈ 1h)**

**Objectifs :** manipuler les routes et les méthodes principales.

* Méthodes HTTP : GET, POST, PUT, DELETE
* Paramètres de chemin et de requête (`@app.get("/items/{item_id}")`)
* Requêtes avec corps JSON (`POST`)
* Réponses et codes HTTP (`status_code`, `Response`)

**Exemple :**

```python
from fastapi import FastAPI

app = FastAPI()

items = {"apple": 3, "banane": 5}

@app.get("/items/{name}")
def read_item(name: str):
    return {"item": name, "stock": items.get(name, 0)}

@app.post("/items/")
def add_item(name: str, quantity: int):
    items[name] = quantity
    return {"message": f"{name} ajouté avec {quantity} unités"}
```

**Exercice guidé :**

* Créer une API permettant de gérer un petit inventaire : ajouter, consulter, supprimer un article.

---

### **3. Modélisation et validation avec Pydantic (≈ 1h15)**

**Objectifs :** définir des schémas de données et valider les entrées.

* Introduction à Pydantic (`BaseModel`)
* Typage et validation automatique
* Gestion des erreurs de validation
* Documentation automatique Swagger (`/docs`) et ReDoc (`/redoc`)

**Exemple :**

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    quantity: int = 0

@app.post("/product/")
def add_product(produit: Product):
    return {"product": product}
```

**Exercice :**

* Créer un modèle `User` avec champs : `name`, `email`, `age`
* Implémenter une route POST `/user/` pour enregistrer un utilisateur et retourner un message de confirmation.

---

## **Après-midi – Travaux pratiques : mini API complète**

### **TP : API d'analyse de données (≈ 3h à 3h30)**

**Objectif général :**
Mettre en pratique les notions vues le matin en créant une API complète qui expose des fonctions d'analyse ou de calcul.

#### **1. Cahier des charges**

Créer une API offrant les fonctionnalités suivantes :

* Endpoint `/analyse/` : reçoit une liste de nombres et renvoie moyenne, médiane et variance.
* Endpoint `/comparaison/` : compare deux ensembles de données et indique lequel a la plus grande moyenne.
* Endpoint `/dataset/{nom}` : enregistre un ensemble de données nommé en mémoire.

#### **2. Structure du projet**

```
tp_fastapi/
├── main.py
├── models.py
├── utils.py
└── requirements.txt
```

#### **3. Étapes de développement**

* Implémenter les calculs statistiques dans `utils.py`

  ```python
  from statistics import mean, median, variance

  def analys_data(data: list[float]) -> dict:
      return {
          "mean": mean(data),
          "median": median(data),
          "variance": variance(data)
      }
  ```
* Créer les modèles Pydantic dans `models.py`

  ```python
  from pydantic import BaseModel
  from typing import List

  class DataRequest(BaseModel):
      values: List[float]
  ```
* Définir les routes FastAPI dans `main.py`

  ```python
  from fastapi import FastAPI
  from models import DataRequest
  from utils import analys_data

  app = FastAPI()

  @app.post("/analys/")
  def analys(data: DataRequest):
      return analys_data(data.values)
  ```

#### **4. Tests et validation**

* Utiliser Swagger UI (`http://127.0.0.1:8000/docs`)
* Envoyer des requêtes JSON :

  ```json
  {
    "valeurs": [2, 4, 6, 8]
  }
  ```
* Vérifier le retour JSON des statistiques calculées.

#### **5. Extensions possibles**

* Enregistrer les ensembles de données dans un dictionnaire global
* Gérer la persistance via un fichier JSON ou une base SQLite
* Ajouter un endpoint `/datasets` listant les ensembles enregistrés

---

## Evaluation méthode

Créez un devoir dans Teams et donner ce devoir à rendre soit sur la demi-journée, soit plus tard, pas plus d'une semaine pour le rendre.

Faire un QCM de rattrapage.