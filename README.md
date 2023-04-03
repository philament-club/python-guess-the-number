# 🎲 Guess the Number !

Une introduction ludique à la programmation en Python par le biais d'un jeu simple: deviner un nombre.

## 📜 Règles du jeu

- Un nombre est tiré au hasard entre 1 et 100.
- Le joueur doit deviner le nombre en question.
  - Si la valeur donnée n'est pas bonne, on affiche un indice, comme *"plus"* ou *"moins"*.
  - 5 essais maximum!

## 🧠 Objectifs d'apprentissage

- Import de modules.
- Créer une fonction.
- Définir et manipuler des variables.
- Types de données (et se méfier des inputs!).
- Branches (`if`/`elif`/`else`).
- Boucles (`while`).

## 👀 Notice de consultation

**SPOILER ALERT!** Ne consultez le code que si vous ne voulez pas résoudre le problème par vous-même, ou si vous êtes bloqué...

Il existe plusieurs méthodes pour visualiser le code de ce projet...

- [Consulter la version "annotée" générée à partir du code source](https://philament-club.github.io/python-guess-the-number/annotated-sources/v1-simple/main.html) (le mieux et le plus didactique!) ;
- [*via* l'interface de GitHub](./v1-simple/main.py) (le plus facile) ;
- En local, *via* votre éditeur de texte préféré (si vous avez cloné ce repository).

## ⏩ Feuille de route / évolutions possibles

***« Faire de grandes choses à partir de petits riens »***

Pour l'instant, seule une "v1" minimaliste est implémentée et commentée,
et devrait déjà pouvoir servir de bonne base.

On peut imaginer au fil du temps rajouter des fonctionnalités, comme par exemple :
- un tableau des 5 meilleurs scores
- la possibilité de changer la plage [1..100]
- la possibilité de changer le nombre d'essais

L'idée est d'avoir une base et de montrer comment on peut la faire évoluer,
quitte à lui faire changer son "média":
- sous forme de "TUI" *via* [Rich](https://github.com/Textualize/rich)          
- sous forme de "GUI" *via* `tkinter` (lol)
- sous forme de "jeu" *via* PyGame
- sous forme de page web (auquel cas on passe à l'étape logique suivante:
  découvrir un nouveau monde! [server-side! HTML5! JavaScript!]).
