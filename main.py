import pygame
from random import randint

# Inicializa o pygame
pygame.init()

# Configuração da tela
x, y = (960, 540)
janela = pygame.display.set_mode([x, y])
pygame.display.set_caption('Retorno dos Aliens')

# Carrega imagens (fora do loop principal)
background_image = pygame.image.load('D:/Jogos/AtividadePratica/asset/space bg game.png')
player_ship = pygame.image.load('D:/Jogos/AtividadePratica/asset/sprite_nave_pequena.png')
enemy_ship = pygame.image.load('D:/Jogos/AtividadePratica/asset/nave_inimiga_pequena.png')
shot = pygame.image.load('D:/Jogos/AtividadePratica/asset/missil_pequeno.png')
shot = pygame.transform.scale(shot, (30, 30))

# Fonte para exibir a pontuação e vida
fonte = pygame.font.Font(None, 36)

# Posições iniciais
pos_x_player, pos_y_player = 425, 440
pos_x_enemy, pos_y_enemy = 50, 0
pos_x_missil, pos_y_missil = pos_x_player, pos_y_player

# Velocidades
speed_ship_player = 10  # Aumentei para 10
speed_ship_enemy = 5
speed_x_missil = 10
tiro_alvo = False

# Variáveis do jogo
pontuacao = 0
vida = 100  # Inicializa a vida do jogador
colisao_ocorrida = False  # Flag para evitar múltiplas reduções de vida
loop = True

# Função de colisão
def colisoes():
    global pontuacao, pos_x_enemy, pos_y_enemy, pos_x_missil, pos_y_missil, tiro_alvo, vida, colisao_ocorrida

    if player_rect.colliderect(inimigo_rect) and not colisao_ocorrida:
        vida -= 20  # Reduz 20 pontos de vida ao colidir com o inimigo
        colisao_ocorrida = True  # Marca que a colisão já ocorreu
    elif not player_rect.colliderect(inimigo_rect):
        colisao_ocorrida = False  # Reseta a flag quando não há colisão
    if tiro_alvo and tiro_rect.colliderect(inimigo_rect):
        pontuacao += 1
        pos_y_enemy = -50  # Reseta posição do inimigo para cima
        pos_x_enemy = randint(50, 870)  # Randomiza posição X
        tiro_alvo = False  # Reseta tiro
        pos_y_missil = pos_y_player
        pos_x_missil = pos_x_player

# Loop principal do jogo
while loop:
    pygame.time.delay(30)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    # Movimentação do inimigo
    pos_y_enemy += speed_ship_enemy
    if pos_y_enemy > 530:
        pontuacao -= 5  # Reduz pontuação se o inimigo sair da tela sem ser destruído
        pos_y_enemy = -50
        pos_x_enemy = randint(50, 870)

    # Captura comandos do teclado
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] and pos_y_player > 0:
        pos_y_player -= speed_ship_player
    if comandos[pygame.K_DOWN] and pos_y_player < 500:
        pos_y_player += speed_ship_player
    if comandos[pygame.K_LEFT] and pos_x_player > 0:
        pos_x_player -= speed_ship_player
    if comandos[pygame.K_RIGHT] and pos_x_player < 870:
        pos_x_player += speed_ship_player
    if comandos[pygame.K_SPACE] and not tiro_alvo:
        tiro_alvo = True
        pos_x_missil = pos_x_player + 15
        pos_y_missil = pos_y_player

    # Movimento do míssil
    if tiro_alvo:
        pos_y_missil -= speed_x_missil
        if pos_y_missil < 0:
            tiro_alvo = False

    # Atualiza os retângulos de colisão
    player_rect = player_ship.get_rect(topleft=(pos_x_player, pos_y_player))
    inimigo_rect = enemy_ship.get_rect(topleft=(pos_x_enemy, pos_y_enemy))
    tiro_rect = shot.get_rect(topleft=(pos_x_missil, pos_y_missil))

    colisoes()

    # Renderiza as imagens
    janela.blit(background_image, (0, 0))
    janela.blit(player_ship, (pos_x_player, pos_y_player))
    janela.blit(enemy_ship, (pos_x_enemy, pos_y_enemy))
    if tiro_alvo:
        janela.blit(shot, (pos_x_missil, pos_y_missil))

    # Exibe a pontuação e vida na tela
    texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, (255, 255, 255))
    texto_vida = fonte.render(f'Vida: {vida}', True, (255, 0, 0))
    janela.blit(texto_pontuacao, (20, 20))
    janela.blit(texto_vida, (20, 50))

    pygame.display.update()

    # Verifica se a vida chegou a 0 e encerra o jogo
    if vida <= 0:
        loop = False

