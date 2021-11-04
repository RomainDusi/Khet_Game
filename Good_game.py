#coding=utf-8
#_*_ coding:Latin-1 _*_


import pygame, sys              # On importe les necessités
from pygame.locals import *
import os.path
os.chdir(sys.path[0])
from Variables import *

pygame.init()

def newgrid():  # Création de grilles vides
    grid = [[[0, 0, 0] for i in range(10)] for k in range(8)]
    grid[0][0] = [1, 5, 2]
    grid[7][9] = [2, 5, 0]  # Placement des 2 Sphinx
    base = [[0, 2, 0, 0, 0, 0, 0, 0, 1, 2],     # Cases appartenant à un joueur ou l'autre
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [1, 2, 0, 0, 0, 0, 0, 0, 1, 0]]
    return grid, base


def loadconfiguration(selectgrid):  # Choix du plateau parmis les pré-faits
    if selectgrid == 1:     # Classic
        grid = [[[1, 5, 2], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 3, 2], [1, 1, 2], [1, 3, 2], [1, 4, 2], [0, 0, 0],[0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [1, 4, 3], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 4, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0]],
                [[1, 4, 1], [0, 0, 0], [2, 4, 3], [0, 0, 0], [1, 2, 3], [1, 2, 0], [0, 0, 0], [1, 4, 2], [0, 0, 0],[2, 4, 0]],
                [[1, 4, 2], [0, 0, 0], [2, 4, 0], [0, 0, 0], [2, 2, 2], [2, 2, 1], [0, 0, 0], [1, 4, 1], [0, 0, 0],[2, 4, 3]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 4, 2], [0, 0, 0], [0, 0, 0],[0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 4, 1], [0, 0, 0],[0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [2, 4, 0], [2, 3, 0], [2, 1, 0], [2, 3, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[2, 5, 0]]]
    elif selectgrid == 2:       # Imhotep
        grid = [[[1, 5, 2], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 3, 2], [1, 1, 2], [1, 3, 2], [1, 2, 0], [0, 0, 0],[0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 4, 0], [0, 0, 0], [0, 0, 0], [1, 4, 1], [0, 0, 0], [0, 0, 0],[0, 0, 0]],
                [[1, 4, 1], [2, 4, 3], [0, 0, 0], [0, 0, 0], [2, 4, 2], [1, 2, 0], [0, 0, 0], [0, 0, 0], [1, 4, 2],[2, 4, 0]],
                [[1, 4, 2], [2, 4, 0], [0, 0, 0], [0, 0, 0], [2, 2, 2], [1, 4, 0], [0, 0, 0], [0, 0, 0], [1, 4, 1],[2, 4, 3]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 4, 3], [0, 0, 0], [0, 0, 0], [1, 4, 2], [0, 0, 0], [0, 0, 0],[0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [2, 2, 2], [2, 3, 0], [2, 1, 0], [2, 3, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[2, 5, 0]]]
    elif selectgrid == 3:       # Dynasty
        grid = [[[1, 5, 2], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 4, 3], [1, 3, 2], [1, 4, 2], [0, 0, 0], [0, 0, 0],[0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 1, 2], [0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0]],
                [[1, 4, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 4, 3], [1, 3, 2], [1, 2, 2], [0, 0, 0], [0, 0, 0],[0, 0, 0]],
                [[1, 4, 2], [0, 0, 0], [1, 2, 1], [0, 0, 0], [2, 4, 0], [0, 0, 0], [2, 4, 2], [0, 0, 0], [0, 0, 0],[0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 4, 0], [0, 0, 0], [1, 4, 2], [0, 0, 0], [2, 2, 3], [0, 0, 0],[2, 4, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 2, 0], [2, 3, 0], [2, 4, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0],[2, 4, 3]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 4, 0], [2, 3, 0], [2, 4, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0],[2, 5, 0]]]
    return grid


def Possible(grid, player, base, m, n, i, j):   # Si le mouvement de la pièce est possible
    if (i < m -1 or i > m + 1 or j < n - 1 or j > n + 1) or (grid[i][j][0] == player) or (base[i][j] != player and base[i][j] != 0):
        # Si la case n'est pas adjacente, ou qu'une de nos pièce est déjà sur la case, ou si la case ne nous appartient pas
        return False
    else:
        if grid[m][n][1] == 2:  # Si le pion a déplacer est un scarab
            if (grid[i][j][1] == 3 or grid[i][j][1] == 4):  # Si la destination est un Anubis ou une Pyramid
                return True
        if (i < m - 1 or i > m + 1 or j < n - 1 or j > n + 1) or (grid[i][j][0] != 0):  # Si la case n'est pas adjacente, ou la case est occupée
            return False
    return True


def rotation(grid, rotate, i, j):
    if grid[i][j][1] == 5:  # Si la pièce est un Sphinx
        if grid[i][j][0] == 1:  # Si elle est au joueur 1
            if grid[i][j][2] == 2:  # Rotation dans le seul sens possible
                grid[i][j][2] = 1
            else:
                grid[i][j][2] = 2
        else:   # Si elle est au joueur 2
            if grid[i][j][2] == 0:  # Rotation dans le seul sens possible
                grid[i][j][2] = 3
            else:
                grid[i][j][2] = 0
    else:   # Pour les autres pièces
        if rotate == 1: # Sens anti-horaire
            if grid[i][j][2] == 0:
                grid[i][j][2] = 3
            else:
                grid[i][j][2] -= 1
        else:   # Sens horaire
            if grid[i][j][2] == 3:
                grid[i][j][2] = 0
            else:
                grid[i][j][2] += 1
    return grid


def changePlayer(player):   # Changement de joueur
    if player == 1:
        player = 2
    else:
        player = 1
    return player


