import pygame
pygame.init()

# Comandos de propriedades da janela
window = pygame.display.set_mode([1472, 832])
pygame.display.set_caption("Drop Trash")

# Funções do jogo
def music():
    pygame.mixer.music.load('music/hino_SPFC.mp3')
    pygame.mixer.music.play(-1, 0.0)

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

def sceneHome():
    global loop
    global scenes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        else:
            window.blit(backGround, (0, 0))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    scenes = "Maike"
                else:
                    scenes = "home"

def scenesMike():
    global loop
    global scenes
    global controlMikeScenes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                controlMikeScenes += 1  

                if controlMikeScenes > 5:
                    controlMikeScenes = 5  

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

music()
images()
loop = True
scenes = "home"
controlMikeScenes = 1

# Loop principal do jogo
while loop:

    # Comando para carregar a cena de home
    if scenes == "home":
        sceneHome()

    # Comando para carregar as cenas de fala do Maike (Lixeiro do jogo)
    elif scenes == "Maike":
        scenesMike()

    pygame.display.update()
