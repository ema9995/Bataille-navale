import streamlit as st
import random

# Création de la grille
taille_grille = 5
grille = [["O" for _ in range(taille_grille)] for _ in range(taille_grille)]

# Placement du bateau
bateau_x = random.randint(0, taille_grille - 1)
bateau_y = random.randint(0, taille_grille - 1)

# Fonction d'affichage de la grille
def afficher_grille():
    return "\n".join([" ".join(ligne) for ligne in grille])

# Fonction d'indice
def donner_indice(x, y):
    if abs(x - bateau_x) <= 1 and abs(y - bateau_y) <= 1:
        return "Le bateau est à proximité !"
    elif x == bateau_x or y == bateau_y:
        return "Le bateau est sur la même ligne ou colonne, essaye encore !"
    else:
        return "Le bateau est plus loin, essaie une autre zone."

# Fonction de jeu
def jeu():
    essais = 0
    trouve = False

    # Affichage du jeu
    st.title("Mini Bataille Navale avec indices")
    st.write("Devine où se cache le bateau (grille 5x5).")
    st.text(afficher_grille())

    # Entrées utilisateur pour les coordonnées
    x = st.number_input("Choisis une colonne (1-5) : ", min_value=1, max_value=5)
    y = st.number_input("Choisis une ligne (1-5) : ", min_value=1, max_value=5)

    # Vérification des coordonnées
    if st.button("Tirer"):
        essais += 1
        x -= 1  # Conversion en index 0-based
        y -= 1  # Conversion en index 0-based

        if x == bateau_x and y == bateau_y:
            st.write(f"Bravo ! Tu as trouvé le bateau en {essais} essais.")
            grille[y][x] = "X"
            st.text(afficher_grille())
            trouve = True
        else:
            if grille[y][x] == "O":
                grille[y][x] = "-"
                st.write("Manqué !")
            else:
                st.write("Tu as déjà tiré ici.")
            
            # Donner un indice
            indice = donner_indice(x, y)
            st.write(indice)

        if trouve:
            st.button("Recommencer", on_click=recommencer)

# Fonction pour recommencer
def recommencer():
    global grille, bateau_x, bateau_y
    grille = [["O" for _ in range(taille_grille)] for _ in range(taille_grille)]
    bateau_x = random.randint(0, taille_grille - 1)
    bateau_y = random.randint(0, taille_grille - 1)
    jeu()

# Lancement du jeu
if __name__ == "__main__":
    jeu()