def drawngameboard(MySurface, grid, base):  # Affichage de la zone de jeu
    pygame.draw.rect(MySurface, NOIR, (0, 0, 60 * 10 + 20, 60 * 8 + 20), 0) # Fond noir
    fond_jeux = pygame.image.load("images/fond_jeux.jpg").convert()
    fond_jeux = pygame.transform.scale(fond_jeux, (900, 550))
    MySurface.blit(fond_jeux, (0, 0))
    pygame.draw.rect(MySurface, GRIS2, (20, 20, 60 * 10, 60 * 8), 0)    # Zone de jeu
    for j in range(10):  # Pour chaque lignes et colonnes
        for i in range(8):
            pygame.draw.rect(MySurface, GRIS3, (20+60*j, 20+60*i, 60, 60), 2)   # On crée le contour de la case
            drawCell(MySurface, grid, i, j, base)   # L'intérieur de la case
    pygame.display.flip()


def  drawCell(MySurface, grid, i, j, base): # Affiche l'intérieur des cases
    if base[i][j] == 1: # L'appartenant de la case au joueur 1
        Case_Rouge = pygame.image.load("images/jeton_rouge.png")
        Case_Rouge = pygame.transform.scale(Case_Rouge, (56, 56))
        MySurface.blit(Case_Rouge, (22+60*j, 22+60*i))
    elif base[i][j] == 2:   # L'appartenant de la case au joueur 2
        Case_Bleue = pygame.image.load("images/jeton_bleu.png")
        Case_Bleue = pygame.transform.scale(Case_Bleue, (56, 56))
        MySurface.blit(Case_Bleue, (22+60*j, 22+60*i))
    if grid[i][j][0] == 1:  # Pions du joueur 1
        if grid[i][j][1] == 1:  # Pharaon
            Pharaon = pygame.image.load('images/pharaon.png')
            Pharaon = pygame.transform.scale(Pharaon,(56, 56))
            Pharaon = pygame.transform.rotate(Pharaon, (-90) * grid[i][j][2])   # Fait pivoter l'image en fonction de grid[i][j][2]
            MySurface.blit(Pharaon, (22+60*j, 22+60*i))
        elif grid[i][j][1] == 2:    # Scarab
            Scarab = pygame.image.load('images/scarab.png')
            Scarab = pygame.transform.scale(Scarab, (56, 56))
            Scarab = pygame.transform.rotate(Scarab, (-90) * grid[i][j][2])
            MySurface.blit(Scarab, (22 + 60 * j, 22 + 60 * i))
        elif grid[i][j][1] == 3:    # Anubis
            Anubis = pygame.image.load('images/anubis.png')
            Anubis = pygame.transform.scale(Anubis, (56, 56))
            Anubis = pygame.transform.rotate(Anubis, (-90) * grid[i][j][2])
            MySurface.blit(Anubis, (22 + 60 * j, 22 + 60 * i))
        elif grid[i][j][1] == 4:    # Pyramid
            Pyramid = pygame.image.load('images/pyramid.png')
            Pyramid = pygame.transform.scale(Pyramid, (56, 56))
            Pyramid = pygame.transform.rotate(Pyramid, (-90) * grid[i][j][2])
            MySurface.blit(Pyramid, (22 + 60 * j, 22 + 60 * i))
        elif grid[i][j][1] == 5:    # Shpinx
            Sphinx = pygame.image.load('images/sphinx.png')
            Sphinx = pygame.transform.scale(Sphinx, (56, 56))
            Sphinx = pygame.transform.rotate(Sphinx, (-90) * grid[i][j][2])
            MySurface.blit(Sphinx, (22 + 60 * j, 22 + 60 * i))
    elif grid[i][j][0] == 2:    # Pions du joueur 2
        if grid[i][j][1] == 1:  # Pharaon
            Pharaon = pygame.image.load('images/pharaon2.png')
            Pharaon = pygame.transform.scale(Pharaon, (56, 56))
            Pharaon = pygame.transform.rotate(Pharaon, (-90) * grid[i][j][2])
            MySurface.blit(Pharaon, (22 + 60 * j, 22 + 60 * i))
        elif grid[i][j][1] == 2:    # Scarab
            Scarab = pygame.image.load('images/scarab2.png')
            Scarab = pygame.transform.scale(Scarab, (56, 56))
            Scarab = pygame.transform.rotate(Scarab, (-90) * grid[i][j][2])
            MySurface.blit(Scarab, (22 + 60 * j, 22 + 60 * i))
        elif grid[i][j][1] == 3:    # Anubis
            Anubis = pygame.image.load('images/anubis2.png')
            Anubis = pygame.transform.scale(Anubis, (56, 56))
            Anubis = pygame.transform.rotate(Anubis, (-90) * grid[i][j][2])
            MySurface.blit(Anubis, (22 + 60 * j, 22 + 60 * i))
        elif grid[i][j][1] == 4:    # Pyramid
            Pyramid = pygame.image.load('images/pyramid2.png')
            Pyramid = pygame.transform.scale(Pyramid, (56, 56))
            Pyramid = pygame.transform.rotate(Pyramid, (-90) * grid[i][j][2])
            MySurface.blit(Pyramid, (22 + 60 * j, 22 + 60 * i))
        elif grid[i][j][1] == 5:    # Sphinx
            Sphinx = pygame.image.load('images/sphinx2.png')
            Sphinx = pygame.transform.scale(Sphinx, (56, 56))
            Sphinx = pygame.transform.rotate(Sphinx, (-90) * grid[i][j][2])
            MySurface.blit(Sphinx, (22 + 60 * j, 22 + 60 * i))


