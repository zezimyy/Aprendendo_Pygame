import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

#Som da moeda
"""som_moeda = pygame.mixer.music.load("8_bit_click.wav")"""
som_moeda = pygame.mixer.Sound("8_bit_click.wav")



#controle da movimentação constante da cobra
velocidade = 1
controle_x = velocidade
controle_y = 0


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

#corpo cobra
lista_corpo = []
comprimento_inicial = 5

#Função criar corpo da cobra
def aumentar_cobra(lista_corpo):
    for XeY in lista_corpo:
        pygame.draw.rect(tela, (0,0,255), (XeY[0], XeY[1], 20, 20))

#Loop Principal
while True:

    #Limite de velocidade do FPS
    fps.tick(80)

    #Limpar a tela a cada iteração
    tela.fill((255,255,255))

    #Formatacao e renderização de pontos
    mensagem = f"Pontos: {ponto}"
    texto_formatado = fonte.render(mensagem, False, (0, 0, 0))

    for event in pygame.event.get():

        #Fechar a tela
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        #Movimentação via teclado Basica
        if event.type == KEYDOWN:
            if event.key == K_a:
                if controle_x == velocidade:
                    pass
                else:
                    controle_x = -velocidade
                    controle_y = 0

            if event.key == K_d:
                if controle_x == -velocidade:
                    pass
                else:
                    controle_x = velocidade
                    controle_y = 0

            if event.key == K_w:
                if controle_y == velocidade:
                    pass
                else:
                    controle_y = -velocidade
                    controle_x = 0

            if event.key == K_s:
                if controle_y == -velocidade:
                    pass
                else:
                    controle_y = velocidade
                    controle_x = 0

    #movimentação permanente
    x_player = x_player + controle_x
    y_player = y_player + controle_y
    
    #Movimentação via teclado Normal
    '''if pygame.key.get_pressed()[K_w]:
        y_player-=1
    if pygame.key.get_pressed()[K_a]:
        x_player-=1
    if pygame.key.get_pressed()[K_s]:
        y_player+=1
    if pygame.key.get_pressed()[K_d]:
        x_player+=1'''

    #Player
    player = pygame.draw.rect(tela, (0, 0, 255), (x_player, y_player, 20, 20))
    
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
        comprimento_inicial+=5

        #Tocar som da moeda
        '''pygame.mixer.music.play(0)'''
        som_moeda.play()

    #cabeca cobra
    lista_cabeca = []
    lista_cabeca.append(x_player)
    lista_cabeca.append(y_player)

    #corpo cobra
    lista_corpo.append(lista_cabeca)
    aumentar_cobra(lista_corpo)

    #limitar tamanho cobra
    if len(lista_corpo) > comprimento_inicial:
        del lista_corpo[0]

    #limitar tamanho cobra
    '''if len(lista_corpo) > ponto:
        del lista_corpo[0]'''

    #Atualizar a tela para mostrar os pontos
    tela.blit(texto_formatado, (300, 0))
    
    #Atualizar a tela a cada iteração
    pygame.display.update()
