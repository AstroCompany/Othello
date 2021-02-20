import pygame

class Boutton:

    def __init__(self, fenetre, couleur_boutton, couleur_texte, hover_color, x, y, x_txt, y_txt, width, eight, label):
        self.fenetre = fenetre
        self.couleur = couleur_boutton
        self.hover_color = hover_color
        self.x = x
        self.y = y
        self.x_txt = x_txt
        self.y_txt = y_txt
        self.width = width
        self.eight = eight

        self.font = pygame.font.SysFont('Corbel',100)
        self.label = self.font.render(label , True , couleur_texte)

    def affiche(self, mouse_pos):
        '''Cette fonction affiche et anime les bouttons'''
        if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.eight:
            pygame.draw.rect(self.fenetre, (24, 77, 71), (self.x + 5, self.y + 5, self.width, self.eight), border_radius=20)
            pygame.draw.rect(self.fenetre, self.couleur, (self.x, self.y, self.width, self.eight), border_radius=20)
            self.fenetre.blit(self.label, (self.x_txt, self.y_txt))
        else:
            pygame.draw.rect(self.fenetre, (0, 121, 101), (self.x + 5, self.y + 5, self.width, self.eight), border_radius=20)
            pygame.draw.rect(self.fenetre, self.couleur, (self.x, self.y, self.width, self.eight), border_radius=20)
            self.fenetre.blit(self.label, (self.x_txt, self.y_txt))


class Menu:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.width = 800
        self.eight = 800
        self.bg_color = (24, 77, 71)

        self.fin = False
        self.etat = None

    def texte(self):
        font1 = pygame.font.SysFont('Corbel', 200)
        font2 = pygame.font.SysFont('Corbel', 40)
        titre = font1.render("Othello", True, (37, 37, 37))
        credit = font2.render(("Fait par Gabriel et Ilian. Astro Company" u"\u00A9" " 2018 - 2021"), True, (37, 37, 37))
        self.fenetre.blit(titre, (160, 20))
        self.fenetre.blit(credit, (40, 750))

    def update(self):
        if self.etat == 1:
            self.fenetre.fill((24, 77, 71))
            self.texte()
        if self.etat == 2:
            self.fenetre.fill((255, 0, 0))

    def mode(self):
        return self.etat

    def boucle_principale(self):
        boutton_jouer = Boutton(self.fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 250, 300, 300, 320, 300, 100, "Jouer")
        boutton_quitter = Boutton(self.fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 50, 500, 80, 520, 300, 100, "Quitter")
        boutton_regles = Boutton(self.fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 450, 500, 490, 520, 300, 100, "Règles")

        boutton_JvsJ = Boutton(self.fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 50, 300, 100, 320, 300, 100, "J vs J")
        boutton_JvsIA = Boutton(self.fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 450, 300, 490, 320, 300, 100, "J vs IA")
        boutton_IAvsIA = Boutton(self.fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 450, 500, 480, 520, 300, 100, "IA vs IA")

        self.texte()

        while not self.fin:

            mouse = pygame.mouse.get_pos()
            self.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.fin = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.fin = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 < mouse[0] < 350 and 500 < mouse[1] < 600: # click pour Quitter
                        self.fin = True

                    if 250 < mouse[0] < 550 and 300 < mouse[1] < 400 and self.etat == None: # click pour Jouer
                        self.etat = 1

                    if 450 < mouse[0] < 750 and 500 < mouse[1] < 600 and self.etat == None: # click pour Règles
                        self.etat = 2
                    
                    if 50 < mouse[0] < 350 and 300 < mouse[1] < 400 and self.etat == 1: # click pour J vs J
                        self.etat = 3
                        self.fin = True

                    if 450 < mouse[0] < 750 and 300 < mouse[1] < 400 and self.etat == 1: # click pour J vs IA
                        self.etat = 4
                        self.fin = True

                    if 450 < mouse[0] < 750 and 500 < mouse[1] < 600 and self.etat == 1: # click pour IA vs IA
                        self.etat = 5
                        self.fin = True

            if self.etat == None:
                boutton_jouer.affiche(mouse)
                boutton_regles.affiche(mouse)
            if self.etat == 1:
                boutton_JvsJ.affiche(mouse)
                boutton_JvsIA.affiche(mouse)
                boutton_IAvsIA.affiche(mouse)

            boutton_quitter.affiche(mouse)
                
            pygame.display.update()



class Gagnant:

    def __init__(self, joueur, fenetre, gagnant):
        self.joueur = joueur
        self.fenetre = fenetre
        self.gagnant = gagnant
        self.font = pygame.font.SysFont('Corbel', 100)
        self.title = self.font.render("Le gagnant est:", True, (37, 37, 37))
        self.title2 = self.font.render("Egalité::", True, (37, 37, 37))

    def affichage(self):
        '''Cette fonction contient la boucle affichant le fenetre d'affichage du ou des gagnants'''
        quitter = Boutton(self.fenetre, (0, 175, 145), (37, 37, 37), (24, 77, 71), 250, 600, 270, 615, 300, 100, "Quitter")
        fin = False

        while not fin:

            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 250 <= mouse[0] <= 550 and 600 <= mouse[1] <= 700: # boutton Jouer
                        fin = True                
            
            if self.gagnant == 1:
                self.fenetre.blit(self.title, (140, 20))
                pygame.draw.circle(self.fenetre, (34, 40, 49), (400, 400), 100, 100)
            if self.gagnant == 2:
                self.fenetre.blit(self.title, (140, 20))
                pygame.draw.circle(self.fenetre, (221, 221, 221), (400, 400), 100, 100)
            if self.gagnant == 3:
                self.fenetre.blit(self.title2, (10, 10))
                pygame.draw.circle(self.fenetre, (34, 40, 49), (200, 400), 100, 100)
                pygame.draw.circle(self.fenetre, (221, 221, 221), (600, 400), 100, 100)
            
            quitter.affiche(mouse)
            

            pygame.display.update()