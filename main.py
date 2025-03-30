import pygame
from random import randint

# Inicializa o pygame e o mixer
pygame.init()
pygame.mixer.init()

# Carrega os sons
som_explosao = pygame.mixer.Sound('D:/Jogos/AtividadePratica/asset/explosao.wav')
som_tiro = pygame.mixer.Sound('D:/Jogos/AtividadePratica/asset/tiro.wav')
pygame.mixer.music.load('D:/Jogos/AtividadePratica/asset/musica_fundo.mp3')
pygame.mixer.music.play(-1, 0.0)  # Reproduz a música em loop

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


# Função para o menu inicial
def menu_inicial():
    selecionado = 0  # 0: START, 1: EXIT
    while True:
        janela.fill((0, 0, 0))
        # Desenha o fundo
        janela.blit(background_image, (0, 0))

        # Exibe as opções
        texto_start = fonte.render('START', True, (255, 255, 255) if selecionado == 0 else (150, 150, 150))
        texto_exit = fonte.render('EXIT', True, (255, 255, 255) if selecionado == 1 else (150, 150, 150))

        janela.blit(texto_start, (x // 2 - texto_start.get_width() // 2, y // 2 - 50))
        janela.blit(texto_exit, (x // 2 - texto_exit.get_width() // 2, y // 2 + 20))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Navegação com as teclas de seta
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selecionado = 0
                elif event.key == pygame.K_DOWN:
                    selecionado = 1
                elif event.key == pygame.K_RETURN:  # Tecla Enter
                    if selecionado == 0:
                        return "START"
                    elif selecionado == 1:
                        pygame.quit()
                        exit()


# Função de colisão
def colisoes(player_rect, inimigo_rect, tiro_rect, tiro_alvo, pos_x_player, pos_y_player, vida, pontuacao, proxima_fase, pos_x_enemy, pos_y_enemy):
    global colisao_ocorrida

    # Colisão do player com o inimigo
    if player_rect.colliderect(inimigo_rect) and not colisao_ocorrida:
        vida -= 20  # Reduz 20 pontos de vida ao colidir com o inimigo
        colisao_ocorrida = True
    elif not player_rect.colliderect(inimigo_rect):
        colisao_ocorrida = False

    # Colisão do tiro com o inimigo
    if tiro_alvo and tiro_rect.colliderect(inimigo_rect):
        pontuacao += 1
        proxima_fase -= 1
        # Reposiciona o inimigo após ser destruído
        pos_y_enemy = -50  # Coloca o inimigo acima da tela
        pos_x_enemy = randint(50, 870)  # Novo valor aleatório para a posição X do inimigo
        tiro_alvo = False
        som_explosao.play()  # Toca o som da explosão quando o inimigo é destruído

    return tiro_alvo, vida, pontuacao, proxima_fase, pos_x_enemy, pos_y_enemy


# Loop principal do jogo
def jogo():
    # Posições iniciais
    pos_x_player, pos_y_player = 425, 440
    pos_x_enemy, pos_y_enemy = 50, 0
    pos_x_missil, pos_y_missil = pos_x_player, pos_y_player

    # Velocidades
    speed_ship_player = 10
    speed_ship_enemy = 5
    speed_x_missil = 10
    tiro_alvo = False

    # Variáveis do jogo
    pontuacao = 0
    vida = 100
    proxima_fase = 30
    colisao_ocorrida = False
    loop = True

    # Variáveis para animação do background
    background_y = 0
    star_list = [[randint(0, x), randint(0, y)] for _ in range(50)]

    # Loop principal do jogo
    while loop:
        pygame.time.delay(30)

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                loop = False

        # Movimentação do fundo para efeito de animação
        background_y += 2
        if background_y >= y:
            background_y = 0

        # Movimentação das estrelas
        for star in star_list:
            star[1] += 2
            if star[1] > y:
                star[0] = randint(0, x)
                star[1] = 0

        # Movimentação do inimigo
        pos_y_enemy += speed_ship_enemy
        if pos_y_enemy > 530:
            pontuacao -= 5  # Reduz pontuação se o inimigo sair da tela sem ser destruído
            proxima_fase += 1
            pos_y_enemy = -50
            pos_x_enemy = randint(50, 870)

        # Captura comandos do teclado
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_UP] and pos_y_player > 0:
            pos_y_player -= speed_ship_player
        if comandos[pygame.K_DOWN] and pos_y_player < 440:  # Ajustado para que a nave não ultrapasse a parte inferior da tela
            pos_y_player += speed_ship_player
        if comandos[pygame.K_LEFT] and pos_x_player > 0:
            pos_x_player -= speed_ship_player
        if comandos[pygame.K_RIGHT] and pos_x_player < 870:
            pos_x_player += speed_ship_player
        if comandos[pygame.K_SPACE] and not tiro_alvo:
            tiro_alvo = True
            pos_x_missil = pos_x_player + 15
            pos_y_missil = pos_y_player
            som_tiro.play()  # Toca o som do tiro sempre que o jogador dispara

        # Movimento do míssil
        if tiro_alvo:
            pos_y_missil -= speed_x_missil
            if pos_y_missil < 0:
                tiro_alvo = False

        # Atualiza os retângulos de colisão
        player_rect = player_ship.get_rect(topleft=(pos_x_player, pos_y_player))
        inimigo_rect = enemy_ship.get_rect(topleft=(pos_x_enemy, pos_y_enemy))
        tiro_rect = shot.get_rect(topleft=(pos_x_missil, pos_y_missil))

        tiro_alvo, vida, pontuacao, proxima_fase, pos_x_enemy, pos_y_enemy = colisoes(player_rect, inimigo_rect, tiro_rect, tiro_alvo, pos_x_player, pos_y_player, vida, pontuacao, proxima_fase, pos_x_enemy, pos_y_enemy)

        # Renderiza o fundo e estrelas
        janela.blit(background_image, (0, background_y))
        janela.blit(background_image, (0, background_y - y))
        for star in star_list:
            pygame.draw.circle(janela, (255, 255, 255), star, 2)

        # Renderiza as imagens
        janela.blit(player_ship, (pos_x_player, pos_y_player))
        janela.blit(enemy_ship, (pos_x_enemy, pos_y_enemy))
        if tiro_alvo:
            janela.blit(shot, (pos_x_missil, pos_y_missil))

        # Exibe a pontuação, vida e próxima fase na tela
        texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, (255, 255, 255))
        texto_vida = fonte.render(f'Vida: {vida}', True, (255, 0, 0))
        texto_fase = fonte.render(f'Próxima fase: {proxima_fase}', True, (0, 255, 0))
        janela.blit(texto_pontuacao, (20, 20))
        janela.blit(texto_vida, (20, 50))
        janela.blit(texto_fase, (20, 80))

        pygame.display.update()

        # Verifica se a vida chegou a 0 e encerra o jogo com a mensagem "Game Over"
        if vida <= 0:
            janela.fill((0, 0, 0))
            mensagem = fonte.render('VOCÊ PERDEU! GAME OVER!', True, (255, 0, 0))
            janela.blit(mensagem, (x // 2 - 200, y // 2))
            pygame.display.update()
            pygame.time.delay(3000)  # Exibe a mensagem por 3 segundos
            loop = False

        # Verifica se a próxima fase chegou a 0 e encerra o jogo com mensagem de transição
        if proxima_fase <= 0:
            janela.fill((0, 0, 0))
            mensagem = fonte.render('VOCÊ PASSOU PARA A SEGUNDA FASE!', True, (0, 255, 0))
            janela.blit(mensagem, (x // 2 - 200, y // 2))
            pygame.display.update()
            pygame.time.delay(3000)
            loop = False


# Inicia o menu e o jogo
opcao = menu_inicial()

if opcao == "START":
    jogo()

pygame.quit()