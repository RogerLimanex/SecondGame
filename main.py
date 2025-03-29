# from code.Game import Game
#
# game = Game()
# game.run()

import pygame

window = pygame.display.set_mode([960, 540])

pygame.display.set_caption('Second Game')

background_image = pygame.image.load('D:/Jogos/AtividadePratica/asset/space bg game.png')

player_ship = pygame.image.load('D:/Jogos/AtividadePratica/asset/sprite_nave_pequena.png')

#posição da nave player
pos_y_player = 400
pos_x_player = 420
vel_nave_player = 10

loop = True

while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    teclas = pygame.key.get_pressed()

    window.blit(background_image, (0, 0))
    window.blit(player_ship, (pos_y_player, pos_x_player))

    pygame.display.update()
