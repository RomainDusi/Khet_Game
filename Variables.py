import os
import pygame, sys
from pygame.locals import *

pygame.init()

font = pygame.font.Font(None, 48)
font2 = pygame.font.Font(None, 36)
font3 = pygame.font.Font(None, 70)

continuer = 1
continuer_accueil = 1
continuer_jeu = 0

ROSE = (255,20,127)
BLEU = (0,0,255)
GRIS = (118, 111, 100)
GRIS2 = (143, 143, 143)
GRIS3 = (69, 69, 69)
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)

print(os.getcwd())
fontObj = pygame.font.Font('fonts/Sketch3D.otf', 70)
fontmenue = pygame.font.Font('fonts/BADGRUNGE.ttf', 70)
fontmenue2 = pygame.font.Font('fonts/BADGRUNGE.ttf', 100)