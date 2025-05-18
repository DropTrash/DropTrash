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

# Tamanhos Padrão para Lixos (Nível 1 e como fallback)
TRASH_WIDTH = 70
TRASH_HEIGHT = 70

# --- TAMANHOS ESPECÍFICOS PARA LIXOS DO NÍVEL 2 (AJUSTE MANUAL) ---
TRASH_WIDTH_ORGANIC = 70
TRASH_HEIGHT_ORGANIC = 70
TRASH_WIDTH_GLASS = 70
TRASH_HEIGHT_GLASS = 70
TRASH_WIDTH_PLASTIC = 70
TRASH_HEIGHT_PLASTIC = 70

# --- TAMANHOS ESPECÍFICOS PARA LIXEIRAS DO NÍVEL 2 (AJUSTE MANUAL) ---
BIN_ORGANIC_WIDTH = 180
BIN_ORGANIC_HEIGHT = 220
BIN_GLASS_WIDTH = 180
BIN_GLASS_HEIGHT = 220
BIN_PLASTIC_WIDTH = 180
BIN_PLASTIC_HEIGHT = 220


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
ASSET_PAPER_WASTE = "assets/Level01/PaperWaste.png"
ASSET_SODA_CAN = "assets/Level01/SodaCan.png"
ASSET_GAME_OVER_BG = "assets/GameOverScreen.png"

# Fontes
FONT_DEFAULT_SYS = "Arial"  # Pygame tentará usar esta fonte do sistema
FONT_SIZE_LARGE = 72
FONT_SIZE_MEDIUM = 48

# --- CAMINHOS PARA NOVOS ASSETS DO NÍVEL 2 ---
ASSET_MIKE_LVL2_INTRO = "assets/Level02/Nivel2Mike.png"
ASSET_MIKE_LVL2_EXPLAIN = "assets/Level02/SceneAwareness.png"
ASSET_ORGANIC_BIN = "assets/Level02/OrganicGarbage.png"
ASSET_GLASS_BIN = "assets/Level02/GlassGarbage.png"
ASSET_PLASTIC_BIN = "assets/Level02/PlasticGarbage.png"
ASSET_ORGANIC_WASTE = "assets/Level02/Banana.png"
ASSET_GLASS_WASTE = "assets/Level02/GeleiaPixel.png"
ASSET_PLASTIC_WASTE = "assets/Level02/PlasticoPixel.png"
