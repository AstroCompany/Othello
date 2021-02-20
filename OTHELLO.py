# importation
import pygame
import time
import PLATEAU
import GUI


pygame.init()
pygame.display.set_caption("Othello")
fenetre_menu = pygame.display.set_mode((800, 800)) # fenetre de l'écran du menu 
fenetre_menu.fill((24, 77, 71))



# menu = PLATEAU.Menu(fenetre_menu)
# menu.boucle_principale(fenetre_menu)
menu = GUI.Menu(fenetre_menu)
menu.boucle_principale()


# création du tableau ///////////////////////////
if menu.fin:
    tableau  = PLATEAU.Tableau()
    fenetre = tableau.creation_fenetre()
    tableau.dessine_tableau(fenetre)
    affichage = PLATEAU.GUI()

# boucle principale /////////

    if menu.etat == 3:
        tableau.boucle_principale_JvsJ(fenetre, tableau, affichage)

    if menu.etat == 4:
       tableau.boucle_principale_JvsIA(fenetre, tableau, affichage)

    if menu.etat == 5:
        tableau.boucle_principale_IAvsIA(fenetre, tableau, affichage)

# Creation de la fenetre de l'écran de victoire /

fenetre__victoire = pygame.display.set_mode((800, 800)) # fenetre de l'écran de victoire
fenetre_menu.fill((24, 77, 71))

ecran_victoire = GUI.Gagnant(tableau.gagnant, fenetre, tableau.gagnant)

ecran_victoire.affichage()