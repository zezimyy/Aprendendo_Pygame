import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#tela 
largura = 400
altura = 300
tela = pygame.display.set_mode((largura, altura))

while True:
    for event in pygame.event.get():

        #Fechar a tela
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    #Atualizar a tela a cada iteração
    pygame.display.update()
