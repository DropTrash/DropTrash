import pygame
pygame.init()

# Comandos de propriedades da janela
window = pygame.display.set_mode([1472, 832])
pygame.display.set_caption("Drop Trash")
backGround = pygame.image.load('assets/HomeScreen.jpg')
pygame.mixer.music.load('music/hino_SPFC.mp3')
pygame.mixer.music.play(-1, 0.0)  


loop = True
scenes = "home"

# Loop principal do jogo
while loop:

    # Comando para carregar a cena de jogabilidade
    if scenes == "playing":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            window.fill((0, 255, 0))
    
    # Comando para carregar a cena de home
    elif scenes == "home":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                loop = False
            else:
                window.blit(backGround,(0, 0))

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        scenes = "playing"
                    else:
                        scenes = "home"

    pygame.display.update()
