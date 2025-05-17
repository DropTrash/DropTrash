import pygame
import random

pygame.init()

# Comandos das propriedades da janela
window_width = 1472
window_height = 832
window = pygame.display.set_mode([window_width, window_height])
pygame.display.set_caption("Drop Trash")

# --- ASSETS (RECURSOS) ---
backGround = None
mikeScene01, mikeScene02, mikeScene03, mikeScene04, mikeScene05 = (
    None,
    None,
    None,
    None,
    None,
)
backGroundGaming = None
papperGarbage_bin_img = None
metalGarbage_bin_img = None
lifes_img = None  
player_img = None
paper_trash_item_img = None
metal_trash_item_img = None
font = None  
# --- END ASSETS ---


# --- VARIÁVEIS DE ESTADO DO JOGO ---
trash_items = []
garbage_bins = []
dragging_item = None
mouse_offset_x = 0
mouse_offset_y = 0
level_completed = False

# Vidas
max_lifes = 3
current_lifes = max_lifes
# --- END GAME STATE VARIABLES ---


# Funções do jogo
def musicHome():
    pygame.mixer.music.load("music/natureSound.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)


def musicMike():
    pygame.mixer.music.load("music/mikeSound.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)


def images():
    global backGround, mikeScene01, mikeScene02, mikeScene03, mikeScene04, mikeScene05
    global backGroundGaming, papperGarbage_bin_img, metalGarbage_bin_img
    global lifes_img, player_img, paper_trash_item_img, metal_trash_item_img
    global font  

    backGround = pygame.image.load("assets/HomeScene.png")
    mikeScene01 = pygame.image.load("assets/MikeScene01.png")
    mikeScene02 = pygame.image.load("assets/MikeScene02.png")
    mikeScene03 = pygame.image.load("assets/MikeScene03.png")
    mikeScene04 = pygame.image.load("assets/MikeScene04.png")
    mikeScene05 = pygame.image.load("assets/MikeScene05.png")
    backGroundGaming = pygame.image.load("assets/GamingScene.png")
    papperGarbage_bin_img = pygame.image.load("assets/Level01/PapperGarbage.png")
    metalGarbage_bin_img = pygame.image.load("assets/Level01/MetalGarbage.png")
    lifes_img = pygame.image.load("assets/Lifes.png")  
    player_img = pygame.image.load("assets/Player.png")
    player_img = pygame.transform.scale(player_img, (350, 200))

    paper_trash_item_img_original = pygame.image.load(
        "assets/Level01/PaperWaste.png"
    ).convert_alpha()
    metal_trash_item_img_original = pygame.image.load(
        "assets/Level01/SodaCan.png"
    ).convert_alpha()

    trash_width = 70  
    trash_height = 70
    paper_trash_item_img = pygame.transform.scale(
        paper_trash_item_img_original, (trash_width, trash_height)
    )
    metal_trash_item_img = pygame.transform.scale(
        metal_trash_item_img_original, (trash_width, trash_height)
    )

    # Carregar uma fonte para a tela de Game Over
    try:
        font = pygame.font.SysFont("Arial", 72)  # Tenta carregar uma fonte do sistema
    except pygame.error:
        font = pygame.font.Font(None, 72)  # Se falhar, usa a fonte padrão do Pygame


def fade_transition(surface, currentImg, nextImg, speed=10):
    fade_surface = pygame.Surface((window_width, window_height))
    fade_surface.fill((0, 0, 0))
    for alpha in range(0, 255, speed):
        surface.blit(currentImg, (0, 0))
        fade_surface.set_alpha(alpha)
        surface.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)
    for alpha in range(255, 0, -speed):
        surface.blit(nextImg, (0, 0))
        fade_surface.set_alpha(alpha)
        surface.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)
    surface.blit(nextImg, (0, 0))
    pygame.display.update()


def homeScene():
    global loop, scenes, controlMikeScenes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                fade_transition(window, backGround, mikeScene01)
                pygame.mixer.music.stop()
                musicMike()
                scenes = "maike"
                controlMikeScenes = 1
                return
    window.blit(backGround, (0, 0))