def played(MySurface, grid, player, base):  # Gestion du tour joueur
    x = None                                # Variables nécessaires
    Movement = font.render("Deplacer", 1, BLANC)
    Rotation = font.render("Rotation", 1, BLANC)
    Rotate = None
    x = 200
    y = 200
    End = False
    drawngameboard(MySurface, grid, base)                       # Affiche l'écran de jeu
    pygame.draw.rect(MySurface, GRIS3, (680, 90, 180, 50), 3)
    pygame.draw.rect(MySurface, GRIS3, (680, 190, 180, 50), 3)
    MySurface.blit(Movement, (700, 100))
    MySurface.blit(Rotation, (700, 200))
    pygame.display.flip()
    while End != True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                poseX, poseY = event.pos
                for i in range(8):  # Pour chaque case
                    for j in range(10):
                        if poseX >= 20 + 60 * j and poseX <= 20 + 60 * (j + 1):
                            if poseY >= 20 + 60 * i and poseY <= 20 + 60 * (i + 1):
                                if grid[i][j][0] == player: # Si la case sélectionnée représente un de nos pions
                                    x, y = i, j
                                    drawngameboard(MySurface, grid, base)   # On affiche la zone de jeu
                                    pygame.draw.rect(MySurface, GRIS3, (680, 90, 180, 50), 3)
                                    pygame.draw.rect(MySurface, GRIS3, (680, 190, 180, 50), 3)
                                    MySurface.blit(Movement, (700, 100))
                                    MySurface.blit(Rotation, (700, 200))
                                    current = pygame.Surface((60, 60), pygame.SRCALPHA) # On affiche le pion sélectionné
                                    current.fill((255, 192, 203, 128))
                                    MySurface.blit(current, (20 + 60 * y, 20 + 60 * x))
                if poseX >= 680 and poseX <= 860 and Rotate and x < 8:  # Si on a déjà choisi d'effectuer une rotation
                    if poseY >= 90 and poseY <= 140:    # Rotation horaire
                        rotate = 2
                        rotation(grid, rotate, x, y)
                        return 1, 1
                    if poseY >= 190 and poseY <= 240:   # Rotation anti-horaire
                        rotate = 1
                        rotation(grid, rotate, x, y)
                        return 1, 1
                if poseX >= 680 and poseX <= 860 and Rotate != True and x < 8:  # Si on clique sur Rotation
                    if poseY >= 190 and poseY <= 240:
                        drawngameboard(MySurface, grid, base)
                        Movement = font.render("Horaire", 1, BLANC)                 # Affichage des possibilités de rotation
                        Rotation = font2.render("Anti horaire", 1, BLANC)
                        pygame.draw.rect(MySurface, GRIS3, (680, 90, 180, 50), 3)
                        pygame.draw.rect(MySurface, GRIS3, (680, 190, 180, 50), 3)
                        MySurface.blit(Movement, (700, 100))
                        MySurface.blit(Rotation, (700, 200))
                        pygame.display.flip()
                        Rotate = True
                if poseX >= 680 and poseX <= 860 and x < 8: # Si on choisi de déplacer le pion
                    if poseY >= 90 and poseY <= 140:
                        Playable = False
                        if grid[x][y][1] != 5:  # Si le pion n'est pas un Sphinx
                            Possible_Movement(grid, player, base, x, y) # On affiche les mouvements possible
                            while Playable != True:
                                for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:
                                        poseX, poseY = event.pos
                                        for i in range(8):  # Pour chaque case
                                            for j in range(10):
                                                if poseX >= 20 + 60 * j and poseX <= 20 + 60 * (j + 1):
                                                    if poseY >= 20 + 60 * i and poseY <= 20 + 60 * (i + 1):
                                                        Playable = Possible(grid, player, base, x, y, i, j) # On vérifie si le déplacement est possible
                                                        if Playable == True:
                                                            grid[x][y], grid[i][j] = grid[i][j], grid[x][y] # Si c'est le cas on effectue le mouvement
                                    if event.type == QUIT:
                                        End = True
                            End = True
                            return 1, 1
            if event.type == QUIT:
                End = True
            pygame.display.flip()
    return 0, 0


def Possible_Movement(grid, player, base, x, y):    # Affiche les mouvements possibles
    for i in range(8):  # Pour chaques cases
        for j in range(10):
            Possible_mov = Possible(grid, player, base, x, y, i, j) # On vérifie si le déplacement sur cette case est valide
            if Possible_mov == True:
                poss_mov = pygame.Surface((60, 60), pygame.SRCALPHA)    # Si c'est le cas on l'affiche en vert
                poss_mov.fill((197, 255, 0, 100))
                MySurface.blit(poss_mov, (20 + 60 * j, 20 + 60 * i))
    pygame.display.flip()


