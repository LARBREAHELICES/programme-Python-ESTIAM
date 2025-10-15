# **1. Introduction et installation**

FastAPI est un framework Python moderne pour la création d’**API web rapides, typées et asynchrones**.
Il repose sur des standards robustes : **OpenAPI**, **Pydantic** et **Starlette**.

---

### **Principes de FastAPI**

* **Asynchrone et performant** : construit sur `asyncio` et le serveur `uvicorn` (ASGI), il supporte les requêtes simultanées de façon efficace.
* **Typé** : s’appuie sur les annotations de type Python pour la validation et la documentation automatique.
* **Auto-documenté** : génère automatiquement une documentation Swagger à l’adresse `/docs`.
* **Facile à tester et à maintenir** : structure claire, intégration avec `pytest`.

---

### **Comparaison avec Flask et Django**

| Critère            | Flask                 | Django                 | FastAPI                      |
| ------------------ | --------------------- | ---------------------- | ---------------------------- |
| Type               | Micro-framework       | Framework complet      | Framework API                |
| Asynchrone         | Non (sauf extensions) | Partiel                | Oui (ASGI natif)             |
| Typage             | Non                   | Non                    | Oui (Pydantic)               |
| Documentation auto | Non                   | Non                    | Oui                          |
| Cas d’usage        | Petites APIs          | Applications complexes | APIs modernes, microservices |

FastAPI se situe entre la simplicité de Flask et la puissance de Django.
Il est idéal pour :

* des **microservices**,
* des **projets IA / Data** exposant des modèles,
* ou des **APIs REST** performantes.

---

### **Installation et configuration de l’environnement**

Créer un environnement virtuel :

```bash
python -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows
```

Installer les dépendances principales :

```bash
pip install fastapi uvicorn pydantic requests
```

Structure de projet recommandée :

```
app/
│
├── main.py
├── routers/
│   └── __init__.py
├── models/
│   └── __init__.py
└── tests/
    └── __init__.py
```

* `main.py` : point d’entrée de l’application.
* `routers/` : regroupe les routes par domaine fonctionnel.
* `models/` : contient les schémas de données (`Pydantic` ou ORM).
* `tests/` : tests unitaires (Pytest).

---

### **Premier serveur local**

Créons un fichier `main.py` :

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur FastAPI"}
```

Démarrer le serveur :

```bash
uvicorn main:app --reload
```

Sortie attendue :

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

Dans le navigateur :

* **[http://127.0.0.1:8000](http://127.0.0.1:8000)** → affiche `{"message": "Bienvenue sur FastAPI"}`
* **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** → interface Swagger
* **[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)** → documentation alternative ReDoc

---

### **Objectif de la séquence**

À ce stade, vous devez :

* savoir installer et lancer un serveur FastAPI,
* comprendre le rôle de `FastAPI()` et `uvicorn`,
* être capable d’exposer une première route simple.

---

# **2. Structure d’une application FastAPI**

Une application FastAPI repose sur des **routes** (ou *endpoints*) associées à des **fonctions Python**.
Chaque route définit une méthode HTTP (`GET`, `POST`, etc.) et une URL.

---

### **Création de l’objet principal**

Toute application commence par l’instanciation de FastAPI :

```python
from fastapi import FastAPI

app = FastAPI(title="Exemple API", version="1.0.0")
```

---

### **Définition des routes**

Une route est définie par un **décorateur** correspondant à une méthode HTTP :

```python
@app.get("/hello")
def say_hello():
    return {"message": "Hello, world!"}
```

Autres méthodes disponibles :

```python
@app.post("/users")
def create_user():
    pass

@app.put("/users/{id}")
def update_user(id: int):
    pass

@app.delete("/users/{id}")
def delete_user(id: int):
    pass
```

Les fonctions associées peuvent :

* renvoyer un dictionnaire Python (automatiquement converti en JSON),
* recevoir des paramètres de requête (`query`), de chemin (`path`) ou de corps (`body`).

---

### **Exemple avec paramètres**

```python
@app.get("/greet/{name}")
def greet(name: str, age: int = 0):
    return {"message": f"Bonjour {name}", "age": age}
```

Test :

```
GET /greet/Alice?age=25
→ {"message": "Bonjour Alice", "age": 25}
```

---

### **Organisation modulaire**

Pour les projets de taille moyenne à grande, il est conseillé de séparer les routes dans des modules dédiés :

**app/main.py**

```python
from fastapi import FastAPI
from app.routers import users

app = FastAPI()
app.include_router(users.router)
```

**app/routers/users.py**

```python
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def list_users():
    return [{"name": "Alice"}, {"name": "Bob"}]
