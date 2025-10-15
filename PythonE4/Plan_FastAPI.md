## **Développement d'API avec FastAPI**

### **1. Introduction et installation**

* Présentation du framework FastAPI et de ses principes (asynchrone, typé, performant).
* Comparaison avec Flask et Django : positionnement et usages.
* Installation et configuration de l'environnement :

  * `fastapi`, `uvicorn`, `pydantic`, `requests`
  * structure de projet (`app/`, `main.py`, `routers/`, `models/`, `tests/`)
* Lancement d'un premier serveur local avec `uvicorn main:app --reload`.

**Objectif :** comprendre l'architecture et exécuter une première route API.

---

### **2. Structure d'une application FastAPI**

* Création de l'objet principal `FastAPI()`.
* Définition de routes (`@app.get`, `@app.post`, `@app.put`, `@app.delete`).
* Syntaxe des endpoints et retour d'objets Python ou de modèles.
* Organisation du code : séparation en modules (`routers`, `schemas`, `models`).
* Bonnes pratiques : typage, indentation, gestion des dépendances.

**Exercice :**
Créer une API minimaliste exposant une route `/hello` renvoyant un message JSON personnalisé.

---

### **3. Schémas de données et validation avec Pydantic**

* Définition de modèles de données avec `BaseModel`.
* Validation automatique des entrées utilisateur.
* Champs optionnels, valeurs par défaut, alias et contraintes (`Field()`).
* Sérialisation et transformation d'objets en JSON.
* Exemple : modèle `User` avec validation d'email et longueur de mot de passe.

**Exercice :**
Créer un modèle `Product` avec les champs `name`, `price`, `in_stock`.
Valider que `price` soit positif et que `name` ne soit pas vide.

---

### **4. Gestion des erreurs et des statuts HTTP**

* Codes de statut (`200`, `201`, `400`, `404`, `500`, etc.).
* Gestion des erreurs avec `HTTPException`.
* Réponses personnalisées et messages d'erreur structurés.
* Middleware et hooks pour journalisation et sécurité.
* Bonnes pratiques : cohérence des statuts et messages explicites.

**Exercice :**
Modifier une route pour lever une `HTTPException` lorsque le produit demandé n'existe pas.

---

### **5. Méthodes HTTP et opérations CRUD**

* Rappels sur les méthodes HTTP : `GET`, `POST`, `PUT`, `DELETE`.
* Mise en œuvre d'un CRUD complet sur une ressource (`User`, `Product`, etc.).
* Simulation de base de données avec une liste ou un dictionnaire Python.
* Retour de listes, d'objets uniques, ou de statuts (`Response`, `status_code`).

**Exercice :**
Créer une API `/users` permettant :

* d'ajouter un utilisateur,
* de consulter la liste des utilisateurs,
* de supprimer un utilisateur par son identifiant.

---

### **6. Gestion des dépendances et modularisation**

* Utilisation du décorateur `Depends`.
* Injection de dépendances (connexion, configuration, sécurité).
* Organisation du code avec `APIRouter`.
* Modularisation : séparation des routes et des modèles.

**Exercice :**
Séparer les routes `/users` et `/products` dans deux modules indépendants et les importer via `APIRouter`.

---

### **7. Intégration avec une base de données (approche légère)**

* Introduction à SQLModel / SQLAlchemy (ou stockage en mémoire).
* Connexion à une base SQLite.
* Définition d'un modèle persistant (`User`, `Product`).
* Création et lecture via ORM.
* Notion de session et transaction.

**Exercice :**
Créer une base SQLite contenant des produits et exposer une route `/products` retournant le contenu de la table.

---

### **8. Documentation automatique et OpenAPI**

* Documentation interactive avec `/docs` (Swagger UI) et `/redoc`.
* Description automatique des paramètres, corps de requête, réponses.
* Personnalisation du titre, de la description et des métadonnées de l'API.
* Utilisation des annotations de type pour enrichir la documentation.

**Exercice :**
Personnaliser le titre et la description de l'API et vérifier la documentation interactive générée.

---

### **9. Tests automatisés d'API avec Pytest et HTTPX**

* Installation de `pytest` et `httpx`.
* Configuration d'un client de test pour FastAPI (`from fastapi.testclient import TestClient`).
* Tests unitaires et d'intégration sur les endpoints (`client.get`, `client.post`).
* Vérification des statuts et des contenus JSON.
* Organisation du dossier `tests/` pour un projet API.

**Exemple :**

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
```

**Exercices :**

* Écrire des tests pour les routes CRUD `/users`.
* Vérifier le retour des statuts (`201`, `404`) selon les cas.

---