def Creation_level():   # Crée un niveau
    grid, base = newgrid()  # On récupère les listes vierges
    MySurface = pygame.display.set_mode((1100, 550))
    pygame.display.set_caption('KHET 18.0')
    End = False
    current = pygame.Surface((80, 80), pygame.SRCALPHA) # Initialisation des variables
    current.fill((255, 192, 203, 128))
    x = 2000
    y = 2000
    player = 0
    piece = None
    drawngameboard(MySurface, grid, base)   # On affiche la zone de jeu
    Red_Pharaoh, Blue_Pharaoh, Red_Scarab, Blue_Scarab, Red_Pyramid, Blue_Pyramid, Red_Anubis, Blue_Anubis = draw_creation(
        MySurface, grid, current, x, y)
    while End != True:
        Red_Pharaoh, Blue_Pharaoh, Red_Scarab, Blue_Scarab, Red_Pyramid, Blue_Pyramid, Red_Anubis, Blue_Anubis = draw_creation(
            MySurface, grid, current, x, y)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                    poseX, poseY = event.pos
                    if poseX >= 675 and poseX <= 755:   # Pour le joueur 1
                        if poseY >= 40 and poseY <=  120:   # Sélection Pharaoh
                            x, y = 675, 40
                            piece = [Red_Pharaoh, 1, 1]
                        elif poseY >= 150 and poseY <= 230: # Scarab
                            x, y = 675, 150
                            piece = [Red_Scarab, 1, 2]
                        elif poseY >= 260 and poseY <= 340: # Anubis
                            x, y = 675, 260
                            piece = [Red_Anubis, 1, 3]
                        elif poseY >= 370 and poseY <= 450: # Pyramid
                            x, y = 675, 370
                            piece = [Red_Pyramid, 1, 4]
                    elif poseX >= 880 and poseX <= 960: # Pour le joueur 2
                        if poseY >= 40 and poseY <=  120:   # Pharaoh
                            x, y = 880, 40
                            piece = [Blue_Pharaoh, 2, 1]
                        elif poseY >= 150 and poseY <= 230: # Scarab
                            x, y = 880, 150
                            piece = [Blue_Scarab, 2, 2]
                        elif poseY >= 260 and poseY <= 340: # Anubis
                            x, y = 880, 260
                            piece = [Blue_Anubis, 2, 3]
                        elif poseY >= 370 and poseY <= 450: # Pyramid
                            x, y = 880, 370
                            piece = [Blue_Pyramid, 2, 4]
                    if poseX >= 675 and poseX <= 855:   # Quand on choisi la rotation
                        if poseY >= 475 and poseY <= 525:
                            Rotate = True
                            while Rotate != False:
                                Cur_Rotation = pygame.Surface((180, 50), pygame.SRCALPHA)   # On affiche qu'on est en mode rotation
                                Cur_Rotation.fill((255, 192, 203, 5))
                                MySurface.blit(Cur_Rotation, (675, 475))
                                pygame.display.flip()
                                for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:
                                        poseX, poseY = event.pos
                                        if poseX >= 675 and poseX <= 855:   # Si on reclique sur le bouton, on sort de ce mode
                                            if poseY >= 475 and poseY <= 525:
                                                Rotate = False
                                        for i in range(8):  # Pour chaque case
                                            for j in range(10):
                                                if poseX >= 20 + 60 * j and poseX <= 20 + 60 * (j + 1):
                                                    if poseY >= 20 + 60 * i and poseY <= 20 + 60 * (i + 1):
                                                        grid = rotation(grid, 0, i, j)  # On effectue la rotation
                                                        drawngameboard(MySurface, grid, base)   # On affiche la zone de jeu
                                    if event.type == QUIT:
                                        return 0, 0
                    for i in range(8):  # Pour chaque case
                        for j in range(10):
                            if poseX >= 20 + 60 * j and poseX <= 20 + 60 * (j + 1):
                                if poseY >= 20 + 60 * i and poseY <= 20 + 60 * (i + 1):
                                    if grid[i][j][1] == 0 and (base[i][j] == 0 or base[i][j] == piece[1]) and piece != None and piece[0] > 0:
                                        # Si la case est vide, qu'une pièce est sélectionnée et qu'il nous en reste à poser
                                        piece[0] -= 1
                                        grid[i][j] = [piece[1], piece[2], 0]    # On pose le pion
                                    elif grid[i][j][1] != 5:    # Si on clique sur un pion exepté le Sphinx
                                        grid[i][j] = [0, 0, 0]  # Supprime le pion
                                    drawngameboard(MySurface, grid, base)   # Affiche la zone de jeu
                    if poseX >= 880 and poseX <= 1060:  # Si on sauvegarde
                        if poseY >= 475 and poseY <= 525:
                            if Red_Pharaoh == 0 and Red_Scarab == 0 and Red_Pyramid == 0 and Red_Anubis == 0:           # Si toutes les pièces sont posées
                                if Blue_Pharaoh == 0 and Blue_Scarab == 0 and Blue_Pyramid == 0 and Blue_Anubis == 0:
                                    while End != True:
                                        pygame.draw.rect(MySurface, NOIR, (350, 200, 400, 120), 0)      # Affiche du choix du fichier
                                        pygame.draw.rect(MySurface, BLANC, (350, 200, 400, 120), 3)
                                        pygame.draw.rect(MySurface, BLANC, (370, 220, 80, 80), 3)
                                        pygame.draw.rect(MySurface, BLANC, (510, 220, 80, 80), 3)
                                        pygame.draw.rect(MySurface, BLANC, (650, 220, 80, 80), 3)
                                        Un = font3.render("1", 1, BLANC)
                                        Deux = font3.render("2", 1, BLANC)
                                        Trois = font3.render("3", 1, BLANC)
                                        MySurface.blit(Un, (398, 238))
                                        MySurface.blit(Deux, (538, 238))
                                        MySurface.blit(Trois, (678, 238))
                                        pygame.display.flip()
                                        for event in pygame.event.get():
                                            if event.type == MOUSEBUTTONDOWN:
                                                poseX, poseY = event.pos
                                                if poseY >= 220 and poseY <= 300:   # Fichier 1
                                                    if poseX >= 370 and poseX <= 450:
                                                        saveGrid(grid, 1)
                                                        End = True
                                                    if poseX >= 510 and poseX <= 590:   # Fichier 2
                                                        saveGrid(grid, 2)
                                                        End = True
                                                    if poseX >= 650 and poseX <= 730:   # Fichier 3
                                                        saveGrid(grid, 3)
                                                        End = True
                                            if event.type == QUIT:
                                                return 0, 0
            if event.type == QUIT:
                return 0, 0
    return 1, 0


def loadGrid(file): # Charge une sauvegarde crée par le joueur
    Fichier = file.readlines()  # On enregistre le contenu du fichier
    grid = [[[0, 0, 0] for i in range(10)] for k in range(8)]    # On crée une nouvelle grid
    for i in range(8):
        compt = 0
        list = Fichier[i]   # Pour chaque ligne de notre fichier
        for j in range(10):
            for k in range(3):
                grid[i][j][k] = int(list[compt])   # On recrée la grid case par case
                compt += 1
    file.close()
    return grid


