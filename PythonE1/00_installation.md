---
marp: true
theme: default
paginate: true
size: 16:9
---

# Stacks

*Lisez bien tout pour choisir une méthode d'installation*

1. **Télécharger Python**
2. **Environnement virtuel**
3. **Jupyter & JupyterLab**
4. **Alternative : Google Colab**

---

# DataOps — Cours

Cours complet :  
[https://antoine07.github.io/dataops_estiam/](https://antoine07.github.io/dataops_estiam/)

---

# Télécharger Python

Téléchargez la dernière version :  
[python.org/downloads](https://www.python.org/downloads/)

![w:600](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

---

# Créer un environnement virtuel

```bash
python -m venv env_dataops
````

Activez-le selon votre système :

**Windows**

```bash
env_dataops\Scripts\activate
```

**Mac / Linux**

```bash
source env_dataops/bin/activate
```

---

# Installer Jupyter et JupyterLab

![w:100](https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg)

```bash
pip install --upgrade pip
pip install notebook jupyterlab
```

Lancez JupyterLab :

```bash
jupyter lab
```

Pour sortir :

```bash
deactivate
```

# Organisation de travail avec la virtualisation

```txt
project_data/
│
├── env_dataops/          ←  environnement virtuel
│
├── requirements.txt      ← liste des dépendances du projet
├── main.py               ← point d'entrée principal du programme
│
├── mon_projet/           ← dossier du code source (ton “package”)
│   ├── models/           ← tes classes ou structures de données
│   │   └── user.py
│   └── utils/            ← fonctions utilitaires
│       └── helpers.py
│
└── tests/                ← tes fichiers de test
    └── test_user.py
```

---

# En cas de problème d'installation

Alternative en ligne sans installation : [Google Colab](https://colab.research.google.com)

---

# Alternative Docker

Si vous êtes à l'aise avec Docker, vous pouvez suivre cette installation.
Elle remplace la méthode précédente.

![w:150](https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png)

---
