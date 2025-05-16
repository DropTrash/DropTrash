import pygame
pygame.init()

# Comandos das propriedades da janela
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

# Função das imagens do jogo
def images():
    global backGround
    global mikeScene01
    global mikeScene02
    global mikeScene03
    global mikeScene04
    global mikeScene05
    global backGroundGaming
    global papperGarbage
    global metalGarbage
    global lifes
    global player

    backGround = pygame.image.load('assets/HomeScene.png')
    mikeScene01 = pygame.image.load('assets/MikeScene01.png')
    mikeScene02 = pygame.image.load('assets/MikeScene02.png')
    mikeScene03 = pygame.image.load('assets/MikeScene03.png')
    mikeScene04 = pygame.image.load('assets/MikeScene04.png')
    mikeScene05 = pygame.image.load('assets/MikeScene05.png')
    backGroundGaming = pygame.image.load('assets/GamingScene.png')
    papperGarbage = pygame.image.load('assets/Level01/PapperGarbage.png')
    metalGarbage = pygame.image.load('assets/Level01/MetalGarbage.png')
    lifes = pygame.image.load('assets/lifes.png')

    player = pygame.image.load('assets/Player.png')
    player = pygame.transform.scale(player, (350, 200))

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
def homeScene():
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
                    fade_transition(window, backGround, mikeScene01)
                    pygame.mixer.music.stop() 
                    musicMike()                
                    scenes = "maike"
                    controlMikeScenes = 1

# Função para as cenas de fala do Mike (Lixeiro do jogo)
def mikeScenes():
    global loop
    global scenes
    global controlMikeScenes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if controlMikeScenes == 1:
                    fade_transition(window, mikeScene01, mikeScene02)
                    controlMikeScenes = 2
                    musicMike()  
                elif controlMikeScenes == 2:
                    fade_transition(window, mikeScene02, mikeScene03)
                    controlMikeScenes = 3
                    musicMike()
                elif controlMikeScenes == 3:
                    fade_transition(window, mikeScene03, mikeScene04)
                    controlMikeScenes = 4
                    musicMike()
                elif controlMikeScenes == 4:
                    fade_transition(window, mikeScene04, mikeScene05)
                    controlMikeScenes = 5
                    musicMike()
                elif controlMikeScenes == 5:
                    fade_transition(window, mikeScene05, backGroundGaming)
                    garbages()
                    musicHome()
                    controlMikeScenes = 5
                    scenes = "gaming"
                    return
                    
    # Controle das cenas do Mike (Lixeiro do jogo)
    if controlMikeScenes == 1:
        window.blit(mikeScene01, (0, 0))
    elif controlMikeScenes == 2:
        window.blit(mikeScene02, (0, 0))
    elif controlMikeScenes == 3:
        window.blit(mikeScene03, (0, 0))
    elif controlMikeScenes == 4:
        window.blit(mikeScene04, (0, 0))
    elif controlMikeScenes == 5:
        window.blit(mikeScene05, (0, 0))

# Função da cena de plano de fundo do jogo
def gammingScene():
    global loop
    global scenes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    window.blit(backGroundGaming, (0, 0))

def garbages():
    global loop
    global scenes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    window.blit(papperGarbage, (450, 10))
    window.blit(metalGarbage, (800, 10))

def playerLife():
    global loop
    global scenes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    window.blit(player, (0, 0))
    #window.blit(lifes, (50, 10))
    #window.blit(lifes, (90, 10))
    #window.blit(lifes, (150, 10))

# Inicialização do jogo
musicHome()  
images()
loop = True
scenes = "home"
controlMikeScenes = 1

# Loop principal do jogo
while loop:

    # Comando para chamar a função de cena home do jogo
    if scenes == "home":
        homeScene()
        
    # Comando para chamar a função de cenas do Mike (Lixeiro do jogo)
    elif scenes == "maike":
        mikeScenes()
    
    # Comando para chamar a função de cena do plano de fundo do jogo das lixeiras
    elif scenes == "gaming":
        gammingScene()
        garbages()
        playerLife()
        # pos = pygame.mouse.get_pos()
        # print(pos) 

    pygame.display.update()