def saveGrid(grid, sauvegarde): # Sauvegarde les listes crées par le joueur
    if sauvegarde == 1: # Fichier 1
        file = open('saves/1.txt', 'w+')
    elif sauvegarde == 2:   # Fichier 2
        file = open('saves/2.txt', 'w+')
    elif sauvegarde == 3:   # Fichier 3
        file = open('saves/3.txt', 'w+')
    for i in range(8):  # Pour chaque case de la grid
        for j in range(10):
            for k in range(3):
                file.writelines(str(grid[i][j][k]))    # On écrit ligne par ligne dans le fichier
        file.writelines("\n")
    file.close()


def draw_creation(MySurface, grid, current, x, y):  # Affiche le choix des pions lors de la création d'un niveau
    Red_Pharaoh = 1      # Nombres de pièces disponible
    Blue_Pharaoh = 1
    Red_Scarab = 2
    Blue_Scarab = 2
    Red_Pyramid = 7
    Blue_Pyramid = 7
    Red_Anubis = 2
    Blue_Anubis = 2
    for i in range(8):  # Pour chaque case
        for j in range(10):
            if grid[i][j][0] == 1:          # On recalcule les pièces restante à poser
                if grid[i][j][1] == 1:
                    Red_Pharaoh -= 1
                elif grid[i][j][1] == 2:
                    Red_Scarab -= 1
                elif grid[i][j][1] == 3:
                    Red_Anubis -= 1
                elif grid[i][j][1] == 4:
                    Red_Pyramid -= 1
            elif grid[i][j][0] == 2:
                if grid[i][j][1] == 1:
                    Blue_Pharaoh -= 1
                elif grid[i][j][1] == 2:
                    Blue_Scarab -= 1
                elif grid[i][j][1] == 3:
                    Blue_Anubis -= 1
                elif grid[i][j][1] == 4:
                    Blue_Pyramid -= 1
    pygame.draw.rect(MySurface, NOIR, (640, 0, 500, 600), 0)   # On affiche les pions
    Pharaon = pygame.image.load('images/pharaon.png')
    Pharaon = pygame.transform.scale(Pharaon, (80, 80))
    MySurface.blit(Pharaon, (675, 40))
    Scarab = pygame.image.load('images/scarab.png')
    Scarab = pygame.transform.scale(Scarab, (80, 80))
    MySurface.blit(Scarab, (675, 150))
    Anubis = pygame.image.load('images/anubis.png')
    Anubis = pygame.transform.scale(Anubis, (80, 80))
    MySurface.blit(Anubis, (675, 260))
    Pyramid = pygame.image.load('images/pyramid.png')
    Pyramid = pygame.transform.scale(Pyramid, (80, 80))
    MySurface.blit(Pyramid, (675, 370))
    Pharaon = pygame.image.load('images/pharaon2.png')
    Pharaon = pygame.transform.scale(Pharaon, (80, 80))
    MySurface.blit(Pharaon, (880, 40))
    Scarab = pygame.image.load('images/scarab2.png')
    Scarab = pygame.transform.scale(Scarab, (80, 80))
    MySurface.blit(Scarab, (880, 150))
    Anubis = pygame.image.load('images/anubis2.png')
    Anubis = pygame.transform.scale(Anubis, (80, 80))
    MySurface.blit(Anubis, (880, 260))
    Pyramid = pygame.image.load('images/pyramid2.png')
    Pyramid = pygame.transform.scale(Pyramid, (80, 80))
    MySurface.blit(Pyramid, (880, 370))
    Save = font.render("Save", 1, BLANC)            # On affiche les boutons
    Rotation = font.render("Rotation", 1, BLANC)
    pygame.draw.rect(MySurface, GRIS3, (675, 475, 180, 50), 3)
    pygame.draw.rect(MySurface, GRIS3, (880, 475, 180, 50), 3)
    MySurface.blit(Save, (928, 485))
    MySurface.blit(Rotation, (695, 485))
    Nb_Red_Pharaoh = font.render("X " + str(Red_Pharaoh), 1, BLANC)     # On affiche le nombre de pions restant
    MySurface.blit(Nb_Red_Pharaoh, (780, 70))
    Nb_Red_Scarab = font.render("X " + str(Red_Scarab), 1, BLANC)
    MySurface.blit(Nb_Red_Scarab, (780, 180))
    Nb_Red_Anubis = font.render("X " + str(Red_Anubis), 1, BLANC)
    MySurface.blit(Nb_Red_Anubis, (780, 290))
    Nb_Red_Pyramid = font.render("X " + str(Red_Pyramid), 1, BLANC)
    MySurface.blit(Nb_Red_Pyramid, (780, 400))
    Nb_Blue_Pharaoh = font.render("X " + str(Blue_Pharaoh), 1, BLANC)
    MySurface.blit(Nb_Blue_Pharaoh, (985, 70))
    Nb_Blue_Scarab = font.render("X " + str(Blue_Scarab), 1, BLANC)
    MySurface.blit(Nb_Blue_Scarab, (985, 180))
    Nb_Blue_Anubis = font.render("X " + str(Blue_Anubis), 1, BLANC)
    MySurface.blit(Nb_Blue_Anubis, (985, 290))
    Nb_Blue_Pyramid = font.render("X " + str(Blue_Pyramid), 1, BLANC)
    MySurface.blit(Nb_Blue_Pyramid, (985, 400))
    MySurface.blit(current, (x, y))     # Pion actuellement sélectionnée
    pygame.display.flip()
    return Red_Pharaoh, Blue_Pharaoh, Red_Scarab, Blue_Scarab, Red_Pyramid, Blue_Pyramid, Red_Anubis, Blue_Anubis