def mikeScenes():
    global loop, scenes, controlMikeScenes
    current_mike_scene_img = None
    next_mike_scene_img_to_draw_after_event = None  

    if controlMikeScenes == 1:
        current_mike_scene_img = mikeScene01
    elif controlMikeScenes == 2:
        current_mike_scene_img = mikeScene02
    elif controlMikeScenes == 3:
        current_mike_scene_img = mikeScene03
    elif controlMikeScenes == 4:
        current_mike_scene_img = mikeScene04
    elif controlMikeScenes == 5:
        current_mike_scene_img = mikeScene05

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                temp_next_scene_img = None
                if controlMikeScenes == 1:
                    temp_next_scene_img = mikeScene02
                    controlMikeScenes = 2
                elif controlMikeScenes == 2:
                    temp_next_scene_img = mikeScene03
                    controlMikeScenes = 3
                elif controlMikeScenes == 3:
                    temp_next_scene_img = mikeScene04
                    controlMikeScenes = 4
                elif controlMikeScenes == 4:
                    temp_next_scene_img = mikeScene05
                    controlMikeScenes = 5
                elif controlMikeScenes == 5:
                    fade_transition(window, mikeScene05, backGroundGaming)
                    setup_gaming_scene()
                    musicHome()  
                    scenes = "gaming"
                    return  

                if temp_next_scene_img:
                    fade_transition(window, current_mike_scene_img, temp_next_scene_img)
                    musicMike()
                    next_mike_scene_img_to_draw_after_event = temp_next_scene_img
                return  

    # Desenha a cena apropriada do Mike
    if next_mike_scene_img_to_draw_after_event:
        window.blit(next_mike_scene_img_to_draw_after_event, (0, 0))
    elif current_mike_scene_img:
        window.blit(current_mike_scene_img, (0, 0))


def setup_gaming_scene():
    global trash_items, garbage_bins, level_completed, current_lifes 

    trash_items = []
    garbage_bins = []
    level_completed = False
    current_lifes = max_lifes  # Reseta as vidas

    garbage_bins.append(
        {
            "image": papperGarbage_bin_img,
            "rect": papperGarbage_bin_img.get_rect(topleft=(450, 10)),
            "type": "paper",
        }
    )
    garbage_bins.append(
        {
            "image": metalGarbage_bin_img,
            "rect": metalGarbage_bin_img.get_rect(topleft=(800, 10)),
            "type": "metal",
        }
    )

    margin_x = 100
    margin_y_top = papperGarbage_bin_img.get_height() + 120  
    margin_y_bottom = 100
    spawn_area_x_start = margin_x
    spawn_area_x_end = window_width - margin_x - paper_trash_item_img.get_width()
    spawn_area_y_start = margin_y_top
    spawn_area_y_end = (
        window_height - margin_y_bottom - paper_trash_item_img.get_height()
    )

    num_paper_trash = 3
    num_metal_trash = 3
    all_trash_to_spawn = []
    for _ in range(num_paper_trash):
        all_trash_to_spawn.append({"type": "paper", "image": paper_trash_item_img})
    for _ in range(num_metal_trash):
        all_trash_to_spawn.append({"type": "metal", "image": metal_trash_item_img})
    random.shuffle(all_trash_to_spawn)
    min_distance_between_trash = 70  

    for trash_info in all_trash_to_spawn:
        placed = False
        attempts = 0
        while not placed and attempts < 100:
            pos_x = random.randint(spawn_area_x_start, spawn_area_x_end)
            pos_y = random.randint(spawn_area_y_start, spawn_area_y_end)
            new_trash_rect = trash_info["image"].get_rect(topleft=(pos_x, pos_y))
            collision_with_other_trash = False
            for existing_item in trash_items:
                if new_trash_rect.colliderect(
                    existing_item["rect"].inflate(
                        min_distance_between_trash, min_distance_between_trash
                    )
                ):
                    collision_with_other_trash = True
                    break
            if not collision_with_other_trash:
                trash_items.append(
                    {
                        "image": trash_info["image"],
                        "rect": new_trash_rect,
                        "type": trash_info["type"],
                        "initial_pos": (pos_x, pos_y),
                    }
                )
                placed = True
            attempts += 1
        if not placed:
            print(
                f"Não foi possível posicionar um lixo do tipo {trash_info['type']} sem sobreposição significativa."
            )


