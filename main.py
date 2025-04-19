import pygame
pygame.init()

# Comandos de propriedades da janela
window = pygame.display.set_mode([1472, 832])
pygame.display.set_caption("Drop Trash")

# Funções do jogo
# Função da música da cena de home
def musicHome():
    pygame.mixer.music.load('music/natureSound.mp3')
    pygame.mixer.music.play(-1) 
    pygame.mixer.music.set_volume(0.5)

# Função da música das cenas de falas do Mike (Lixeiro do jogo)
def musicMike():
    pygame.mixer.music.load('music/mikeSound.mp3')
    pygame.mixer.music.play() 
    pygame.mixer.music.set_volume(0.5)

# Função de imagens do jogo
def images():
    global backGround
    global imgScene01
    global imgScene02
    global imgScene03
    global imgScene04
    global imgScene05
    backGround = pygame.image.load('assets/HomeScreen.png')
    imgScene01 = pygame.image.load('assets/Scene01.png')
    imgScene02 = pygame.image.load('assets/Scene02.png')
    imgScene03 = pygame.image.load('assets/Scene03.png')
    imgScene04 = pygame.image.load('assets/Scene04.png')
    imgScene05 = pygame.image.load('assets/Scene05.png')

# Função de transição de imagens (fade)
def fade_transition(surface, currentImg, nextImg, speed=10):
    fade = pygame.Surface((1472, 832))
    fade.fill((0, 0, 0))

    # Fade-out da imagem atual
    for alpha in range(0, 255, speed):
        surface.blit(currentImg, (0, 0))
        fade.set_alpha(alpha)
        surface.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

    # Fade-in da próxima imagem
    for alpha in range(255, 0, -speed):
        surface.blit(nextImg, (0, 0))
        fade.set_alpha(alpha)
        surface.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

# Função para a cena de home
def sceneHome():
    global loop
    global scenes
    global controlMikeScenes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        else:
            window.blit(backGround, (0, 0))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    fade_transition(window, backGround, imgScene01)
                    pygame.mixer.music.stop() 
                    musicMike()                
                    scenes = "Maike"
                    controlMikeScenes = 1

# Função para as cenas de fala do Mike (Lixeiro do jogo)
def scenesMike():
    global loop
    global scenes
    global controlMikeScenes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if controlMikeScenes == 1:
                    fade_transition(window, imgScene01, imgScene02)
                    controlMikeScenes = 2
                    musicMike()  
                elif controlMikeScenes == 2:
                    fade_transition(window, imgScene02, imgScene03)
                    controlMikeScenes = 3
                    musicMike()
                elif controlMikeScenes == 3:
                    fade_transition(window, imgScene03, imgScene04)
                    controlMikeScenes = 4
                    musicMike()
                elif controlMikeScenes == 4:
                    fade_transition(window, imgScene04, imgScene05)
                    controlMikeScenes = 5
                    musicMike()
                elif controlMikeScenes == 5:
                    controlMikeScenes = 5

    # Controle das cenas do Mike (Lixeiro do jogo)
    if controlMikeScenes == 1:
        window.blit(imgScene01, (0, 0))
    elif controlMikeScenes == 2:
        window.blit(imgScene02, (0, 0))
    elif controlMikeScenes == 3:
        window.blit(imgScene03, (0, 0))
    elif controlMikeScenes == 4:
        window.blit(imgScene04, (0, 0))
    elif controlMikeScenes == 5:
        window.blit(imgScene05, (0, 0))

musicHome()  
images()
loop = True
scenes = "home"
controlMikeScenes = 1

# Loop principal do jogo
while loop:

    # Comando para chamar a função de cena home do jogo
    if scenes == "home":
        sceneHome()
        
    # Comando para chamar a função de cenas do Mike (Lixeiro do jogo)
    elif scenes == "Maike":
        scenesMike()

    pygame.display.update()
