import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#Tela 
largura = 400
altura = 300
tela = pygame.display.set_mode((largura, altura))

#Posição do player
x = 184
y = 118

#Criação da variavel fps
fps = pygame.time.Clock()

#Loop Principal
while True:

    #Limite de velocidade do FPS
    fps.tick(60)

    #Limpar a tela a cada iteração
    tela.fill((0,0,0))

    for event in pygame.event.get():

        #Fechar a tela
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        #Movimentação via teclado Basica
        '''if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 1
            if event.key == K_d:
                x = x + 1
            if event.key == K_w:
                y = y - 1
            if event.key == K_s:
                y = y + 1'''
    
    #Movimentação via teclado Normal
    if pygame.key.get_pressed()[K_w]:
        y-=1
    if pygame.key.get_pressed()[K_a]:
        x-=1
    if pygame.key.get_pressed()[K_s]:
        y+=1
    if pygame.key.get_pressed()[K_d]:
        x+=1

    #Player
    player = pygame.draw.rect(tela, (0, 0, 255), (x, y, 32, 32))
    
    #Se o player passar do limite da tela, ele retorna ao y = 0
    if y > altura:
        y = 0

    #Moeda
    moeda = pygame.draw.circle(tela, (255, 0, 255), (60, 150), 5)
    
    #Atualizar a tela a cada iteração
    pygame.display.update()
