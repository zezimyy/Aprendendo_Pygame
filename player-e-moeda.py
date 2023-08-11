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

    #Player
    player = pygame.draw.rect(tela, (0, 0, 255), (largura/2-32, altura/2-32, 32, 32))

    #moeda
    moeda = pygame.draw.circle(tela, (255, 0, 255), (60, 150), 5)
    
    #Atualizar a tela a cada iteração
    pygame.display.update()