def lauch_lasers(grid, MySurface, player):      # Gère le laser
    Laser = [[0 for k in range(10)] for l in range(8)]  # Création de la grille
    End = False
    if player == 1:
        if grid[0][0][2] == 1:      # Selon la rotation du Sphinx
            x, y = 0, 1 # Déplacement du laser vers la droite
        elif grid[0][0][2] == 2:
            x, y = 1, 0 # Déplacement du laser vers le bas
        i, j = 0, 0 # Débute à 0, 0
    elif player == 2:
        if grid[7][9][2] == 0:      # Selon la rotation du Sphinx
            x, y = -1, 0    # Déplacement du laser vers le haut
        elif grid[7][9][2] == 3:
            x, y = 0, -1    # Déplacement du laser vers la gauche
        i, j = 7, 9 # Débute à 7, 9
    while End != True:
        i, j = i+x, j+y # Déplacement du laser
        if x != 0:
            Laser[i][j] = 1 # Déplacement vertical
        elif y != 0:
            Laser[i][j] = 2 # Déplacement horizontal
        End, x, y = Collision_laser(grid, Laser, i, j, x, y)    # On vérifie si un pion est touché
        if (i <= 0 and x == -1) or (i >= 7 and x == 1) or (j <= 0 and y == -1) or (j >= 9 and y == 1):  # Si le laser sort de la zone de jeu
            End = True
    return Laser


def Collision_laser(grid, Laser, i, j, x, y):   # Vérifie si le laser touche une pièce
    if grid[i][j][1] == 1:  # Si le Pharaon est touché
        grid[i][j] = [0, 0, 0]  # On le détruit
        return True, x, y
    elif grid[i][j][1] == 5:    # Si le Sphinx est touché
        return True, x, y   # On stop le laser
    elif grid[i][j][1] == 3:    # Si l'Anubis est touché
        if (x == 1 and grid[i][j][2] == 0) or (x == -1 and grid[i][j][2] == 2) or (y == 1 and grid[i][j][2] == 3) or (y == -1 and grid[i][j][2] == 1):  # Si il prend le laser de face
            return True, x, y   # Arrète le laser
        else:
            grid[i][j] = [0, 0, 0]  # Sinon est détruit
            return True, x, y
    elif grid[i][j][1] == 4:    # Si la Pyramid est touchée
        if (x == 1 and grid[i][j][2] == 2) or (x == -1 and grid[i][j][2] == 0) or (y == 1 and grid[i][j][2] == 1) or (y == -1 and grid[i][j][2] == 3) or \
                (x == 1 and grid[i][j][2] == 3) or (x == -1 and grid[i][j][2] == 1) or (y == 1 and grid[i][j][2] == 2) or (y == -1 and grid[i][j][2] == 0): # Si ce n'est pas sur le miroir
            grid[i][j] = [0, 0, 0]  # Il est détruit
            return True, x, y
        else:   # Si c'est sur le miroir
            if (x == 1 and grid[i][j][2] == 0) or (x == -1 and grid[i][j][2] == 2) or (y == 1 and grid[i][j][2] == 3) or (y == -1 and grid[i][j][2] == 1):  # Premier côté du miroir
                if x != 0:              # Réflection du laser
                    x, y = 0, -x
                    return False, x, y
                elif y != 0:
                    x, y = y, 0
                    return False, x, y
            elif (x == 1 and grid[i][j][2] == 1) or (x == -1 and grid[i][j][2] == 3) or (y == 1 and grid[i][j][2] == 0) or (y == -1 and grid[i][j][2] == 2):    # Second côté du miroir
                if x != 0:              # Réflection du laser
                    x, y = 0, x
                    return False, x, y
                elif y != 0:
                    x, y = -y, 0
                    return False, x, y
    elif grid[i][j][1] == 2:    # Si le Scarab est touché
        if (x == 1 and grid[i][j][2] == 0) or (x == -1 and grid[i][j][2] == 2) or (y == 1 and grid[i][j][2] == 3) or (y == -1 and grid[i][j][2] == 1) or \
                (x == 1 and grid[i][j][2] == 2) or (x == -1 and grid[i][j][2] == 0) or (y == 1 and grid[i][j][2] == 1) or (y == -1 and grid[i][j][2] == 3): # Côté 1 et 3 du miroir
            if x != 0:                  # Réflection du laser
                x, y = 0, -x
                return False, x, y
            elif y != 0:
                x, y = y, 0
                return False, x, y
        elif (x == 1 and grid[i][j][2] == 3) or (x == -1 and grid[i][j][2] == 1) or (y == 1 and grid[i][j][2] == 2) or (y == -1 and grid[i][j][2] == 0) or \
                (x == 1 and grid[i][j][2] == 1) or (x == -1 and grid[i][j][2] == 3) or (y == 1 and grid[i][j][2] == 0) or (y == -1 and grid[i][j][2] == 2): # Côté 2 et 4 du miroir
            if x != 0:                  # Réflection du laser
                x, y = 0, x
                return False, x, y
            elif y != 0:
                x, y = -y, 0
                return False, x, y
    return False, x, y


