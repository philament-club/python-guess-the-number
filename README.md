# 🎲 Guess the Number !

Ce projet a pour ambition d'être une introduction ludique au monde
de la programmation en Python, en partant d'un jeu simple: deviner un nombre.

## 📜 Règles du jeu

- Un nombre est tiré au hasard entre 1 et 100.
- Le joueur ou la joueuse doit deviner le nombre en question.
  - Si la valeur donnée n'est pas bonne, on affiche un indice,
    comme *plus* ou *moins*.
  - 5 essais maximum!

## 🧠 Objectifs d'apprentissage

- Import de modules (le générateur de nombres aléatoire).
- Créer une fonction.
- Définir et manipuler des variables.
- Types de données (et se méfier des inputs!).
- Comparaisons (`if`/`elif`/`else`).
- Boucles (`while`).

## 👀 Notice de consultation

## ⏩ Feuille de route / évolutions possibles

***« Faire de grandes choses à partir de petits riens »***

Pour l'instant, seule une "v1" minimaliste est implémentée et commentée,
et devrait déjà pouvoir servir de bonne base.

On peut imaginer au fil du temps rajouter des fonctionnalités, comme par exemple :
- pouvoir appuyer sur `q` pour quitter le jeu sans utiliser Ctrl+C
- un tableau des 5 meilleurs scores
- la possibilité de changer la plage [1..100]

L'idée est d'avoir une base et de montrer comment on peut la faire évoluer,
quitte à lui faire changer son "média":
- sous forme de mini jeu "graphique" via PyGame
- sous forme de page web (auquel cas on passe à l'étape logique suivante:
  découvrir un nouveau monde! [HTML5 et JavaScript]).