# Exibe o resultado final na tela
janela.fill((0, 0, 0))  # Tela preta para mostrar o resultado
mensagem = fonte.render('GAME OVER!', True, (255, 0, 0))
janela.blit(mensagem, (x // 2 - 100, y // 2))
pygame.display.update()
pygame.time.delay(3000)  # Mantém a mensagem por 3 segundos

pygame.quit()


# import pygame
# from random import randint
#
# # Inicializa o pygame
# pygame.init()
#
# # Configuração da tela
# x, y = (960, 540)
# janela = pygame.display.set_mode([x, y])
# pygame.display.set_caption('Retorno dos Aliens')
#
# # Carrega imagens (fora do loop principal)
# background_image = pygame.image.load('D:/Jogos/AtividadePratica/asset/space bg game.png')
# player_ship = pygame.image.load('D:/Jogos/AtividadePratica/asset/sprite_nave_pequena.png')
# enemy_ship = pygame.image.load('D:/Jogos/AtividadePratica/asset/nave_inimiga_pequena.png')
# shot = pygame.image.load('D:/Jogos/AtividadePratica/asset/missil_pequeno.png')
# shot = pygame.transform.scale(shot, (30, 30))
#
# # Posições iniciais
# pos_x_player, pos_y_player = 425, 440
# pos_x_enemy, pos_y_enemy = 50, 0
# pos_x_missil, pos_y_missil = pos_x_player, pos_y_player
#
# # Velocidades
# speed_ship_player = 10
# speed_ship_enemy = 5
# speed_x_missil = 10
# tiro_alvo = False
#
# pontuacao = 0
# loop = True
#
# # Função de colisão
# def colisoes():
#     global pontuacao, pos_x_enemy, pos_y_enemy, pos_x_missil, pos_y_missil, tiro_alvo
#
#     if player_rect.colliderect(inimigo_rect) or inimigo_rect.y > 500:
#         pontuacao -= 1
#         print("Pontuação:", pontuacao)
#         return True
#     elif tiro_rect.colliderect(inimigo_rect):
#         pontuacao += 1
#         pos_y_enemy = -50  # Reseta posição do inimigo para cima
#         pos_x_enemy = randint(50, 870)  # Randomiza posição X
#         print("Pontuação:", pontuacao)
#         tiro_alvo = False  # Reseta tiro
#         pos_y_missil = pos_y_player
#         pos_x_missil = pos_x_player
#         return True
#     return False
#
# # Loop principal do jogo
# while loop:
#     pygame.time.delay(30)  # Pequeno delay para otimizar FPS
#
#     # Eventos do Pygame
#     for events in pygame.event.get():
#         if events.type == pygame.QUIT:
#             loop = False
#
#     # Movimentação do inimigo
#     pos_y_enemy += speed_ship_enemy
#     if pos_y_enemy > 530:
#         pos_y_enemy = -50
#         pos_x_enemy = randint(50, 870)
#
#     # Captura comandos do teclado
#     comandos = pygame.key.get_pressed()
#     if comandos[pygame.K_UP] and pos_y_player > 0:
#         pos_y_player -= speed_ship_player
#     if comandos[pygame.K_DOWN] and pos_y_player < 500:
#         pos_y_player += speed_ship_player
#     if comandos[pygame.K_LEFT] and pos_x_player > 0:
#         pos_x_player -= speed_ship_player
#     if comandos[pygame.K_RIGHT] and pos_x_player < 870:
#         pos_x_player += speed_ship_player
#     if comandos[pygame.K_SPACE] and not tiro_alvo:
#         tiro_alvo = True
#         pos_x_missil = pos_x_player + 15
#         pos_y_missil = pos_y_player
#
#     # Movimento do míssil
#     if tiro_alvo:
#         pos_y_missil -= speed_x_missil
#         if pos_y_missil < 0:
#             tiro_alvo = False  # Reseta o tiro
#
#     # Atualiza os retângulos de colisão
#     player_rect = player_ship.get_rect(topleft=(pos_x_player, pos_y_player))
#     inimigo_rect = enemy_ship.get_rect(topleft=(pos_x_enemy, pos_y_enemy))
#     tiro_rect = shot.get_rect(topleft=(pos_x_missil, pos_y_missil))
#
#     colisoes()  # Verifica colisões
#
#     # Renderiza as imagens
#     janela.blit(background_image, (0, 0))
#     janela.blit(player_ship, (pos_x_player, pos_y_player))
#     janela.blit(enemy_ship, (pos_x_enemy, pos_y_enemy))
#     if tiro_alvo:
#         janela.blit(shot, (pos_x_missil, pos_y_missil))
#
#     pygame.display.update()
#
# # Exibe o resultado final
# if pontuacao < 0:
#     print("GAME OVER! Você perdeu!")
# else:
#     print("PARABÉNS! Você ganhou!")
#
# pygame.quit()



# import pygame
# import pygame.display
# from pygame import mixer
# from time import sleep
# from random import randint
# from random import random
#
# x, y = (960, 540)
# janela = pygame.display.set_mode([x, y])
# pygame.display.set_caption('Retorno dos Aliens')
#
# tiro_alvo = False
#
# # posição e velocidade da nave player
# pos_y_player = 440
# pos_x_player = 425
# speed_ship_player = 5
#
# # posição e velocidade da nave inimigo
# pos_y_enemy = 440
# pos_x_enemy = 50
# speed_ship_enemy = 5
#
# # posição e velocidade do missil
# pos_y_missil = 450
# pos_x_missil = 430
# speed_x_missil = 10
#
# pontuacao = 0
#
#
# def colisoes():
#     global pontuacao
#     global pos_y_enemy
#     global pos_x_enemy
#     global som_nave_colisao
#     global som_missil
#     global som_explosao
#
#     # Se o player principal colidir com a nave inimiga.
#     if player_rect.colliderect(inimigo_rect) or inimigo_rect.y > 500:
#         pontuacao -= 1
#         print(pontuacao)
#         return True
#     elif tiro_rect.colliderect(inimigo_rect):
#         pontuacao += 1
#         pos_y_enemy -= 1200
#         if pos_y_enemy < -1000:
#             random_y = randint(1, 440)
#             random_x = randint(1, 870)
#             pos_y_enemy -= 450
#             pos_y_enemy = random_y
#             pos_x_enemy = random_x
#         print(pontuacao)
#         som_explosao.play()
#         return True
#
#     else:
#         return False
#
#
# def resultado():
#     global pontuacao
#
#     if pontuacao < 0:
#         print('GAME OVER! Você perdeu o jogo!')
#     else:
#         print('PARABÉNS! Você ganhou o jogo!')
#
#
# loop = True
#
# while loop:
#     for events in pygame.event.get():
#         if events.type == pygame.QUIT:
#             loop = False
#
#         # Carregamento e inserção das imagens do jogo
#         background_image = pygame.image.load('D:/Jogos/AtividadePratica/asset/space bg game.png')
#         player_ship = pygame.image.load('D:/Jogos/AtividadePratica/asset/sprite_nave_pequena.png')
#         enemy_ship = pygame.image.load('D:/Jogos/AtividadePratica/asset/nave_inimiga_pequena.png')
#         shot = pygame.image.load('D:/Jogos/AtividadePratica/asset/missil_pequeno.png')
#         shot = pygame.transform.scale(shot, (30, 30))  # Transforma o tamanho do objeto
#
#         # Movimento do Inimigo
#
#         pos_y_enemy += 10
#
#         """print(pos_inimigo_y)
#         print(pos_y_missil)"""
#
#          if pos_y_enemy > 530:
#             random_y = randint(1, 440)
#             random_x = randint(1, 870)
#             pos_y_enemy -= 450
#             pos_y_enemy = random_y
#             pos_x_enemy = random_x
#
#         # Obtém todos os comandos pressionados no Teclado ao Jogar.
#         comandos = pygame.key.get_pressed()
#
#         # Verifica qual comando pressionado e lhe retorna uma ação.
#         if comandos[pygame.K_UP] and pos_y_player > 1:
#             # Faz a Nave Subir
#             pos_y_player -= speed_ship_player
#             if not tiro_alvo:
#                 pos_y_missil -= speed_x_missil
#                 vel_x_missil = 10
#
#         if comandos[pygame.K_DOWN] and pos_y_player < 440:
#             # Faz a Nave Descer
#             pos_y_player += speed_ship_player
#             if not tiro_alvo:
#                 pos_y_missil += speed_x_missil
#                 vel_x_missil = 10
#         if comandos[pygame.K_LEFT] and pos_x_player > 1:
#             # Faz a nave ir para esquerda
#             pos_x_player -= speed_ship_player
#             if not tiro_alvo:
#                 pos_x_missil -= speed_x_missil
#                 vel_x_missil = 10
#         if comandos[pygame.K_RIGHT] and pos_x_player < 870:
#             pos_x_player += speed_ship_player
#             if not tiro_alvo:
#                 tiro_alvo = False
#                 pos_x_missil += speed_x_missil
#                 vel_x_missil = 10
#         if comandos[pygame.K_SPACE]:
#             tiro_alvo = True
#             if tiro_alvo:
#                 vel_x_missil = 10
#                 pos_y_missil -= vel_x_missil
#             if pos_y_missil < 1:
#                 # Reseta o Míssil para poder ser atirado novamente.
#                 tiro_alvo = True
#                 pos_y_missil = pos_y_player
#                 pos_x_missil = pos_x_player
#                 vel_x_missil = 10
#
#         player_rect = player_ship.get_rect()
#         inimigo_rect = enemy_ship.get_rect()
#         tiro_rect = shot.get_rect()
#
#         player_rect.y = pos_y_player
#         player_rect.x = pos_x_player
#
#         inimigo_rect.y = pos_y_enemy
#         inimigo_rect.x = pos_x_enemy
#
#         tiro_rect.y = pos_y_missil
#         tiro_rect.x = pos_x_missil
#
#         colisoes()
#
#         """pygame.draw.rect(janela, (255, 0, 0), player_rect, 4)
#         pygame.draw.rect(janela, (255, 0, 0), inimigo_rect, 4)
#         pygame.draw.rect(janela, (255, 0, 0), tiro_rect, 4)"""
#
#         if tiro_alvo:
#             pos_y_missil -= speed_x_missil
#
#         # Colisão do tiro com nave Inimiga.
#
#         janela.blit(shot, (pos_x_missil, pos_y_missil))
#         janela.blit(enemy_ship, (pos_x_enemy, pos_y_enemy))
#         janela.blit(player_ship, (pos_x_player, pos_y_player))
#
#         # window.blit(background_image, (0, 0))
#         # window.blit(player_ship, (pos_x_player, pos_y_player))
#         # window.blit(enemy_ship, (440, 50))
#         # Transforma a imagem, em um objeto interativo.
#
#     pygame.display.update()
#
# print('-=' * 20)
# resultado()
# print('-=' * 20)

# pygame.init()
# mixer.init()
#
#
# def colisoes():
#     global pontuacao
#     global pos_y_enemy
#     global pos_x_enemy
#     global som_nave_colisao
#     global som_missil
#     global som_explosao
#
#     # Se o player principal colidir com a nave inimiga
#     if player_rect.colliderect(inimigo_rect) or inimigo_rect.y > 500:
#         pontuacao -= 1
#         print(pontuacao)
#         return True
#     elif tiro_rect.colliderect(inimigo_rect):
#         pontuacao += 1
#         pos_y_enemy -= 1200
#         if pos_y_enemy < -1000:
#             random_y = randint(1, 440)
#             random_x = randint(1, 870)
#             pos_y_enemy -= 450
#             pos_y_enemy = random_y
#             pos_x_enemy = random_x
#         print(pontuacao)
#         som_explosao.play()
#         return True
#     else:
#         return False
#
#
# # Carregamento e inserção dos sons do jogo
# # som_missil = mixer.music.load('nome do laser')
# # som_explosao = pygame.mixer.Sound('nome do som da explosao')
#
#
#
# x, y = (960, 540)
# window = pygame.display.set_mode([x, y])
# pygame.display.set_caption('Retorno dos Aliens')
# pygame.display.set_caption('Second Game')
#
# tiro_alvo = False
#
# pos_y_enemy += 10
#
# if pos_y_enemy > 530:
#     random_y = randint(1, 440)
#     random_x = randint(1, 870)
#     pos_y_enemy -= 450
#     pos_y_enemy = random_y
#     pos_x_enemy = random_x
#
# keys = pygame.key.get_pressed()
#
# # Movimentação do player principal do jogo
#
# # Se pressionar a seta para cima, a nave se moverá para cima
# if keys[pygame.K_UP]:
#     pos_y_player -= speed_ship_player
# # Se pressionar a seta para baixo, a nave se moverá para baixo
# if keys[pygame.K_DOWN]:
#     pos_y_player += speed_ship_player
# # Se pressionar a seta para a esquerda, a nave se moverá para a esquerda
# if keys[pygame.K_LEFT]:
#     pos_x_player -= speed_ship_player
# # Se pressionar a seta para a direita, a nave se moverá para a direita
# if keys[pygame.K_RIGHT]:
#     pos_x_player += speed_ship_player
#
# # Posição do player principal do jogo
# if pos_y_player <= -10:
#     pos_y_player = -10
# if pos_y_player >= 440:
#     pos_y_player = 440
# if pos_x_player <= 0:
#     pos_x_player = 0
# if pos_x_player >= 870:
#     pos_x_player = 870
#
# window.blit(background_image, (0, 0))
# window.blit(player_ship, (pos_x_player, pos_y_player))
# window.blit(enemy_ship, (440, 50))
#
# pygame.display.update()
#
# print('-=' * 20)
# resultado()
# print('-=' * 20)
