import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

#texto do jogo
pygame.display.set_caption('jogo de andre!')

#Pontos ao colidir com moeda
ponto = 0

#Posição moeda
x_moeda = random.randint(16, 384)
y_moeda = random.randint(16, 284)

#Tela 
largura = 400
altura = 300
tela = pygame.display.set_mode((largura, altura))

#Posição do player
x_player= 184
y_player = 118

#Criação da variavel fps
fps = pygame.time.Clock()

fonte = pygame.font.SysFont("Arial", 25, False, False)

#Loop Principal
while True:

    #Limite de velocidade do FPS
    fps.tick(60)

    #Limpar a tela a cada iteração
    tela.fill((0,0,0))

    #Formatacao e renderização de pontos
    mensagem = f"Pontos: {ponto}"
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))

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
        y_player-=1
    if pygame.key.get_pressed()[K_a]:
        x_player-=1
    if pygame.key.get_pressed()[K_s]:
        y_player+=1
    if pygame.key.get_pressed()[K_d]:
        x_player+=1

    #Player
    player = pygame.draw.rect(tela, (0, 0, 255), (x_player, y_player, 32, 32))
    
    #Se o player passar do limite da tela, ele retorna ao y = 0
    if y_player > altura:
        y_player = 0
    if x_player > largura:
        x_player = 0

    #Moeda
    moeda = pygame.draw.circle(tela, (255, 0, 255), (x_moeda, y_moeda), 5)

    #Colisão entre Player e Moeda
    if player.colliderect(moeda):
        x_moeda = random.randint(16, 384)
        y_moeda = random.randint(16, 284)
        ponto+=1
        print("pontos: {}".format(ponto))

    #Atualizar a tela para mostrar os pontos
    tela.blit(texto_formatado, (300, 0))
    
    #Atualizar a tela a cada iteração
    pygame.display.update()
