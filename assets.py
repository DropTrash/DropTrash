import pygame
import settings  # Importa as configurações


# --- Variáveis Globais para Assets Carregados ---
# Imagens de Fundo e Cenas
backGround = None
mikeScene01, mikeScene02, mikeScene03, mikeScene04, mikeScene05 = (
    None,
    None,
    None,
    None,
    None,
)
backGroundGaming = None

# Imagens de Objetos do Jogo
papperGarbage_bin_img = None
metalGarbage_bin_img = None
lifes_img = None
player_img = None
paper_trash_item_img = None
metal_trash_item_img = None

# Fontes
font_large = None
font_medium = None


def load_all_assets():
    global backGround, mikeScene01, mikeScene02, mikeScene03, mikeScene04, mikeScene05
    global backGroundGaming, papperGarbage_bin_img, metalGarbage_bin_img
    global lifes_img, player_img, paper_trash_item_img, metal_trash_item_img
    global font_large, font_medium

    backGround = pygame.image.load(
        settings.ASSET_HOME_SCENE
    ).convert()  # .convert() pode otimizar
    mikeScene01 = pygame.image.load(settings.ASSET_MIKE_SCENE_01).convert()
    mikeScene02 = pygame.image.load(settings.ASSET_MIKE_SCENE_02).convert()
    mikeScene03 = pygame.image.load(settings.ASSET_MIKE_SCENE_03).convert()
    mikeScene04 = pygame.image.load(settings.ASSET_MIKE_SCENE_04).convert()
    mikeScene05 = pygame.image.load(settings.ASSET_MIKE_SCENE_05).convert()
    backGroundGaming = pygame.image.load(settings.ASSET_GAMING_SCENE).convert()

    papperGarbage_bin_img = pygame.image.load(settings.ASSET_PAPER_BIN).convert_alpha()
    metalGarbage_bin_img = pygame.image.load(settings.ASSET_METAL_BIN).convert_alpha()
    lifes_img = pygame.image.load(settings.ASSET_LIFES).convert_alpha()
    player_img_original = pygame.image.load(settings.ASSET_PLAYER).convert_alpha()
    player_img = pygame.transform.scale(player_img_original, (350, 200))

    paper_trash_item_img_original = pygame.image.load(
        settings.ASSET_PAPER_WASTE
    ).convert_alpha()
    metal_trash_item_img_original = pygame.image.load(
        settings.ASSET_SODA_CAN
    ).convert_alpha()

    paper_trash_item_img = pygame.transform.scale(
        paper_trash_item_img_original, (settings.TRASH_WIDTH, settings.TRASH_HEIGHT)
    )
    metal_trash_item_img = pygame.transform.scale(
        metal_trash_item_img_original, (settings.TRASH_WIDTH, settings.TRASH_HEIGHT)
    )

    try:
        font_large = pygame.font.SysFont(
            settings.FONT_DEFAULT_SYS, settings.FONT_SIZE_LARGE
        )
        font_medium = pygame.font.SysFont(
            settings.FONT_DEFAULT_SYS, settings.FONT_SIZE_MEDIUM
        )
    except pygame.error:
        print("Aviso: Fonte do sistema não encontrada, usando fonte padrão do Pygame.")
        font_large = pygame.font.Font(None, settings.FONT_SIZE_LARGE)
        font_medium = pygame.font.Font(None, settings.FONT_SIZE_MEDIUM)

    print("Assets carregados com sucesso!")
