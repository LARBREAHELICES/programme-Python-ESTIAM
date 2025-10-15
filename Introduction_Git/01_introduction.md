# **Git : installation, configuration et commandes de base**

---

## **1. Introduction à Git**

**Git** est un **système de gestion de versions décentralisé**.
Il permet de :

* Sauvegarder les différentes versions d’un projet.
* Travailler à plusieurs sans écraser le travail des autres.
* Revenir à un état antérieur si nécessaire.

Git est aujourd’hui l’outil standard du développement (logiciels, IA, web, etc.).

---

## **2. Installation de Git**

### **Windows**

1. Télécharge Git depuis [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Lance l’installeur, laisse les options par défaut.
3. Vérifie l’installation dans PowerShell :

   ```bash
   git --version
   ```

### **macOS**

```bash
brew install git
git --version
```

### **Linux (Debian/Ubuntu)**

```bash
sudo apt update
sudo apt install git -y
git --version
```

---

## **3. Configuration initiale**

Avant d’utiliser Git, configure ton identité :

```bash
git config --global user.name "Ton Nom"
git config --global user.email "ton.email@example.com"
```

Vérifie la configuration :

```bash
git config --list
```

---

## **4. Créer un dépôt Git**

### **Initialiser un dépôt dans un dossier existant**

```bash
git init
```

Cela crée un dossier caché `.git` contenant l’historique du projet.
Tu peux le voir avec :

```bash
ls -a
```

---

## **5. Suivre les fichiers**

### **Ajouter un fichier au suivi**

```bash
git add fichier.py
```

### **Ajouter tous les fichiers**

```bash
git add .
```

---

## **6. Enregistrer les modifications**

### **Créer un commit**

Un **commit** est un enregistrement du projet à un instant donné.

```bash
git commit -m "Premier commit : ajout du fichier principal"
```

---

## **7. Consulter l’état du dépôt**

### **Voir les fichiers modifiés**

```bash
git status
```

### **Voir l’historique des commits**

```bash
git log
```

Exemple :

```
commit 3a9e8c4f2b
Author: Alice <alice@example.com>
Date:   Tue Oct 15 10:00:00 2025
    Ajout du module de calcul
```

### **Voir un résumé condensé**

```bash
git log --oneline
```

---

## **8. Exemple de cycle complet**

```bash
mkdir projet_git
cd projet_git
git init
echo "print('Hello, Git!')" > main.py
git add main.py
git commit -m "Premier commit : création de main.py"
git log --oneline
```

---

## **9. Bonnes pratiques**

1. Toujours écrire un message de commit clair et concis.
2. Commiter souvent (une fonctionnalité = un commit).
3. Ne jamais commiter des fichiers générés (`.venv/`, `__pycache__/`, etc.).
4. Ajouter un fichier `.gitignore` :

   ```bash
   echo ".venv/" >> .gitignore
   git add .gitignore
   git commit -m "Ajout du fichier .gitignore"
   ```

---

## **Exercices**

1. Installer Git et le configurer.
2. Créer un dossier `projet_test` et initialiser un dépôt (`git init`).
3. Ajouter un fichier `main.py` et le commiter.
4. Modifier le fichier, puis exécuter `git status`, `git add`, `git commit`.
5. Consulter l’historique avec `git log`.

---

# **Chapitre 2 – Travailler avec les branches**

---

## **1. Qu’est-ce qu’une branche ?**

Une **branche** est une **copie parallèle** de ton projet.
Elle permet de développer une nouvelle fonctionnalité **sans modifier la version principale**.

La branche principale s’appelle souvent :

* `main` (moderne)
* ou `master` (ancien nom)

---

## **2. Créer une branche**

```bash
git branch nouvelle_fonction
```

Lister les branches :

```bash
git branch
```

Exemple :

```
* main
  nouvelle_fonction
```

L’étoile indique la branche active.

---

## **3. Changer de branche**

```bash
git checkout nouvelle_fonction
```

Depuis Git 2.23, tu peux utiliser la nouvelle syntaxe :

```bash
git switch nouvelle_fonction
```

---

## **4. Fusionner une branche**

Reviens sur la branche principale :

```bash
git switch main
```

Puis fusionne :

```bash
git merge nouvelle_fonction
```

Si tout se passe bien :

```
Fast-forward
 main.py | 2 ++
 1 file changed, 2 insertions(+)
```

---

## **5. Supprimer une branche**

Une fois fusionnée :

```bash
git branch -d nouvelle_fonction
```

---

## **6. Gérer les conflits**

Un **conflit** survient quand deux branches modifient la même ligne.
Git marque le conflit dans le fichier :

```text
<<<<<<< HEAD
print("Version principale")
=======
print("Version expérimentale")
>>>>>>> nouvelle_fonction
```

Tu dois **choisir** la version à conserver,
puis exécuter :

```bash
git add main.py
git commit -m "Résolution de conflit"
```

---

## **7. Exemple complet**

```bash
git switch -c dev          # crée et bascule sur dev
echo "print('Test dev')" >> test.py
git add test.py
git commit -m "Ajout de test.py sur la branche dev"
git switch main
git merge dev
git branch -d dev
```

---

## **8. Bonnes pratiques avec les branches**

| Objectif                 | Branche typique    |
| ------------------------ | ------------------ |
| Version stable du projet | `main`             |
| Nouvelle fonctionnalité  | `feature/...`      |
| Correction d’un bug      | `fix/...`          |
| Expérimentations         | `dev` ou `sandbox` |

---

## **Exercices**

1. Créer une branche `feature-message` et y ajouter un fichier `message.py`.
2. Modifier le contenu, le commiter, puis fusionner dans `main`.
3. Créer une branche `fix-bug` qui modifie la même ligne qu’une autre branche pour provoquer un conflit, puis le résoudre.
4. Supprimer les branches après fusion.
