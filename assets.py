import pygame
import settings

backGround = None
mikeScene01, mikeScene02, mikeScene03, mikeScene04, mikeScene05 = (
    None,
    None,
    None,
    None,
    None,
)
backGroundGaming = None
gameOver_bg_img = None
papperGarbage_bin_img = None
metalGarbage_bin_img = None
paper_trash_item_img = None
metal_trash_item_img = None
lifes_img = None
player_img = None
font_large = None
font_medium = None
mike_lvl2_intro_img = None
mike_lvl2_explain_img = None
organic_bin_img = None
glass_bin_img = None
plastic_bin_img = None
organic_waste_item_img = None
glass_waste_item_img = None
plastic_waste_item_img = None


def load_all_assets():
    global backGround, mikeScene01, mikeScene02, mikeScene03, mikeScene04, mikeScene05
    global backGroundGaming, papperGarbage_bin_img, metalGarbage_bin_img
    global lifes_img, player_img, paper_trash_item_img, metal_trash_item_img
    global font_large, font_medium, gameOver_bg_img
    global mike_lvl2_intro_img, mike_lvl2_explain_img
    global organic_bin_img, glass_bin_img, plastic_bin_img
    global organic_waste_item_img, glass_waste_item_img, plastic_waste_item_img

    try:
        backGround = pygame.image.load(settings.ASSET_HOME_SCENE).convert()
        mikeScene01 = pygame.image.load(settings.ASSET_MIKE_SCENE_01).convert()
        mikeScene02 = pygame.image.load(settings.ASSET_MIKE_SCENE_02).convert()
        mikeScene03 = pygame.image.load(settings.ASSET_MIKE_SCENE_03).convert()
        mikeScene04 = pygame.image.load(settings.ASSET_MIKE_SCENE_04).convert()
        mikeScene05 = pygame.image.load(settings.ASSET_MIKE_SCENE_05).convert()
        backGroundGaming = pygame.image.load(settings.ASSET_GAMING_SCENE).convert()
    except pygame.error as e:
        print(f"Erro ao carregar imagens de cena: {e}")

    try:
        papperGarbage_bin_img = pygame.image.load(
            settings.ASSET_PAPER_BIN
        ).convert_alpha()
    except pygame.error as e:
        print(f"Erro ao carregar lixeira de papel: {e}")
    try:
        metalGarbage_bin_img = pygame.image.load(
            settings.ASSET_METAL_BIN
        ).convert_alpha()
    except pygame.error as e:
        print(f"Erro ao carregar lixeira de metal: {e}")
    try:
        lifes_img = pygame.image.load(settings.ASSET_LIFES).convert_alpha()
    except pygame.error as e:
        print(f"Erro ao carregar imagem de vidas: {e}")
    try:
        player_img_original = pygame.image.load(settings.ASSET_PLAYER).convert_alpha()
        player_img = pygame.transform.scale(player_img_original, (100, 60))
    except pygame.error as e:
        print(f"Erro ao carregar imagem do jogador: {e}")

    try:
        paper_trash_item_img_original = pygame.image.load(
            settings.ASSET_PAPER_WASTE
        ).convert_alpha()
        paper_trash_item_img = pygame.transform.scale(
            paper_trash_item_img_original, (settings.TRASH_WIDTH, settings.TRASH_HEIGHT)
        )
    except pygame.error as e:
        print(f"Erro ao carregar lixo de papel: {e}")
    try:
        metal_trash_item_img_original = pygame.image.load(
            settings.ASSET_SODA_CAN
        ).convert_alpha()
        metal_trash_item_img = pygame.transform.scale(
            metal_trash_item_img_original, (settings.TRASH_WIDTH, settings.TRASH_HEIGHT)
        )
    except pygame.error as e:
        print(f"Erro ao carregar lixo de metal: {e}")

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

    try:
        gameOver_bg_img = pygame.image.load(settings.ASSET_GAME_OVER_BG).convert()
    except pygame.error as e:
        print(
            f"Erro ao carregar imagem de Game Over: {settings.ASSET_GAME_OVER_BG} - {e}"
        )
        gameOver_bg_img = None

    try:
        mike_lvl2_intro_img = pygame.image.load(
            settings.ASSET_MIKE_LVL2_INTRO
        ).convert()
    except pygame.error as e:
        print(f"Erro ao carregar {settings.ASSET_MIKE_LVL2_INTRO}: {e}")
    try:
        mike_lvl2_explain_img = pygame.image.load(
            settings.ASSET_MIKE_LVL2_EXPLAIN
        ).convert()
    except pygame.error as e:
        print(f"Erro ao carregar {settings.ASSET_MIKE_LVL2_EXPLAIN}: {e}")

    try:
        organic_bin_original = pygame.image.load(
            settings.ASSET_ORGANIC_BIN
        ).convert_alpha()
        organic_bin_img = pygame.transform.scale(
            organic_bin_original,
            (settings.BIN_ORGANIC_WIDTH, settings.BIN_ORGANIC_HEIGHT),
        )
    except pygame.error as e:
        print(f"Erro ao carregar/redimensionar lixeira orgânica: {e}")
    try:
        glass_bin_original = pygame.image.load(settings.ASSET_GLASS_BIN).convert_alpha()
        glass_bin_img = pygame.transform.scale(
            glass_bin_original, (settings.BIN_GLASS_WIDTH, settings.BIN_GLASS_HEIGHT)
        )
    except pygame.error as e:
        print(f"Erro ao carregar/redimensionar lixeira de vidro: {e}")
    try:
        plastic_bin_original = pygame.image.load(
            settings.ASSET_PLASTIC_BIN
        ).convert_alpha()
        plastic_bin_img = pygame.transform.scale(
            plastic_bin_original,
            (settings.BIN_PLASTIC_WIDTH, settings.BIN_PLASTIC_HEIGHT),
        )
    except pygame.error as e:
        print(f"Erro ao carregar/redimensionar lixeira de plástico: {e}")

    try:
        organic_waste_original = pygame.image.load(
            settings.ASSET_ORGANIC_WASTE
        ).convert_alpha()
        organic_waste_item_img = pygame.transform.scale(
            organic_waste_original,
            (settings.TRASH_WIDTH_ORGANIC, settings.TRASH_HEIGHT_ORGANIC),
        )
    except pygame.error as e:
        print(f"Erro ao carregar lixo orgânico Nível 2: {e}")
    try:
        glass_waste_original = pygame.image.load(
            settings.ASSET_GLASS_WASTE
        ).convert_alpha()
        glass_waste_item_img = pygame.transform.scale(
            glass_waste_original,
            (settings.TRASH_WIDTH_GLASS, settings.TRASH_HEIGHT_GLASS),
        )
    except pygame.error as e:
        print(f"Erro ao carregar lixo de vidro Nível 2: {e}")
    try:
        plastic_waste_original = pygame.image.load(
            settings.ASSET_PLASTIC_WASTE
        ).convert_alpha()
        plastic_waste_item_img = pygame.transform.scale(
            plastic_waste_original,
            (settings.TRASH_WIDTH_PLASTIC, settings.TRASH_HEIGHT_PLASTIC),
        )
    except pygame.error as e:
        print(f"Erro ao carregar lixo de plástico Nível 2: {e}")

    print("Assets carregados com sucesso!")
