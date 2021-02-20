# Pour le bon fonctionnement de notre jeu le module Pygame doit être installer
# Documentation: https://www.pygame.org/docs/
# De plus si le jeu est lancé a partir de VScode tout le dossier doit être ouvert sous peine de disfonctionnements
# Mettre message optimisation dans règles du jeu

# importation
import pygame
import time
import random

# creation de la classe Tableau
class Tableau:

    def __init__(self):

        self.window_width = 1400
        self.window_eight = 1000
        self.width = 1000
        self.height = 1000
        self.colonne = 8
        self.ligne = 8
        self.couleur_ligne = (0, 175, 145)
        self.bg_color = (24, 77, 71)
        self.circle_radius = 50
        self.circle_width = 50
        self.pion_noir = (34, 40, 49)
        self.pion_blanc = (221, 221, 221)
        self.grille = [[0 for _ in range(self.ligne)] for _ in range(self.colonne)]
        self.directions = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
        self.gagnant = ""
        self.fin = False

        self.grille[3][3] = 2
        self.grille[3][4] = 1
        self.grille[4][3] = 1
        self.grille[4][4] = 2
    
    def creation_fenetre(self):
        pygame.init()

        pygame.display.set_caption("OTHELLO")
        fenetre = pygame.display.set_mode((self.window_width, self.window_eight))
        fenetre.fill(self.bg_color)
        return fenetre

    def __repr__(self):
        '''Cette fonction permet d'afficher le tableau dans le terminal'''
        grille_aff = ""
        for x in self.grille:
            grille_aff += str(x) + '\n'
        return grille_aff

    def dessine_tableau(self, fenetre):
        '''Cette fonction permet de créer le tableau afficher'''
        for x in range(0, 9):
            pygame.draw.line(fenetre, self.couleur_ligne, (0, x * 125), (self.width, x * 125), 15)
            pygame.draw.line(fenetre, self.couleur_ligne, (x * 125, 0), (x * 125, self.width), 15)

    def place_pion(self, lig, col, joueur):
        '''Cette fonction permet de placer un pion dans le tableau en placant un numero en fonction
        du joueur (Soit 1, soit 2). Exemple: 1 0 0 0
                                             0 2 0 0
                                             0 0 0 0'''
        self.grille[lig][col] = joueur

        for direc in self.directions:
            voisins = [lig + direc[0], col + direc[1]]
            while 0 <= voisins[0] <= 7 and 0 <= voisins[1] <= 7:
                if self.grille[voisins[0]][voisins[1]] == joueur:
                    self.retourne_pion(joueur, lig, col, direc)
                    break

                voisins[0] += direc[0]
                voisins[1] += direc[1]

    def retourne_pion(self, joueur, lig, col, direction):
        '''Cette fonction permet de retourner les pions lorsqu'un joueur joue'''
        voisins = [lig + direction[0], col + direction[1]]
        while self.grille[voisins[0]][voisins[1]] == self.autre_joueur(joueur):
            self.grille[voisins[0]][voisins[1]] = joueur

            voisins[0] += direction[0]
            voisins[1] += direction[1]
    
    def autre_joueur(self, joueur):
        '''Cette fonction retourne le joueur inverse de celui qui joue'''
        if joueur == 1:
            return 2
        else:
            return 1

    def coup_valide(self, joueur, lig, col):
        '''Cette fonction renvoie True si une case est jouable ou non'''
        if self.grille[lig][col] != 0:
            return False
        
        for direc in self.directions:
            voisins = [lig + direc[0], col + direc[1]]
            while 0 <= voisins[0] < 7 and 0 <= voisins[1] < 7 and self.grille[voisins[0]][voisins[1]] == self.autre_joueur(joueur):
                voisins[0] += direc[0]
                voisins[1] += direc[1]

                if self.grille[voisins[0]][voisins[1]] == joueur:
                    return True
        return False

    def meilleurs_coup(self, joueur):
        '''Cette fonction permet a l'IA de placer des pions et de jouer des coups'''
        
        liste_meilleurs_coup = []
        coup_valide = []
        
        for lig in range(self.ligne):
            for col in range(self.colonne):
                if self.coup_valide(joueur, lig, col):
                    coup_valide.append((lig, col))
        
        for c in coup_valide:
            n_max = 0
            for direc in self.directions:
                voisins = [c[0] + direc[0], c[1] + direc[1]]
                n = 0
                while 0 <= voisins[0] <= 7 and 0 <= voisins[1] <= 7 and self.grille[voisins[0]][voisins[1]] == self.autre_joueur(joueur):
                    n += 1
                    voisins[0] += direc[0]
                    voisins[1] += direc[1]

                    if 0 <= voisins[0] <= 7 and 0 <= voisins[1] <= 7:
                        if self.grille[voisins[0]][voisins[1]] == joueur:
                            n_max += n
                            break
            
            liste_meilleurs_coup.append((c[0], c[1], n_max))
            liste_meilleurs_coup.sort(key=lambda x:x[2], reverse=1)
            for x in liste_meilleurs_coup:
                if x[2] < liste_meilleurs_coup[0][2]:
                    liste_meilleurs_coup.remove(x)

        if liste_meilleurs_coup != []:
            liste = random.randint(0, len(liste_meilleurs_coup) - 1)
            self.place_pion(liste_meilleurs_coup[liste][0], liste_meilleurs_coup[liste][1], joueur)

    def affiche_coup_possible(self, joueur, fenetre):
        '''Cette fonction permet de placer des marqueur sur la grille, indiquant les coups possibles'''
        for lig in range(self.ligne):
            for col in range(self.colonne):
                pygame.draw.circle(fenetre, self.bg_color, (int(col * self.width / 8 + 60), int(lig * self.width / 8 + 60)), int(self.circle_radius / 4), int(self.circle_width / 4))
                if self.coup_valide(joueur, lig, col) and self.grille[lig][col] == 0:
                    pygame.draw.circle(fenetre, self.couleur_ligne, (int(col * self.width / 8 + 60), int(lig * self.width / 8 + 60)), int(self.circle_radius / 4), int(self.circle_width / 4))

    def fini(self, joueur):
        '''Cette fonction permet de savoir quant la partie est terminée / quand il n'y a plus de coup possible'''
        for lig in range(self.ligne):
            for col in range(self.colonne):
                if self.coup_valide(joueur, lig, col):
                    return True
        return False

    def dessin_pion(self, fenetre):
        '''Cette fonction permet de dessiner les différent pions lorsque qu'un joueur joue'''
        for lig in range(self.ligne):
            for col in range(self.colonne):
                if self.grille[lig][col] == 1:
                    pygame.draw.circle(fenetre, self.pion_noir, (int(col * self.width / 8 + 63), int(lig * self.width / 8 + 63)), self.circle_radius, self.circle_width)

                if self.grille[lig][col] == 2:
                    pygame.draw.circle(fenetre, self.pion_blanc, (int(col * self.width / 8 + 63), int(lig * self.width / 8 + 63)), self.circle_radius, self.circle_width)

    def case_libre(self, lig, col):
        '''Cette fonction renvoie True si la case selectionner est libre et False sinon'''
        return self.grille[lig][col] == 0 or self.grille[lig][col] == 5

    def sauvegarde(self):
        save = open("save.txt", "w")
        save.write(str(self.grille) + "/")

    def boucle_principale_JvsJ(self, fenetre, tableau, interface):
        '''Cette fonction contient la boucle principale du jeu lors du jeu contre un 2eme joueur humain'''
        joueur = 1
        self.fin = False

        while not self.fin:

            interface.nb_pion(fenetre, tableau.grille)
            interface.joueur_actuel(joueur, fenetre)

            tableau.affiche_coup_possible(joueur, fenetre)
            tableau.dessin_pion(fenetre)

            if not tableau.fini(joueur):
                pygame.display.set_caption("Partie terminée")
                pion_noir = 0
                pion_blanc = 0
                self.fin = True

                for lig in range(self.ligne):
                    for col in range(self.colonne):
                        if self.grille[lig][col] == 1:
                            pion_noir += 1
                        elif self.grille[lig][col] == 2:
                            pion_blanc += 1
                
                if pion_noir > pion_blanc:
                    self.gagnant = 1
                if pion_blanc > pion_noir:
                    self.gagnant = 2
                if pion_noir == pion_blanc:
                    self.gagnant = 3

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.fin = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.fin = True

                    if event.key == pygame.K_s:
                        self.sauvegarde()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    mouse_X = event.pos[0]
                    mouse_Y = event.pos[1]

                    colonne_selectionne = int(mouse_X // 125)
                    ligne_selectionne = int(mouse_Y // 125)

                    if colonne_selectionne <= 7 and ligne_selectionne <= 7:
                        if tableau.coup_valide(joueur, ligne_selectionne, colonne_selectionne):
                            if joueur == 1:
                                tableau.place_pion(ligne_selectionne, colonne_selectionne, 1)
                                joueur = 2                            
                            else:
                                if joueur == 2:
                                    tableau.place_pion(ligne_selectionne, colonne_selectionne, 2)
                                    joueur = 1

            pygame.display.update()
        # time.sleep(4)
    
    def boucle_principale_JvsIA(self, fenetre, tableau, interface):
        '''Cette fonciton contient la boucle principale du jeu lors du jeu contre l'IA'''
        joueur = 1
        self.fin = False

        while not self.fin:

            interface.nb_pion(fenetre, tableau.grille)
            interface.joueur_actuel(joueur, fenetre)


            tableau.affiche_coup_possible(joueur, fenetre)
            tableau.dessin_pion(fenetre)

            if not tableau.fini(joueur):
                pygame.display.set_caption("Partie terminée")
                pion_noir = 0
                pion_blanc = 0
                self.fin = True
 
                for lig in range(self.ligne):
                    for col in range(self.colonne):
                        if self.grille[lig][col] == 1:
                            pion_noir += 1
                        elif self.grille[lig][col] == 2:
                            pion_blanc += 1
                
                if pion_noir > pion_blanc:
                    self.gagnant = 1
                if pion_blanc > pion_noir:
                    self.gagnant = 2
                if pion_noir == pion_blanc:
                    self.gagnant = 3

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.fin = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.fin = True
                    
                    if event.type == pygame.K_p:
                        pass

                if event.type == pygame.MOUSEBUTTONDOWN:

                    mouse_X = event.pos[0]
                    mouse_Y = event.pos[1]

                    colonne_selectionne = int(mouse_X // 125)
                    ligne_selectionne = int(mouse_Y // 125)

                    if colonne_selectionne <= 7 and ligne_selectionne <= 7:
                        if tableau.coup_valide(joueur, ligne_selectionne, colonne_selectionne):
                            if joueur == 1:
                                tableau.place_pion(ligne_selectionne, colonne_selectionne, 1)
                                joueur = 2
                            
            if joueur == 2:
                self.meilleurs_coup(joueur)
                joueur = 1

            pygame.display.update()
        time.sleep(4)

    def boucle_principale_IAvsIA(self, fenetre, tableau, interface):
        '''Cette fonciton contient la boucle principale du jeu lors du jeu IA contre IA'''
        joueur = 1
        self.fin = False

        while not self.fin:

            interface.nb_pion(fenetre, tableau.grille)
            interface.joueur_actuel(joueur, fenetre)


            # tableau.affiche_coup_possible(joueur, fenetre)
            tableau.dessin_pion(fenetre)

            if not tableau.fini(joueur):
                pygame.display.set_caption("Partie terminée")
                pion_noir = 0
                pion_blanc = 0
                self.fin = True

                for lig in range(self.ligne):
                    for col in range(self.colonne):
                        if self.grille[lig][col] == 1:
                            pion_noir += 1
                        elif self.grille[lig][col] == 2:
                            pion_blanc += 1
                
                if pion_noir > pion_blanc:
                    self.gagnant = 1
                if pion_blanc > pion_noir:
                    self.gagnant = 2
                if pion_noir == pion_blanc:
                    self.gagnant = 3

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.fin = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.fin = True
                    
                    if event.type == pygame.K_p:
                        pass

            if joueur == 1:
                self.meilleurs_coup(joueur)
                joueur = 2

            if joueur == 2:
                self.meilleurs_coup(joueur)
                joueur = 1

            pygame.display.update()
        time.sleep(4)

class GUI:

    def __init__(self):
        self.colonne = 8
        self.ligne = 8
        self.couleur_ligne = (0, 175, 145)
        self.bg_color = (24, 77, 71)
        self.circle_radius = 50
        self.circle_width = 50
        self.pion_noir = (34, 40, 49)
        self.pion_blanc = (221, 221, 221)

    def joueur_actuel(self, joueur, fenetre):
        '''Cette fonction permet d'afficher a l'écran le joueur actuel'''
        if joueur == 1:
            pygame.draw.circle(fenetre, self.pion_noir, (1200, 800), int(self.circle_radius * 1.5), int(self.circle_width * 1.5))
        if joueur == 2:
            pygame.draw.circle(fenetre, self.pion_blanc, (1200, 800), int(self.circle_radius * 1.5), int(self.circle_width * 1.5))

    def nb_pion(self, fenetre, grille):
        '''Cette fonction permet de comptabiliser le nombre de pions de chaque joueur'''
        pion_noir = 0
        pion_blanc = 0
        for lig in range(self.ligne):
            for col in range(self.colonne):
                if grille[lig][col] == 1:
                    pion_noir += 1
                if grille[lig][col] == 2:
                    pion_blanc += 1
        self.affiche_nb_pion(str(pion_noir), str(pion_blanc), fenetre)
        return (pion_noir, pion_blanc)
    
    def affiche_nb_pion(self, nb_pion_noir, nb_pion_blanc, fenetre):
        '''Cette fonction permet d'afficher a l'écran le nombre de pion de chaque joueur'''
        my_font2 = pygame.font.SysFont('liberationsansnarrow', 30, bold = 1)

        pygame.draw.rect(fenetre, self.bg_color, (1285, 200, 45, 30))
        pygame.draw.rect(fenetre, self.bg_color, (1300, 300, 45, 30))

        nb_pion_noir = my_font2.render(f'Nombre de pions noir: {nb_pion_noir}', False, (0, 0, 0))
        fenetre.blit(nb_pion_noir, (1015,200))

        nb_pion_blanc = my_font2.render(f'Nombre de pions blanc: {nb_pion_blanc}', False, (0, 0, 0))
        fenetre.blit(nb_pion_blanc, (1015,300))


# class Gagnant:

#     def __init__(self, joueur, fenetre, gagnant):
#         self.joueur = joueur
#         self.fenetre = fenetre
#         self.gagnant = gagnant
#         self.font = pygame.font.SysFont('Corbel', 100)
#         self.title = self.font.render("Le gagnant est:", True, (37, 37, 37))
#         self.title2 = self.font.render("Egalité::", True, (37, 37, 37))

#     def affichage(self):
#         '''Cette fonction contient la boucle affichant le fenetre d'affichage du ou des gagnants'''
#         quitter = Boutton(self.fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 250, 600, 270, 615, 300, 100, "Quitter")
#         fin = False

#         while not fin:

#             mouse = pygame.mouse.get_pos()

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     fin = True

#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if 250 <= mouse[0] <= 550 and 600 <= mouse[1] <= 700: # boutton Jouer
#                         fin = True                
            
#             if self.gagnant == 1:
#                 self.fenetre.blit(self.title, (140, 20))
#                 pygame.draw.circle(self.fenetre, (34, 40, 49), (400, 400), 100, 100)
#             if self.gagnant == 2:
#                 self.fenetre.blit(self.title, (140, 20))
#                 pygame.draw.circle(self.fenetre, (221, 221, 221), (400, 400), 100, 100)
#             if self.gagnant == 3:
#                 self.fenetre.blit(self.title2, (10, 10))
#                 pygame.draw.circle(self.fenetre, (34, 40, 49), (200, 400), 100, 100)
#                 pygame.draw.circle(self.fenetre, (221, 221, 221), (600, 400), 100, 100)
            
#             quitter.affiche(mouse)
            

#             pygame.display.update()

# class Menu:

#     def __init__(self, fenetre):
#         self.fenetre = fenetre
#         self.fin = False
#         self.mode = 0
#         self.font = pygame.font.SysFont('Corbel', 200)
#         self.font2 = pygame.font.SysFont('Corbel', 40)
#         self.title = self.font.render("Othello", True, (37, 37, 37))
#         self.credit = self.font2.render(("Fait par Gabriel et Ilian. Astro Company" u"\u00A9" " 2018 - 2021"), True, (37, 37, 37))

#     def affichage(self):
#         '''Cette fonction affiche les différents textes a l'écrans'''
#         self.fenetre.blit(self.title, (160, 10))
#         self.fenetre.blit(self.credit, (40, 750))

#     def boucle_principale(self, fenetre):
#         '''Cette fonciton contient la boucle qui affiche les différents bouttons qui composent le menu'''
#         boutton_JvJ = Boutton(fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 50, 200, 100, 220, 300, 100, "J vs J")
#         boutton_JvIA = Boutton(fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 450, 400, 490, 420, 300, 100, "J vs IA")
#         boutton_IAvIA = Boutton(fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 450, 200, 475, 220, 300, 100, "IA vs IA")

#         boutton_quitter = Boutton(fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 50, 600, 80, 620, 300, 100, "Quitter")
#         boutton_regles = Boutton(fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 450, 600, 490, 615, 300, 100, "Règles")
#         boutton_charger_partie = Boutton(fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 50, 400, 60, 420, 300, 100, "Charger")


#         menu = Menu(fenetre)
#         choix = False

#         while not self.fin:

#             mouse = pygame.mouse.get_pos()

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()

#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if 450 <= mouse[0] <= 750 and 200 <= mouse[1] <= 300: # boutton IA vs IA
#                         self.fin = True
#                         self.mode = 1
#                     if 450 <= mouse[0] <= 750 and 400 <= mouse[1] <= 500: # boutton J vs IA
#                         self.fin = True
#                         self.mode = 2
#                     if 50 <= mouse[0] <= 350 and 200 <= mouse[1] <= 300: # boutton J vs J
#                         self.fin = True
#                         self.mode = 3
#                     if 450 <= mouse[0] <= 750 and 600 <= mouse[1] <= 700: # boutton Règles
#                         pass

#                     if 50 <= mouse[0] <= 750 and 600 <= mouse[1] <= 700: # boutton Règles
#                         pass

#                     if 50 <= mouse[0] <= 350 and 600 <= mouse[1] <= 700: # boutton Quitter
#                         pygame.quit()


#             boutton_JvJ.affiche(mouse)
#             boutton_JvIA.affiche(mouse)
#             boutton_IAvIA.affiche(mouse)
#             boutton_quitter.affiche(mouse)
#             boutton_regles.affiche(mouse)
#             boutton_charger_partie.affiche(mouse)
#             menu.affichage()

#             pygame.display.update()

#     def fin_menu(self):

# class Boutton:

#     def __init__(self, fenetre, couleur_boutton, couleur_texte, hover_color, x, y, x_txt, y_txt, width, eight, label):
#         self.fenetre = fenetre
#         self.couleur = couleur_boutton
#         self.hover_color = hover_color
#         self.x = x
#         self.y = y
#         self.x_txt = x_txt
#         self.y_txt = y_txt
#         self.width = width
#         self.eight = eight

#         self.font = pygame.font.SysFont('Corbel',100)
#         self.label = self.font.render(label , True , couleur_texte)

#     def affiche(self, mouse_pos):
#         '''Cette fonction affiche et anime les bouttons'''
#         if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.eight:
#             pygame.draw.rect(self.fenetre, (24, 77, 71), (self.x + 5, self.y + 5, self.width, self.eight), border_radius=20)
#             pygame.draw.rect(self.fenetre, self.couleur, (self.x, self.y, self.width, self.eight), border_radius=20)
#             self.fenetre.blit(self.label, (self.x_txt, self.y_txt))
#         else:
#             pygame.draw.rect(self.fenetre, (0, 121, 101), (self.x + 5, self.y + 5, self.width, self.eight), border_radius=20)
#             pygame.draw.rect(self.fenetre, self.couleur, (self.x, self.y, self.width, self.eight), border_radius=20)
#             self.fenetre.blit(self.label, (self.x_txt, self.y_txt))