def draw_laser(grid, MySurface, Laser): # Affiche le laser
    for i in range(8):  # Pour chaque case
        for j in range(10):
            if Laser[i][j] == 1 and grid[i][j][1] == 0:     # Si le laser est vertical et pas sur une pièce
                pygame.draw.line(MySurface, ROUGE, (50 + j*60, 20 + i*60), (50 + j*60, 20 + i*60+60), 5)
            elif Laser[i][j] == 2 and grid[i][j][1] == 0:   # Si le laser est horizontal et pas sur une pièce
                pygame.draw.line(MySurface, ROUGE, (20 + j*60, 50 + i*60), (20 + j*60+60, 50 + i*60), 5)
            elif (grid[i][j][1] == 4 or grid[i][j][1] == 2) and Laser[i][j] != 0: # Si le laser se trouve sur un Scarab ou une Pyramid
                Reflect_Laser = pygame.image.load('images/Laser.png')
                Reflect_Laser = pygame.transform.scale(Reflect_Laser, (60, 60))
                if grid[i][j][1] == 4:              # On affiche le laser sur la pyramid avec le bon angle
                    Reflect_Laser = pygame.transform.rotate(Reflect_Laser, (-90) * grid[i][j][2])
                elif grid[i][j][1] == 2:        #Scarab
                    Pos = False
                    if j-1 > 0 and Pos == False:            # Si la case à gauche est dans la zone de jeu
                        if (grid[i][j][2] == 0 or grid[i][j][2] == 2) and Laser[i][j-1] != 0:       # Orientation 0 ou 2 de la pièce
                            Reflect_Laser = pygame.transform.rotate(Reflect_Laser, (-90) * 0)
                            Pos = True
                        elif (grid[i][j][2] == 1 or grid[i][j][2] == 3) and Laser[i][j-1] != 0:     # Orientation 1 ou 3 de la pièce
                            Reflect_Laser = pygame.transform.rotate(Reflect_Laser, (-90) * ((grid[i][j][2] % 2) + 2))
                            Pos = True
                    if j+1 < 10 and Pos == False:           # Si la case à droite est dans la zone de jeu
                        if (grid[i][j][2] == 0 or grid[i][j][2] == 2) and Laser[i][j+1] != 0:       # Orientation 0 ou 2 de la pièce
                            Reflect_Laser = pygame.transform.rotate(Reflect_Laser, (-90) * ((grid[i][j][2] % 2) + 2))
                        elif (grid[i][j][2] == 1 or grid[i][j][2] == 3) and Laser[i][j+1] != 0:     # Orientation 1 ou 3 de la pièce
                            Reflect_Laser = pygame.transform.rotate(Reflect_Laser, (-90) * 0)
                MySurface.blit(Reflect_Laser, (20 + 60 * j, 20 + 60 * i))
    pygame.display.flip()
    pygame.time.wait(4000)  # On pause le programme


def winner(grid, MySurface):    # Vérifie si un joueur à gagné
    player1 = False
    player2 = False
    for i in range(8):  # Pour chaque case
        for j in range(10):
            if grid[i][j][0] == 1 and grid[i][j][1] == 1:   # Si le joueur 1 a encore son Pharaoh
                player1 = True
            elif grid[i][j][0] == 2 and grid[i][j][1] == 1: # Si le joueur 2 a encore son Pharaoh
                player2 = True
    if player1 != True:     # On enregistre le gagnant
        winner = 2
    elif player2 != True:
        winner = 1
    if player1 != True or player2 != True:
        MySurface.fill(NOIR)                                    # On affiche le gagnat et propose de rejouer
        Victory = pygame.image.load('images/Victory.jpg')
        Victory = pygame.transform.scale(Victory, (900, 550))
        MySurface.blit(Victory, (0, 0))
        Victory = fontmenue.render("Le joueur " + str(winner) + " a gagne !", 1, (255, 255, 255))
        MySurface.blit(Victory, (100, 30))
        Replay = fontmenue.render("Rejouer ?", 1, BLANC)
        MySurface.blit(Replay, (570, 370))
        No = fontmenue.render("Non", 1, BLANC)
        MySurface.blit(No, (530, 450))
        Yes = fontmenue.render("Oui", 1, BLANC)
        MySurface.blit(Yes, (740, 450))
        pygame.display.flip()
        End = False
        while End != True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    poseX, poseY = event.pos
                    if poseY >= 465 and poseY <= 520:       # Si on ne rejoue pas
                        if poseX >= 520 and poseX <= 620:
                            return 0, 0     # Quitte le jeu
                        elif poseX >= 730 and poseX <= 810:     # Si on rejoue
                            return 1, 0     # Relance l'accueil
                if event.type == QUIT:
                    return 0, 0
    else:
        return 1, 1     # Sinon on continue la partie


