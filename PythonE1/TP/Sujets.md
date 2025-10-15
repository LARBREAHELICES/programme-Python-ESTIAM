# **TP 1 – Jeu du Chifoumi (Pierre – Feuille – Ciseaux)**

---

## **Objectif du TP**

Créer un **jeu tour par tour** entre le joueur et l’ordinateur :
le classique **Chifoumi**, où chacun choisit *pierre*, *feuille* ou *ciseaux*,
et le gagnant est déterminé selon les règles du jeu.

L’objectif est de **mettre en pratique les conditions, les boucles et les fonctions**.

---

## **Consignes**

1. Le programme s’exécute en console.
2. Le joueur saisit son choix (`pierre`, `feuille`, `ciseaux`).
3. L’ordinateur choisit aléatoirement une des trois options.
4. Le programme affiche le choix de chacun et le résultat du tour :

   * Pierre bat Ciseaux
   * Ciseaux bat Feuille
   * Feuille bat Pierre
   * Égalité si les deux choix sont identiques
5. Le jeu se joue **en plusieurs manches** (ex. 3 ou 5 tours).
6. Le programme affiche le **score final** et le **vainqueur**.

---

## **Éléments attendus**

* Utilisation de `input()` et `print()`
* Boucle `while` ou `for` pour gérer plusieurs tours
* Fonctions pour organiser le code :

  * `get_user_choice()`
  * `get_computer_choice()`
  * `determine_winner()`
* Gestion des erreurs d’entrée (si le joueur tape autre chose)
* Utilisation du module `random` pour le choix de l’ordinateur

---

## **Améliorations possibles (bonus)**

* Ajouter un mode "meilleur des N manches"
* Sauvegarder les scores dans un fichier texte
* Créer un mini menu (nouvelle partie, quitter)

---

## **Objectif pédagogique**

* Revoir la **structure d’un programme complet**
* Maîtriser les **conditions imbriquées** et les **boucles**
* Introduire la **décomposition fonctionnelle**

---

# **TP 2 – Combat : Dragon vs Chevalier**

---

## **Objectif du TP**

Développer un **jeu de combat tour par tour** en console entre un **Chevalier** et un **Dragon**.

Chaque personnage possède des **points de vie**, une **attaque** et éventuellement une **défense**.
Le combat continue jusqu’à ce que l’un des deux atteigne 0 points de vie.

Ce TP permet de **mettre en pratique les classes et le polymorphisme**.

---

## **Consignes**

1. Créer deux classes :

   * `Knight` (chevalier)
   * `Dragon`
2. Chaque personnage a :

   * un nom
   * des points de vie (`hp`)
   * une force d’attaque (`attack`)
   * une méthode `attack_target(target)` qui inflige des dégâts
3. Les dégâts sont calculés de façon simple (par exemple, `attack - defense`).
4. Le combat se déroule tour par tour :

   * le joueur (chevalier) attaque d’abord
   * puis le dragon réplique
   * les points de vie sont affichés à chaque tour
5. Le combat s’arrête quand un des deux personnages meurt.
6. Le programme affiche le vainqueur à la fin.

---

## **Éléments attendus**

* Utilisation de **classes et méthodes**
* Gestion d’une **boucle principale de jeu**
* Conditions (`if`, `elif`, `else`) pour vérifier les points de vie
* Organisation claire du code :

  * `class Knight`
  * `class Dragon`
  * `main()` pour gérer le déroulement du combat

---

## **Extensions possibles (bonus)**

* Ajouter des coups spéciaux (attaque critique, défense, potion de soin)
* Permettre à l’utilisateur de choisir son action à chaque tour
* Ajouter une interface texte plus immersive (affichage stylisé, couleurs)
* Sauvegarder le résultat dans un fichier `scores.txt`

---

## **Objectif pédagogique**

* Comprendre la **programmation orientée objet** appliquée à un cas concret
* Manipuler les **attributs d’instance** et les **méthodes**
* Maîtriser la **logique de jeu tour par tour**
* Préparer la transition vers des projets structurés (API, jeux complets, etc.)