```

Cette structure permet :

* d’ajouter ou retirer facilement des modules,
* de mieux isoler la logique métier,
* et d’éviter les fichiers trop volumineux.

---

### **Bonnes pratiques**

* **Typage strict** des paramètres et retours (favorise l’autocomplétion et la validation automatique).
* **Nommage cohérent** : routes en anglais, ressources au pluriel (`/users`, `/products`).
* **Indentation claire** (4 espaces par niveau).
* **Commentaires** uniquement sur la logique métier, pas sur la syntaxe évidente.

---

### **Exercice**

Créer un projet minimal `app/` contenant :

* un fichier `main.py` avec un objet `FastAPI()`,
* une route `/hello` renvoyant :

  ```json
  {"message": "Hello, [votre nom] !"}
  ```

Lancer le serveur avec `uvicorn main:app --reload`
et tester les URLs suivantes :

* `/hello`
* `/docs`


# **3. Schémas de données et validation avec Pydantic**

FastAPI repose sur **Pydantic** pour la **validation automatique** et la **sérialisation** des données.
Les modèles Pydantic décrivent la forme, le type et les contraintes des données échangées entre le client et l'API.

---

### **3.1. Définition de modèles de données avec `BaseModel`**

Chaque modèle de données hérite de `pydantic.BaseModel`.
Les annotations de type déterminent la validation automatique.

**Exemple :**

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
```

Une route FastAPI peut ensuite utiliser ce modèle comme paramètre d'entrée :

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users/")
def create_user(user: User):
    return {"message": f"Utilisateur {user.name} créé", "data": user}
