import pygame
import pygame.display
from pygame import mixer
from time import sleep
from random import randint
from random import random

# posição e velocidade da nave player
pos_y_player = 440
pos_x_player = 425
speed_ship_player = 5

# posição e velocidade da nave inimigo
pos_y_enemy = 440
pos_x_enemy = 50
speed_ship_enemy = 5

# posição e velocidade do missil
pos_y_missil = 450
pos_x_missil = 430
speed_x_missil = 10

pontuacao = 0

pygame.init()
mixer.init()

# Carregamento e inserção dos sons do jogo
# som_missil = mixer.music.load('nome do laser')
# som_explosao = pygame.mixer.Sound('nome do som da explosao')

# Carregamento e inserção das imagens do jogo
background_image = pygame.image.load('D:/Jogos/AtividadePratica/asset/space bg game.png')
player_ship = pygame.image.load('D:/Jogos/AtividadePratica/asset/sprite_nave_pequena.png')
enemy_ship = pygame.image.load('D:/Jogos/AtividadePratica/asset/nave_inimiga_pequena.png')
shot = pygame.image.load('D:/Jogos/AtividadePratica/asset/missil_pequeno.png')
shot = pygame.transform.scale(shot, (30, 30)) # Transforma o tamanho do objeto

x, y = (960, 540)
window = pygame.display.set_mode([x, y])
pygame.display.set_caption('Retorno dos Aliens')
pygame.display.set_caption('Second Game')

tiro_alvo = False

loop = True

while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    keys = pygame.key.get_pressed()

    # Movimentação do player principal do jogo

    # Se pressionar a seta para cima, a nave se moverá para cima
    if keys[pygame.K_UP]:
        pos_y_player -= speed_ship_player
    # Se pressionar a seta para baixo, a nave se moverá para baixo
    if keys[pygame.K_DOWN]:
        pos_y_player += speed_ship_player
    # Se pressionar a seta para a esquerda, a nave se moverá para a esquerda
    if keys[pygame.K_LEFT]:
        pos_x_player -= speed_ship_player
    # Se pressionar a seta para a direita, a nave se moverá para a direita
    if keys[pygame.K_RIGHT]:
        pos_x_player += speed_ship_player

    if pos_y_player <= -10:
        pos_y_player = -10
    if pos_y_player >= 440:
        pos_y_player = 440
    if pos_x_player <= 0:
        pos_x_player = 0
    if pos_x_player >= 870:
        pos_x_player = 870

    window.blit(background_image, (0, 0))
    window.blit(player_ship, (pos_x_player, pos_y_player))
    window.blit(enemy_ship, (440, 50))

    pygame.display.update()
