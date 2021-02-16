# Othello
Projet réaliser par deux personnes dans le cadre d'un projet à rendre en NSI en classe de terminale.  
Ce jeu a été codé en Python.  
Ce projet nous a pris environ 2 mois et demi pour être réalisé et il reste encore des choses à faire pour le terminer à 100 % comme nous le voulons.  
Nous vous partageons le code de notre jeu afin que vous puissiez vous en inspirer ou le compléter.  

# Liste des choses à faire:
- Comprendre les règles du jeu:heavy_check_mark:
- Représentation graphique du plateau de jeu:heavy_check_mark:
- Pouvoir jouer une partie contre un autre joueur humain:heavy_check_mark:
- Pouvoir sauvegarder
- Pouvoir jouer contre une IA et faire jouer une IA contre une autre IA:heavy_check_mark:
- Optimisation
- Finalisation

# Règles du jeu:  
Othello est un jeu de réflexion créé en 1971 par Goro Hasegaw au Japon.  
Si le jeu est plutôt simple en apparence, il s’avère qu’il demande de la stratégie et voici donc les règles du jeu :
- Jeu en 1 vs 1
- Deux couleurs : Noir et Blanc
- Le joueur ayant le plus de pions de sa couleur lorsque le plateau de jeu est rempli gagne la partie.

Une contrainte : pour pouvoir placer un pion de sa couleur, il faut que ce dernier soit placé de manière à ce qu’il encercle un pion de couleur adverse.

# Représentation du plateau de jeu
Utilisation d'une liste de listes en python contenant des 0 pour représenter les cases vides :  
[  
[0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0]  
]

Ce choix est dû au fait que les listes sont simples a manipuler et que l'on peut se retrouver avec un système de coordonnées (x, y) grâce au parcours de liste.

# L'interface graphique
Notre choix s'est porté sur le module Pygame de Python.
Nous ne le connaissions pas, mais grâce à des vidéos et des forums nous avons pu en tirer quelque chose et créer une représentation graphique de notre plateau de jeu.

# L'IA
Dans notre projet, nous devions créer une simple IA qui jouais le coup qui lui rapporter le plus de pions possibles.
Grâce a des recherches sur la création d'IA pour certains jeux de plateau, nous avons vu que le sujet étai très intéressant et que de nombreuses personnes se penchent sur le sujet et développent des IA très performantes.  
# Le code sera mis prochainement, nous travaillons dessus actuellement