```

Lorsqu'un client envoie un JSON, FastAPI :

* valide les types (`id` doit être un entier, `email` une chaîne),
* rejette les entrées invalides avec une erreur `422 Unprocessable Entity`,
* convertit automatiquement les données en instance `User`.

---

### **3.2. Validation automatique des entrées utilisateur**

Si la requête contient des données incorrectes :

```json
{
  "id": "abc",
  "name": 123
}
```

FastAPI répond :

```json
{
  "detail": [
    {
      "loc": ["body", "id"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

→ La validation est entièrement gérée par Pydantic, sans code supplémentaire.

---

### **3.3. Champs optionnels, valeurs par défaut, alias et contraintes (`Field`)**

#### Champs optionnels

```python
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None
```

#### Valeurs par défaut

```python
class User(BaseModel):
    name: str
    active: bool = True
```

#### Contraintes avec `Field`

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)
    in_stock: bool = True
```

Les arguments `min_length`, `gt` (*greater than*), `lt`, etc. permettent de restreindre les valeurs acceptées.

#### Alias

Permet de recevoir une clé différente du nom du champ :

```python
class User(BaseModel):
    full_name: str = Field(..., alias="fullName")
```

---

### **3.4. Sérialisation et transformation en JSON**

Les objets Pydantic peuvent être convertis facilement :

```python
product = Product(name="Laptop", price=999.99)
print(product.dict())   # {'name': 'Laptop', 'price': 999.99, 'in_stock': True}
print(product.json())   # JSON string
```

FastAPI utilise automatiquement cette sérialisation pour renvoyer les réponses JSON.

---

### **3.5. Exemple complet : modèle `User`**

```python
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=20)
```

```python
@app.post("/register")
def register(user: User):
    return {"message": f"Utilisateur {user.name} enregistré avec succès."}
```

La validation est automatique :

* un email invalide ou un mot de passe trop court provoque une erreur `422`.

---

### **Exercice**

Créer un modèle `Product` avec :

* `name: str` (non vide, longueur minimale 2)
* `price: float` (strictement positif)
* `in_stock: bool` (valeur par défaut `True`)

Créer ensuite une route `POST /products/` qui :

* reçoit un `Product` en JSON,
* renvoie le produit validé sous forme de dictionnaire.

Tester avec différentes valeurs invalides (prix négatif, nom vide).

---

# **4. Gestion des erreurs et des statuts HTTP**

Une API doit informer clairement le client des **succès** et des **échecs**.
FastAPI facilite cette gestion via les codes de statut et les exceptions HTTP.

---

### **4.1. Codes de statut HTTP**

Les plus courants :

| Code | Signification         | Exemple d'usage                  |
| ---- | --------------------- | -------------------------------- |
| 200  | OK                    | Requête réussie                  |
| 201  | Created               | Création d'une ressource         |
| 204  | No Content            | Suppression réussie              |
| 400  | Bad Request           | Erreur de validation côté client |
| 404  | Not Found             | Ressource introuvable            |
| 500  | Internal Server Error | Erreur côté serveur              |

**Exemple :**

```python
from fastapi import status

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item():
    return {"message": "Créé avec succès"}
```

---

### **4.2. Gestion des erreurs avec `HTTPException`**

`HTTPException` permet de renvoyer une erreur explicite avec un code et un message.

**Exemple :**

```python
from fastapi import HTTPException

@app.get("/products/{product_id}")
def read_product(product_id: int):
    if product_id != 1:
        raise HTTPException(
            status_code=404,
            detail=f"Produit {product_id} introuvable"
        )
    return {"id": 1, "name": "Laptop"}
```

Réponse :

```json
{
  "detail": "Produit 42 introuvable"
}
```

---

### **4.3. Réponses personnalisées**

FastAPI permet de structurer les messages d'erreur avec des détails supplémentaires.

```python
from fastapi.responses import JSONResponse

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id < 0:
        return JSONResponse(
            status_code=400,
            content={"error": "L'ID doit être positif"}
        )
    return {"id": user_id, "name": "Alice"}
```

---

### **4.4. Middleware et hooks**

Les **middlewares** permettent d'intercepter les requêtes et réponses pour :

* journaliser les appels,
* vérifier les permissions,
* mesurer les temps d'exécution.

**Exemple :**

```python
from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Requête : {request.method} {request.url}")
    response = await call_next(request)
    print(f"Réponse : {response.status_code}")
    return response
```

---

### **4.5. Bonnes pratiques**

* Utiliser des **codes HTTP cohérents** (`404` pour une ressource absente, pas `400`).
* Renvoyer des messages clairs et structurés (`{"error": "Détail du problème"}`).
* Préférer les **exceptions explicites** à des retours de dictionnaires “erreur”.

---

### **Exercice**

1. Ajouter une route `GET /products/{id}`.

   * Si `id` ≠ 1, lever une `HTTPException(404, "Produit introuvable")`.
   * Sinon, retourner un dictionnaire contenant le produit.

2. Ajouter un **middleware** qui affiche dans la console :

   * la méthode HTTP,
   * l'URL appelée,
   * et le code de statut renvoyé.

3. Tester plusieurs appels à `/products/{id}` pour observer le comportement des logs et des erreurs.

---

# **5. Méthodes HTTP et opérations CRUD**

Les API REST reposent sur les **méthodes HTTP** pour manipuler les ressources.
FastAPI simplifie leur implémentation en associant chaque méthode à un décorateur.

---

### **5.1. Rappels sur les méthodes HTTP**

| Méthode  | Description                 | Exemple d’usage          |
| -------- | --------------------------- | ------------------------ |
| `GET`    | Lecture d’une ressource     | Lire un utilisateur      |
| `POST`   | Création d’une ressource    | Ajouter un utilisateur   |
| `PUT`    | Mise à jour complète        | Modifier un utilisateur  |
| `DELETE` | Suppression d’une ressource | Supprimer un utilisateur |

---

### **5.2. Simulation d’une base de données**

Pour les démonstrations, on peut simuler une base avec une simple **liste en mémoire**.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users_db = []  # simulation de base
```

---

### **5.3. CRUD complet**

**Créer un utilisateur (POST)**

```python
@app.post("/users", status_code=201)
def create_user(user: User):
    users_db.append(user)
    return {"message": "Utilisateur ajouté", "user": user}
```

**Lire tous les utilisateurs (GET)**

```python
@app.get("/users")
def list_users():
    return users_db
```

**Supprimer un utilisateur (DELETE)**

```python
@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    for u in users_db:
        if u.id == user_id:
            users_db.remove(u)
            return
    raise HTTPException(status_code=404, detail="Utilisateur introuvable")
```

---

### **Exercice**

Créer une API `/users` permettant :

* d’ajouter un utilisateur avec `POST /users`,
* de consulter la liste avec `GET /users`,
* de supprimer un utilisateur via `DELETE /users/{id}`.

Tester les réponses avec des outils comme **curl**, **HTTPie**, ou **Swagger UI** (`/docs`).

---

# **6. Gestion des dépendances et modularisation**

Les dépendances permettent d’injecter des composants réutilisables dans les routes (ex. connexion DB, authentification).
FastAPI propose pour cela le décorateur **`Depends()`**.

---

### **6.1. Utilisation du décorateur `Depends`**

```python
from fastapi import Depends

def get_settings():
    return {"debug": True}

@app.get("/config")
def read_config(settings: dict = Depends(get_settings)):
    return settings
```

Ici, `get_settings()` est exécutée à chaque appel, et son résultat injecté dans `read_config()`.

---

### **6.2. Organisation avec `APIRouter`**

Pour structurer le projet, on définit des routes dans des modules séparés.

**app/routers/users.py**

```python
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def list_users():
    return [{"name": "Alice"}, {"name": "Bob"}]
```

**app/main.py**

```python
from fastapi import FastAPI
from app.routers import users

app = FastAPI()
app.include_router(users.router)
```

Cette modularisation améliore la lisibilité et la maintenance du code.

---

### **Exercice**

* Créer deux modules : `routers/users.py` et `routers/products.py`.
* Chaque module expose un endpoint `GET /` renvoyant une liste fictive.
* Les importer dans `main.py` via `APIRouter` et `include_router()`.

---

# **7. Intégration avec une base de données (approche légère)**

FastAPI s’intègre facilement avec des ORM comme **SQLModel** ou **SQLAlchemy**.
Voici une approche simple utilisant **SQLite** et **SQLModel** (orientée FastAPI).

---

### **7.1. Installation**

```bash
pip install sqlmodel
```

---

### **7.2. Définition du modèle et de la base**

```python
from sqlmodel import SQLModel, Field, Session, create_engine, select

class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: float
    in_stock: bool = True

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)
```

---

### **7.3. Routes pour création et lecture**

```python
@app.post("/products")
def add_product(product: Product):
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product

@app.get("/products")
def get_products():
    with Session(engine) as session:
        products = session.exec(select(Product)).all()
        return products
```

---

### **Exercice**

1. Créer une base SQLite `database.db` avec une table `Product`.
2. Ajouter une route `POST /products` pour insérer un produit.
3. Ajouter une route `GET /products` pour retourner la liste complète.
4. Tester les requêtes via Swagger UI.

---

# **8. Documentation automatique et OpenAPI**

FastAPI génère automatiquement une documentation interactive conforme à la spécification **OpenAPI**.
Elle décrit les routes, les paramètres et les modèles.

---

### **8.1. Accès à la documentation**

Deux interfaces sont disponibles :

* **Swagger UI** : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc** : [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Aucune configuration n’est nécessaire : tout est généré automatiquement.

---

### **8.2. Métadonnées personnalisées**

On peut enrichir la documentation lors de la création de l’application :

```python
app = FastAPI(
    title="API Produits",
    description="Exemple d'API FastAPI pour la gestion de produits.",
    version="1.0.0",
    contact={
        "name": "Equipe Formation",
        "email": "formation@example.com",
    },
    license_info={"name": "MIT"}
)
```

Les métadonnées s’affichent dans Swagger UI.

---

### **8.3. Description automatique des schémas**

Les modèles `Pydantic` définis dans le code sont automatiquement documentés :

* Types des champs (`str`, `float`, `bool`)
* Contraintes (`min_length`, `gt`, etc.)
* Champs obligatoires ou optionnels

---

### **Exercice**

* Modifier le titre et la description de votre application FastAPI.
* Vérifier dans `/docs` que les informations s’affichent correctement.
* Ajouter un champ `license_info` et un contact.

---

# **9. Tests automatisés d’API avec Pytest et HTTPX**

Les tests garantissent la fiabilité des endpoints et préviennent les régressions.
FastAPI s’intègre naturellement à `pytest` via le **TestClient** intégré.

---

### **9.1. Installation**

```bash
pip install pytest httpx
```

---

### **9.2. Création d’un client de test**

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
```

---

### **9.3. Exemple de test simple**

```python
def test_read_root():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
```

---

### **9.4. Tests CRUD**

```python
def test_create_user():
    user = {"id": 1, "name": "Alice", "email": "alice@example.com"}
    response = client.post("/users", json=user)
    assert response.status_code == 201
    assert response.json()["user"]["name"] == "Alice"

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code in [204, 404]
```

---

### **9.5. Tests paramétrés et exceptions**

```python
import pytest

@pytest.mark.parametrize("price", [10.0, 0.0, -5.0])
def test_product_price(price):
    response = client.post("/products", json={"name": "Item", "price": price})
    if price > 0:
        assert response.status_code == 200
    else:
        assert response.status_code == 422
```

---

### **9.6. Organisation du dossier de tests**

Structure recommandée :

```
app/
├── main.py
├── routers/
│   └── users.py
└── tests/
    ├── __init__.py
    └── test_users.py
```

Les tests peuvent être lancés simplement :

```bash
pytest -v
```

---

### **Exercices**

1. Écrire des tests pour les routes CRUD `/users`.

   * Vérifier les statuts de retour (`201`, `200`, `404`).
2. Tester la validation de `Product` (`price > 0`).
3. Organiser vos tests dans un dossier `tests/` et exécuter `pytest -v`.