while continuer:        # Tant que le jeu n'est pas fermé
    player = 1
    pygame.mixer.init()     # On joue en boucle la musique
    son = pygame.mixer.Sound('sounds/son.wav')             # Musique "LHS - Reloaded Installer #17" Lien youtube : https://www.youtube.com/watch?v=SnDYXnDKJ2M
    son.play(loops=-1, maxtime=0, fade_ms=1000)

    continuer_accueil = 1

    # BOUCLE D'ACCUEIL
    while continuer_accueil:
        maSurface = pygame.display.set_mode((1233, 755))                    # On affiche les images, boutons, ... de l'accueil
        pygame.display.set_caption('Khet')

        accueil = pygame.image.load("images/fond.jpg").convert()
        accueil = pygame.transform.scale(accueil, (1233, 755))
        maSurface.blit(accueil, (0, 0))

        texteSurface = fontObj.render('KHET 18.0', True, ROSE)
        texteRect = texteSurface.get_rect()
        texteRect.topleft = (480, 10)

        pygame.draw.rect(maSurface, (170, 0, 0), (400, 160, 20 * 23, 22 * 26), 10)
        menue = pygame.draw.rect(maSurface, NOIR, (400, 160, 20 * 23, 22 * 26), 0)

        #case menue
        pygame.draw.rect(maSurface, GRIS3, (480, 200, 300, 50), 3)
        case1 = pygame.draw.rect(maSurface, NOIR, (480, 200, 300, 50), 0)

        pygame.draw.rect(maSurface, GRIS3, (480, 300, 300, 50), 3)
        case2 = pygame.draw.rect(maSurface, NOIR, (480, 300, 300, 50), 0)

        pygame.draw.rect(maSurface, GRIS3, (480, 400, 300, 50), 3)
        case3 = pygame.draw.rect(maSurface, NOIR, (480, 400, 300, 50), 0)

        pygame.draw.rect(maSurface, GRIS3, (453, 500, 355, 50), 3)
        case4 = pygame.draw.rect(maSurface, NOIR, (453, 500, 355, 50), 0)

        pygame.draw.rect(maSurface, GRIS3, (436, 600, 90, 90), 3)
        case5 = pygame.draw.rect(maSurface, NOIR, (436, 600, 90, 90), 0)

        pygame.draw.rect(maSurface, GRIS3, (586, 600, 90, 90), 3)
        case6 = pygame.draw.rect(maSurface, NOIR, (586, 600, 90, 90), 0)

        pygame.draw.rect(maSurface, GRIS3, (736, 600, 90, 90), 3)
        case7 = pygame.draw.rect(maSurface, NOIR, (736, 600, 90, 90), 0)


        Movement = fontmenue.render("Classic", 1, BLANC)
        maSurface.blit(Movement, (550, 183))
        Rotation = fontmenue.render("Imhotep", 1, BLANC)
        maSurface.blit(Rotation, (550, 283))
        Rotation = fontmenue.render("Dynasty", 1, BLANC)
        maSurface.blit(Rotation, (550, 383))
        Rotation = fontmenue.render("Creer un niveau", 1, BLANC)
        maSurface.blit(Rotation, (460, 483))
        Rotation = fontmenue2.render("1", 10, BLANC)
        maSurface.blit(Rotation, (468, 587))
        Rotation = fontmenue2.render("2", 10, BLANC)
        maSurface.blit(Rotation, (613, 587))
        Rotation = fontmenue2.render("3", 10, BLANC)
        maSurface.blit(Rotation, (764, 587))
        maSurface.blit(texteSurface, texteRect)
        pygame.display.flip()
        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # Si l'utilisateur quitte, on met les variables
            # de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0

            if event.type == MOUSEBUTTONDOWN:
                    poseX, poseY = event.pos
                    if poseX >= 480 and poseX <= 780:
                        if poseY >= 200 and poseY <= 250:   # Sélection niveau Classic
                            continuer_accueil = 0
                            continuer_jeu = 1
                            selectgrid = 1
                            case1 = pygame.draw.rect(maSurface, ROSE, (480, 200, 300, 50), 0)
                        elif poseY >= 300 and poseY <= 350: # Sélection niveau Imhotep
                            continuer_accueil = 0
                            continuer_jeu = 1
                            case2 = pygame.draw.rect(maSurface, ROSE, (480, 300, 300, 50), 0)
                            selectgrid = 2
                        elif poseY >= 400 and poseY <= 450: # Sélection niveau Dynasty
                            continuer_accueil = 0
                            continuer_jeu = 1
                            case3 = pygame.draw.rect(maSurface, ROSE, (480, 400, 300, 50), 0)
                            selectgrid = 3

                    if poseX >= 453 and poseX <= 808:       # Sélection Création de niveau
                        if poseY >= 500 and poseY <= 550:
                            continuer_accueil = 0
                            continuer_jeu = 1
                            case4 = pygame.draw.rect(maSurface, ROSE, (453, 500, 355, 50), 0)
                            selectgrid = 4

                    if poseY >= 600 and poseY <= 690:
                        if poseX >= 436 and poseX <= 526 and os.path.exists("saves/1.txt"):   # Charge la sauvegarde 1 si elle existe
                            continuer_accueil = 0
                            continuer_jeu = 1
                            case5 = pygame.draw.rect(maSurface, ROSE, (436, 600, 90, 90), 0)
                            selectgrid = 5
                        elif poseX >= 586 and poseX <= 676 and os.path.exists("saves/2.txt"): # Charge la sauvegarde 2 si elle existe
                            continuer_accueil = 0
                            continuer_jeu = 1
                            case6 = pygame.draw.rect(maSurface, ROSE, (586, 600, 90, 90), 0)
                            selectgrid = 6
                        elif poseX >= 736 and poseX <= 826 and os.path.exists("saves/3.txt"): # Charge la sauvegarde 3 si elle existe
                            continuer_accueil = 0
                            continuer_jeu = 1
                            case7 = pygame.draw.rect(maSurface, ROSE, (736, 600, 90, 90), 0)
                            selectgrid = 7
    pygame.display.flip()


    while continuer_jeu:    # Lance le jeu
        grid, base = newgrid()
        if selectgrid == 4:
            continuer, continuer_jeu = Creation_level() # Création du niveau
            continuer_accueil = 1   # On revient sur l'accueil
            continuer_jeu = 0
        elif selectgrid == 5:       # Chargement sauvegarde 1
            file = open('saves/1.txt', 'r')
            grid = loadGrid(file)
        elif selectgrid == 6:       # Chargement sauvegarde 2
            file = open('saves/2.txt', 'r')
            grid = loadGrid(file)
        elif selectgrid == 7:       # Chargement sauvegarde 3
            file = open('saves/3.txt', 'r')
            grid = loadGrid(file)
        else:
            grid = loadconfiguration(selectgrid)    # Choix du niveau
        MySurface = pygame.display.set_mode((900, 550))
        pygame.display.set_caption('KHET 18.0')

        while continuer_jeu:
            continuer, continuer_jeu = played(MySurface, grid, player, base)    # Tour du joueur
            drawngameboard(MySurface, grid, base)   # Affiche le jeu
            if continuer_jeu: # Si on a pas quitté entre temps
                Laser = lauch_lasers(grid, MySurface, player)   # Tire le laser du joueur
                draw_laser(grid, MySurface, Laser)  # L'affiche
                continuer, continuer_jeu = winner(grid, MySurface)  # Vérifie si une joueur à gagné
                player = changePlayer(player)   # Change de joueur
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer_jeu = 0
                    continuer = 0

pygame.quit()