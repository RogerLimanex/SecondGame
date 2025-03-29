import pygame

window = pygame.display.set_mode([960, 540])

pygame.display.set_caption('Second Game')

background_image = pygame.image.load('D:/Jogos/AtividadePratica/asset/space bg game.png')

player_ship = pygame.image.load('D:/Jogos/AtividadePratica/asset/sprite_nave_pequena.png')

enemy_ship = pygame.image.load('D:/Jogos/AtividadePratica/asset/nave_inimiga_pequena.png')

#posição da nave player
pos_y_player = 435
pos_x_player = 425
vel_nave_player = 10

loop = True

while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    keys = pygame.key.get_pressed()

    # Movimentação do player principal do jogo

    # Se pressionar a seta para cima, a nave se moverá para cima
    if keys[pygame.K_UP]:
        pos_y_player -= vel_nave_player
    # Se pressionar a seta para baixo, a nave se moverá para baixo
    if keys[pygame.K_DOWN]:
        pos_y_player += vel_nave_player
    # Se pressionar a seta para a esquerda, a nave se moverá para a esquerda
    if keys[pygame.K_LEFT]:
        pos_x_player -= vel_nave_player
    # Se pressionar a seta para a direita, a nave se moverá para a direita
    if keys[pygame.K_RIGHT]:
        pos_x_player += vel_nave_player

    window.blit(background_image, (0, 0))
    window.blit(player_ship, (pos_x_player, pos_y_player))
    window.blit(enemy_ship, (435, 50))



    pygame.display.update()
