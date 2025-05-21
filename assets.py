import pygame
import settings

# --- Variáveis Globais para Assets Carregados ---
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
victory_screen_bg_img = None

# Lixeiras
papperGarbage_bin_img = None
metalGarbage_bin_img = None
organic_bin_img = None
glass_bin_img = None
plastic_bin_img = None

# Listas para armazenar as variações de imagens de lixo carregadas e redimensionadas
paper_trash_images = []
metal_trash_images = []
organic_trash_images = []
glass_trash_images = []
plastic_trash_images = []

# Assets Comuns
lifes_img = None
player_img = None

# Fontes
font_large = None
font_medium = None
font_pixel = None

# Cutscenes
mike_lvl2_intro_img = None
mike_lvl1_explain_gameover_img = None  # Para Game Over Nível 1
mike_lvl2_explain_gameover_img = (
    None  # Para Game Over Nível 2 (renomeado de mike_lvl2_explain_img)
)


def load_all_assets():
    global backGround, mikeScene01, mikeScene02, mikeScene03, mikeScene04, mikeScene05
    global backGroundGaming, papperGarbage_bin_img, metalGarbage_bin_img
    global lifes_img, player_img, font_large, font_medium, gameOver_bg_img, font_pixel
    global mike_lvl2_intro_img, mike_lvl1_explain_gameover_img, mike_lvl2_explain_gameover_img
    global organic_bin_img, glass_bin_img, plastic_bin_img
    global paper_trash_images, metal_trash_images, organic_trash_images, glass_trash_images, plastic_trash_images
    global victory_screen_bg_img

    paper_trash_images.clear()
    metal_trash_images.clear()
    organic_trash_images.clear()
    glass_trash_images.clear()
    plastic_trash_images.clear()

    # --- Carregamento de Fundos e Cenas ---
    try:
        backGround = pygame.image.load(settings.ASSET_HOME_SCENE).convert()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_HOME_SCENE} - {e}")
    try:
        mikeScene01 = pygame.image.load(settings.ASSET_MIKE_SCENE_01).convert()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_MIKE_SCENE_01} - {e}")
    try:
        mikeScene02 = pygame.image.load(settings.ASSET_MIKE_SCENE_02).convert()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_MIKE_SCENE_02} - {e}")
    try:
        mikeScene03 = pygame.image.load(settings.ASSET_MIKE_SCENE_03).convert()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_MIKE_SCENE_03} - {e}")
    try:
        mikeScene04 = pygame.image.load(settings.ASSET_MIKE_SCENE_04).convert()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_MIKE_SCENE_04} - {e}")
    try:
        mikeScene05 = pygame.image.load(settings.ASSET_MIKE_SCENE_05).convert()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_MIKE_SCENE_05} - {e}")
    try:
        backGroundGaming = pygame.image.load(settings.ASSET_GAMING_SCENE).convert()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_GAMING_SCENE} - {e}")
    try:
        gameOver_bg_img = pygame.image.load(settings.ASSET_GAME_OVER_BG).convert()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_GAME_OVER_BG} - {e}")
    try:
        victory_screen_bg_img = pygame.image.load(
            settings.ASSET_VICTORY_SCREEN_BG
        ).convert()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_VICTORY_SCREEN_BG} - {e}")

    # Cutscenes Específicas
    try:
        mike_lvl2_intro_img = pygame.image.load(
            settings.ASSET_MIKE_LVL2_INTRO
        ).convert()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_MIKE_LVL2_INTRO} - {e}")
    try:
        mike_lvl1_explain_gameover_img = pygame.image.load(
            settings.ASSET_MIKE_LVL1_EXPLAIN_GAMEOVER
        ).convert()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_MIKE_LVL1_EXPLAIN_GAMEOVER} - {e}")
    try:
        mike_lvl2_explain_gameover_img = pygame.image.load(
            settings.ASSET_MIKE_LVL2_EXPLAIN_GAMEOVER
        ).convert()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_MIKE_LVL2_EXPLAIN_GAMEOVER} - {e}")

    # --- Carregamento de Lixeiras ---
    try:
        papperGarbage_bin_img = pygame.image.load(
            settings.ASSET_PAPER_BIN
        ).convert_alpha()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_PAPER_BIN} - {e}")
    try:
        metalGarbage_bin_img = pygame.image.load(
            settings.ASSET_METAL_BIN
        ).convert_alpha()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_METAL_BIN} - {e}")
    try:
        img_orig = pygame.image.load(settings.ASSET_ORGANIC_BIN).convert_alpha()
        organic_bin_img = pygame.transform.scale(
            img_orig, (settings.BIN_ORGANIC_WIDTH, settings.BIN_ORGANIC_HEIGHT)
        )
    except pygame.error as e:
        print(f"Erro ao carregar/redim. {settings.ASSET_ORGANIC_BIN}: {e}")
    try:
        img_orig = pygame.image.load(settings.ASSET_GLASS_BIN).convert_alpha()
        glass_bin_img = pygame.transform.scale(
            img_orig, (settings.BIN_GLASS_WIDTH, settings.BIN_GLASS_HEIGHT)
        )
    except pygame.error as e:
        print(f"Erro ao carregar/redim. {settings.ASSET_GLASS_BIN}: {e}")
    try:
        img_orig = pygame.image.load(settings.ASSET_PLASTIC_BIN).convert_alpha()
        plastic_bin_img = pygame.transform.scale(
            img_orig, (settings.BIN_PLASTIC_WIDTH, settings.BIN_PLASTIC_HEIGHT)
        )
    except pygame.error as e:
        print(f"Erro ao carregar/redim. {settings.ASSET_PLASTIC_BIN}: {e}")

    # --- Assets Comuns ---
    try:
        lifes_img = pygame.image.load(settings.ASSET_LIFES).convert_alpha()
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_LIFES} - {e}")
    try:
        player_img_original = pygame.image.load(settings.ASSET_PLAYER).convert_alpha()
        player_img = pygame.transform.scale(player_img_original, (100, 60))
    except pygame.error as e:
        print(f"Erro: {settings.ASSET_PLAYER} - {e}")

    # --- Carregamento e Redimensionamento de Lixos (com variedade) ---
    trash_size = (settings.TRASH_WIDTH, settings.TRASH_HEIGHT)
    _load_and_add_trash_variation(
        settings.ASSET_PAPER_AMASSADO, trash_size, paper_trash_images
    )
    _load_and_add_trash_variation(
        settings.ASSET_PAPER_CAIXA, trash_size, paper_trash_images
    )
    _load_and_add_trash_variation(
        settings.ASSET_METAL_LATA, trash_size, metal_trash_images
    )
    _load_and_add_trash_variation(
        settings.ASSET_METAL_SPRAY, trash_size, metal_trash_images
    )
    _load_and_add_trash_variation(
        settings.ASSET_ORGANIC_BANANA, trash_size, organic_trash_images
    )
    _load_and_add_trash_variation(
        settings.ASSET_ORGANIC_BROCOLIS, trash_size, organic_trash_images
    )
    _load_and_add_trash_variation(
        settings.ASSET_GLASS_GELEIA, trash_size, glass_trash_images
    )
    _load_and_add_trash_variation(
        settings.ASSET_GLASS_VINHO, trash_size, glass_trash_images
    )
    _load_and_add_trash_variation(
        settings.ASSET_PLASTIC_PET, trash_size, plastic_trash_images
    )

    # --- Carregamento de Fontes ---
    try:
        font_large = pygame.font.SysFont(
            settings.FONT_DEFAULT_SYS, settings.FONT_SIZE_LARGE
        )
        font_medium = pygame.font.SysFont(
            settings.FONT_DEFAULT_SYS, settings.FONT_SIZE_MEDIUM
        )
    except pygame.error:
        print("Aviso: Fonte Arial não encontrada, usando fonte padrão.")
        font_large = pygame.font.Font(None, settings.FONT_SIZE_LARGE)
        font_medium = pygame.font.Font(None, settings.FONT_SIZE_MEDIUM)
    try:
        font_pixel = pygame.font.Font(
            settings.FONT_PIXEL_PATH, settings.FONT_PIXEL_SIZE
        )
    except pygame.error as e:
        print(
            f"Aviso: Fonte pixel '{settings.FONT_PIXEL_PATH}' não encontrada ({e}). Usando fallback."
        )
        font_pixel = pygame.font.Font(None, settings.FONT_PIXEL_SIZE)

    print("Assets carregados com sucesso!")


def _load_and_add_trash_variation(asset_path, size, trash_list):
    if not asset_path:
        return
    try:
        original_img = pygame.image.load(asset_path).convert_alpha()
        scaled_img = pygame.transform.scale(original_img, size)
        trash_list.append(scaled_img)
    except pygame.error as e:
        print(f"Erro ao carregar/redimensionar lixo: {asset_path} - {e}")
