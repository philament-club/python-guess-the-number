# == Demande au joueur de deviner un nombre tiré au hasard. ==

# Import d'un générateur de nombres aléatoires
from random import randint


# === La fonction principale de notre petit jeu... ===
def jouer(max_essais=5, cheat=False):
    # 🎲 Nombre tiré au sort (entre 1 et 100)
    numero_gagnant = randint(1, 100)
    # 🧮 Compteur du nombre d'essais pour la partie
    n_essais = 1

    print(f"Devinez un nombre entre 1 et 100... Vous avez {max_essais} essais.")

    # 🥷 *(Petit argument pour faciliter les tests lors du développement...)*
    if cheat:
        print(f">>> {numero_gagnant}")

    # ==== Tant que la réponse n'a pas été trouvée et qu'il reste des essais... ====
    while n_essais <= max_essais:

        # - ⌨️ Demande au joueur de saisir une valeur...
        reponse = input(f"[{n_essais}/{max_essais}] Quel nombre proposez-vous ? ")

        # - ☑️ Tente de convertir la valeur saisie en nombre entier (`int`)
        try:
            reponse = int(reponse)
        # > ❗ *oops!* La valeur saisie ne ressemble pas à un entier!
        except ValueError:
            # > - affiche une erreur s'il ne s'agit pas d'une ligne vide
            if reponse:
                print(f'** "{reponse}" n\'est pas un nombre!')
            # > ℹ️ `continue` → "sort" de l'itération actuelle de la boucle `while` (nouvelle saisie)
            continue

        # - 🟰 Compare la valeur proposée à `numero_gagnant` et affiche un indice...
        if reponse < numero_gagnant:
            print("+ Plus!")
        elif reponse > numero_gagnant:
            print("- Moins!")
        else:
            if n_essais == 1:
                print("PERFECT!")
            else:
                print(f"BRAVO! Vous avez gagné en {n_essais} essais.")
            # > ℹ️ La partie est terminée... `return` nous permet de "quitter" la fonction `jouer`.
            return

        # - ➕ Incrémente le nombre d'essais actuel.
        n_essais += 1

        # - ⬆️ Si `n_essais` ≤ `max_essais`: rinse & repeat (`while` loop)...

    # 🛑 `n_essais` est égal à `max_essais`, la boucle `while` est terminée... *Game over!*
    print(f"Désolé, vous n'avez pas trouvé le numéro gagnant: {numero_gagnant}.")


# === Le point d'entrée de notre script lorsqu'il est appelé en ligne de commande... ===
if __name__ == '__main__':
    # ...se résume à appeler notre fonction `jouer`.
    jouer(cheat=True)
