import pygame

# Dimensões da Janela
WINDOW_WIDTH = 1472
WINDOW_HEIGHT = 832
GAME_CAPTION = "Drop Trash"

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_GREY = (30, 30, 30)
LIGHT_GREY = (200, 200, 200)

# Configurações do Jogo
MAX_LIFES = 3
MIN_DISTANCE_BETWEEN_TRASH = 70
LEVEL_TIME_SECONDS_LVL1 = 30
LEVEL_TIME_SECONDS_LVL2 = 90

# Tamanhos Padrão para Lixos
TRASH_WIDTH = 70
TRASH_HEIGHT = 70

# --- TAMANHOS ESPECÍFICOS PARA LIXEIRAS DO NÍVEL 2 (AJUSTE MANUAL) ---
BIN_ORGANIC_WIDTH = 180
BIN_ORGANIC_HEIGHT = 220
BIN_GLASS_WIDTH = 180
BIN_GLASS_HEIGHT = 220
BIN_PLASTIC_WIDTH = 180
BIN_PLASTIC_HEIGHT = 220

# --- COORDENADAS E DIMENSÕES PARA BOTÕES NA TELA DE GAME OVER ---
GAMEOVER_RETRY_BUTTON_RECT = pygame.Rect(
    500, 580, 220, 90
)  # Exemplo: (x, y, largura, altura)
GAMEOVER_QUIT_BUTTON_RECT = pygame.Rect(780, 580, 200, 90)  # Exemplo

# --- CONFIGURAÇÃO DE QUANTIDADE DE LIXOS POR NÍVEL ---
NUM_TOTAL_PAPER_TRASH_LVL1 = 4
NUM_TOTAL_METAL_TRASH_LVL1 = 4
NUM_TOTAL_ORGANIC_TRASH_LVL2 = 4
NUM_TOTAL_GLASS_TRASH_LVL2 = 4
NUM_TOTAL_PLASTIC_TRASH_LVL2 = 3

# Caminhos para Assets
MUSIC_NATURE = "music/natureSound.mp3"
MUSIC_MIKE = "music/mikeSound.mp3"

ASSET_HOME_SCENE = "assets/HomeScene.png"
ASSET_MIKE_SCENE_01 = "assets/MikeScene01.png"
ASSET_MIKE_SCENE_02 = "assets/MikeScene02.png"
ASSET_MIKE_SCENE_03 = "assets/MikeScene03.png"
ASSET_MIKE_SCENE_04 = "assets/MikeScene04.png"
ASSET_MIKE_SCENE_05 = "assets/MikeScene05.png"
ASSET_GAMING_SCENE = "assets/GamingScene.png"
ASSET_PAPER_BIN = "assets/Level01/PapperGarbage.png"
ASSET_METAL_BIN = "assets/Level01/MetalGarbage.png"
ASSET_LIFES = "assets/Lifes.png"
ASSET_PLAYER = "assets/Player.png"
ASSET_GAME_OVER_BG = "assets/GameOverScreen.png"
ASSET_VICTORY_SCREEN_BG = "assets/Fim.png"

# Fontes
FONT_DEFAULT_SYS = "Arial"
FONT_SIZE_LARGE = 72
FONT_SIZE_MEDIUM = 48
FONT_PIXEL_PATH = "assets/Fonts/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
FONT_PIXEL_SIZE = 40

# --- CAMINHOS PARA ASSETS DE LIXO (COM VARIEDADE) ---
# Nível 1
ASSET_PAPER_AMASSADO = "assets/Level01/PaperWaste.png"
ASSET_PAPER_CAIXA = "assets/Level01/CaixaPapelao.png"
ASSET_METAL_LATA = "assets/Level01/SodaCan.png"
ASSET_METAL_SPRAY = "assets/Level01/SprayCan.png"

# Nível 2
ASSET_ORGANIC_BANANA = "assets/Level02/Banana.png"
ASSET_ORGANIC_BROCOLIS = "assets/Level02/Brocolis.png"
ASSET_GLASS_GELEIA = "assets/Level02/GeleiaPixel.png"
ASSET_GLASS_VINHO = "assets/Level02/Vinho.png"
ASSET_PLASTIC_PET = "assets/Level02/PlasticoPixel.png"

# Cutscenes Nível 2 e Game Over
ASSET_MIKE_LVL2_INTRO = "assets/Level02/Nivel2Mike.png"
ASSET_MIKE_LVL1_EXPLAIN_GAMEOVER = (
    "assets/Level01/ExplanationLevel1.png"  # Explicação Game Over Nível 1
)
ASSET_MIKE_LVL2_EXPLAIN_GAMEOVER = (
    "assets/Level02/SceneAwareness.png"  # Explicação Game Over Nível 2
)

# Lixeiras Nível 2
ASSET_ORGANIC_BIN = "assets/Level02/OrganicGarbage.png"
ASSET_GLASS_BIN = "assets/Level02/GlassGarbage.png"
ASSET_PLASTIC_BIN = "assets/Level02/PlasticGarbage.png"
