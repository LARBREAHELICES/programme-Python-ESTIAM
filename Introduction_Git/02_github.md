# **GitHub et le travail collaboratif (push, pull, PR)**

---

## **1. Introduction à GitHub**

**GitHub** est une plateforme en ligne basée sur Git.
Elle permet de :

* **héberger** des dépôts Git (projets),
* **collaborer** à plusieurs,
* **gérer** les versions et le code source.

Un dépôt GitHub est comme ton dépôt local,
mais **hébergé dans le cloud**, accessible à toute ton équipe.

---

## **2. Créer un compte GitHub**

1. Va sur [https://github.com](https://github.com)
2. Crée un compte gratuit (utilise ton adresse mail académique si possible).
3. Une fois connecté, clique sur **New Repository**.

Remplis :

* Repository name : `mon_projet`
* Cocher **Add a README.md**
* Choisir **Public** ou **Private**

Clique sur **Create repository**.

---

## **3. Lier ton dépôt local à GitHub**

Dans ton terminal (dans ton dossier Git déjà initialisé) :

```bash
git remote add origin https://github.com/<ton_nom>/mon_projet.git
```

Vérifie la configuration :

```bash
git remote -v
```

Tu devrais voir :

```
origin  https://github.com/ton_nom/mon_projet.git (fetch)
origin  https://github.com/ton_nom/mon_projet.git (push)
```

---

## **4. Envoyer ton projet sur GitHub**

### **Premier envoi :**

```bash
git push -u origin main
```

Le drapeau `-u` (upstream) relie la branche locale à celle du dépôt distant.

Pour les push suivants :

```bash
git push
```

---

## **5. Récupérer les modifications**

Si quelqu’un d’autre a modifié le dépôt distant :

```bash
git pull
```

Cette commande met à jour ta branche locale avec les dernières modifications GitHub.

---

## **6. Cloner un dépôt**

Pour récupérer un projet existant :

```bash
git clone https://github.com/ton_nom/mon_projet.git
```

Cela crée un dossier complet avec tout l’historique Git.

---

## **7. Workflow collaboratif typique**

1. Cloner ou forker un projet.
2. Créer une **branche** pour travailler sur une nouvelle fonctionnalité.
3. Commiter et **pousser la branche** sur GitHub.
4. Ouvrir une **Pull Request (PR)** pour demander la fusion.
5. L’équipe **revoit** le code avant de fusionner dans `main`.

---

## **8. Pull Requests (PR)**

Une **Pull Request** (ou **Merge Request** sur d’autres plateformes)
sert à **proposer une modification** dans le code d’un dépôt partagé.

### **Étapes**

1. Crée une nouvelle branche :

   ```bash
   git switch -c feature-readme
   ```
2. Modifie un fichier (ex : `README.md`) et commit :

   ```bash
   git add README.md
   git commit -m "Ajout de ma présentation"
   git push origin feature-readme
   ```
3. Sur GitHub, une bannière s’affiche :
   **“Compare & pull request” → clique dessus**
4. Ajoute un titre et une description claire :

   > "Ajout d’un paragraphe de présentation dans le README"
5. Clique sur **Create pull request**.

---

## **9. Revue et fusion d’une PR**

Une fois la PR créée :

* Les autres membres peuvent **commenter**, **proposer des changements**, ou **valider**.
* L’auteur peut mettre à jour sa branche :

  ```bash
  git add .
  git commit -m "Corrections suite à la revue"
  git push
  ```

Quand tout est bon :

* Le responsable clique sur **Merge pull request**
* Puis sur **Confirm merge**

Enfin, la branche peut être supprimée :

```bash
git branch -d feature-readme
git push origin --delete feature-readme
```

---

## **10. Bonnes pratiques GitHub**

| Action            | Bonne pratique                                        |
| ----------------- | ----------------------------------------------------- |
| Nom de branche    | court et explicite : `feature-login`, `fix-api-error` |
| Message de commit | clair et descriptif                                   |
| PR                | petite et ciblée (1 fonctionnalité à la fois)         |
| Collaboration     | commenter les PR avant de fusionner                   |
| README            | toujours à jour avec instructions d’installation      |

---

## **11. Exemple complet de cycle**

```bash
# Création du dépôt local
git init
echo "# Mon projet Python" > README.md
git add README.md
git commit -m "Initial commit"

# Lien avec GitHub
git remote add origin https://github.com/ton_nom/mon_projet.git
git push -u origin main

# Nouvelle branche
git switch -c feature-hello
echo "print('Hello, GitHub!')" > main.py
git add main.py
git commit -m "Ajout du script principal"
git push origin feature-hello
```

Puis sur GitHub :
→ Ouvrir une **Pull Request** → **Merge** → **Supprimer la branche**.

---

## **12. Exercice**

1. Créer un dépôt GitHub `demo_git`.
2. Lier un dépôt local et y pousser un premier commit.
3. Créer une branche `feature-message`, ajouter un fichier `message.py`, et faire un `push`.
4. Ouvrir une **Pull Request** sur GitHub.
5. Fusionner la PR et supprimer la branche.

---

## **13. Aller plus loin**

* Authentification SSH :

  ```bash
  ssh-keygen -t ed25519 -C "ton.email@example.com"
  ```

  Puis ajouter ta clé publique sur GitHub (Settings → SSH and GPG keys).

* Collaborer via **forks** (contribution à des projets open source).

* Gérer plusieurs **remotes** (`origin`, `upstream`).