def gamingScene():
    global loop, scenes, dragging_item, mouse_offset_x, mouse_offset_y, trash_items
    global level_completed, current_lifes  # Adiciona current_lifes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (
                event.button == 1 and not level_completed and current_lifes > 0
            ):  # Só pode arrastar se tiver vidas
                for i in range(len(trash_items) - 1, -1, -1):
                    item = trash_items[i]
                    if item["rect"].collidepoint(event.pos):
                        dragging_item = item
                        mouse_offset_x = item["rect"].x - event.pos[0]
                        mouse_offset_y = item["rect"].y - event.pos[1]
                        trash_items.pop(
                            i
                        )  
                        trash_items.append(
                            item
                        )  
                        break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and dragging_item:
                dropped_correctly = False
                collided_with_any_bin = False

                for bin_obj in garbage_bins:
                    if dragging_item["rect"].colliderect(bin_obj["rect"]):
                        collided_with_any_bin = True
                        if dragging_item["type"] == bin_obj["type"]:
                            print(
                                f"Lixo de {dragging_item['type']} descartado corretamente!"
                            )
                            if (
                                dragging_item in trash_items
                            ):  
                                trash_items.remove(dragging_item)
                            dropped_correctly = True
                        else:  
                            print(
                                f"Lixeira errada para {dragging_item['type']}! Perdeu uma vida."
                            )
                            current_lifes -= 1
                            print(f"Vidas restantes: {current_lifes}")
                            dragging_item["rect"].topleft = dragging_item["initial_pos"]
                            if current_lifes <= 0:
                                print("Game Over!")
                                scenes = "game_over"  # Mudar para cena de game over
                                pygame.mixer.music.stop()  
                        break  # Já interagiu com uma lixeira

                if not collided_with_any_bin:  # Não colidiu com nenhuma lixeira
                    # Lixo volta para a posição inicial
                    dragging_item["rect"].topleft = dragging_item["initial_pos"]

                dragging_item = None  # Para de arrastar

        elif event.type == pygame.MOUSEMOTION:
            if dragging_item:
                dragging_item["rect"].x = event.pos[0] + mouse_offset_x
                dragging_item["rect"].y = event.pos[1] + mouse_offset_y

    # --- Desenho ---
    window.blit(backGroundGaming, (0, 0))
    for bin_obj in garbage_bins:
        window.blit(bin_obj["image"], bin_obj["rect"])

    # Desenha os itens de lixo que ainda não foram coletados e não estão sendo arrastados
    for item in trash_items:
        if item != dragging_item:  # Não desenha o item que está sendo arrastado aqui
            window.blit(item["image"], item["rect"])
    # Desenha o item sendo arrastado por cima, se houver um
    if dragging_item:
        window.blit(dragging_item["image"], dragging_item["rect"])

    window.blit(player_img, (0, 0))  # Personagem/Avatar

    # Desenhar vidas
    life_heart_width = lifes_img.get_width()
    life_heart_spacing = 10
    life_start_x = 40  # Posição X inicial do primeiro coração
    life_start_y = 20  # Posição Y dos corações

    for i in range(current_lifes):
        pos_x = life_start_x + i * (life_heart_width + life_heart_spacing)
        window.blit(lifes_img, (pos_x, life_start_y))

    if (
        not trash_items
        and not dragging_item
        and scenes == "gaming"
        and not level_completed
        and current_lifes > 0
    ):
        print("Nível Concluído! Todo o lixo foi coletado.")
        level_completed = True

    if (
        current_lifes <= 0 and scenes == "gaming"
    ):  # Checa se mudou para game_over dentro do loop de eventos
        scenes = "game_over"
        pygame.mixer.music.stop()


def gameOverScene():
    global loop, scenes
    window.fill((30, 30, 30))  # Fundo escuro para game over

    game_over_text = font.render("GAME OVER", True, (255, 0, 0))  # Vermelho
    instruction_text = font.render(
        "Pressione ENTER para reiniciar", True, (200, 200, 200)
    )  # Cinza claro
    instruction_text_small = pygame.font.Font(None, 48).render(
        "ou ESC para sair", True, (200, 200, 200)
    )

    text_rect = game_over_text.get_rect(
        center=(window_width / 2, window_height / 2 - 50)
    )
    instruction_rect = instruction_text.get_rect(
        center=(window_width / 2, window_height / 2 + 50)
    )
    instruction_small_rect = instruction_text_small.get_rect(
        center=(window_width / 2, window_height / 2 + 110)
    )

    window.blit(game_over_text, text_rect)
    window.blit(instruction_text, instruction_rect)
    window.blit(instruction_text_small, instruction_small_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                setup_gaming_scene()  # Prepara um novo jogo
                scenes = "gaming"  # Volta para a cena de jogo
                musicHome()  # Reinicia a música (ou música do jogo)
                return
            if event.key == pygame.K_ESCAPE:
                loop = False  # Sai do jogo
                return


# Inicialização do jogo
images()
musicHome()
loop = True
scenes = "home"
controlMikeScenes = 1

# Loop principal do jogo
while loop:
    if scenes == "home":
        homeScene()
    elif scenes == "maike":
        mikeScenes()
    elif scenes == "gaming":
        gamingScene()
    elif scenes == "game_over":  # Adiciona a nova cena ao loop
        gameOverScene()

    pygame.display.update()
pygame.quit()
# --- END OF FILE main.py ---
