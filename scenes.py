import pygame
import random
import settings
import assets  # Para acessar as imagens carregadas
import utils  # Para fade_transition e música
import game_state  # Para acessar e modificar o estado do jogo


def setup_gaming_scene():
    game_state.trash_items = []
    game_state.garbage_bins = []
    game_state.level_completed = False
    game_state.current_lifes = settings.MAX_LIFES

    game_state.garbage_bins.append(
        {
            "image": assets.papperGarbage_bin_img,
            "rect": assets.papperGarbage_bin_img.get_rect(topleft=(450, 10)),
            "type": "paper",
        }
    )
    game_state.garbage_bins.append(
        {
            "image": assets.metalGarbage_bin_img,
            "rect": assets.metalGarbage_bin_img.get_rect(topleft=(800, 10)),
            "type": "metal",
        }
    )

    margin_x = 100
    margin_y_top = assets.papperGarbage_bin_img.get_height() + 120
    margin_y_bottom = 100
    spawn_area_x_start = margin_x
    spawn_area_x_end = (
        settings.WINDOW_WIDTH - margin_x - assets.paper_trash_item_img.get_width()
    )
    spawn_area_y_start = margin_y_top
    spawn_area_y_end = (
        settings.WINDOW_HEIGHT
        - margin_y_bottom
        - assets.paper_trash_item_img.get_height()
    )

    num_paper_trash = 3
    num_metal_trash = 3
    all_trash_to_spawn = []
    for _ in range(num_paper_trash):
        all_trash_to_spawn.append(
            {"type": "paper", "image": assets.paper_trash_item_img}
        )
    for _ in range(num_metal_trash):
        all_trash_to_spawn.append(
            {"type": "metal", "image": assets.metal_trash_item_img}
        )
    random.shuffle(all_trash_to_spawn)

    for trash_info in all_trash_to_spawn:
        placed = False
        attempts = 0
        while not placed and attempts < 100:
            pos_x = random.randint(spawn_area_x_start, spawn_area_x_end)
            pos_y = random.randint(spawn_area_y_start, spawn_area_y_end)
            new_trash_rect = trash_info["image"].get_rect(topleft=(pos_x, pos_y))
            collision_with_other_trash = False
            for existing_item in game_state.trash_items:
                if new_trash_rect.colliderect(
                    existing_item["rect"].inflate(
                        settings.MIN_DISTANCE_BETWEEN_TRASH,
                        settings.MIN_DISTANCE_BETWEEN_TRASH,
                    )
                ):
                    collision_with_other_trash = True
                    break
            if not collision_with_other_trash:
                game_state.trash_items.append(
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
                f"Aviso: Não foi possível posicionar um lixo do tipo {trash_info['type']}."
            )


def homeScene(window, main_loop_flag):  # main_loop_flag é uma lista [True] ou um objeto
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop_flag[0] = False  # Modifica o valor dentro da lista
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                utils.fade_transition(window, assets.backGround, assets.mikeScene01)
                pygame.mixer.music.stop()
                utils.musicMike()
                game_state.current_scene_name = "maike"
                game_state.control_mike_scenes = 1
                return
    window.blit(assets.backGround, (0, 0))


def mikeScenes(window, main_loop_flag):
    current_mike_scene_img = None
    next_mike_scene_img_to_draw_after_event = None

    if game_state.control_mike_scenes == 1:
        current_mike_scene_img = assets.mikeScene01
    elif game_state.control_mike_scenes == 2:
        current_mike_scene_img = assets.mikeScene02
    elif game_state.control_mike_scenes == 3:
        current_mike_scene_img = assets.mikeScene03
    elif game_state.control_mike_scenes == 4:
        current_mike_scene_img = assets.mikeScene04
    elif game_state.control_mike_scenes == 5:
        current_mike_scene_img = assets.mikeScene05

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop_flag[0] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                temp_next_scene_img = None
                if game_state.control_mike_scenes == 1:
                    temp_next_scene_img = assets.mikeScene02
                    game_state.control_mike_scenes = 2
                elif game_state.control_mike_scenes == 2:
                    temp_next_scene_img = assets.mikeScene03
                    game_state.control_mike_scenes = 3
                elif game_state.control_mike_scenes == 3:
                    temp_next_scene_img = assets.mikeScene04
                    game_state.control_mike_scenes = 4
                elif game_state.control_mike_scenes == 4:
                    temp_next_scene_img = assets.mikeScene05
                    game_state.control_mike_scenes = 5
                elif game_state.control_mike_scenes == 5:
                    utils.fade_transition(
                        window, assets.mikeScene05, assets.backGroundGaming
                    )
                    setup_gaming_scene()
                    utils.musicHome()
                    game_state.current_scene_name = "gaming"
                    return

                if temp_next_scene_img:
                    utils.fade_transition(
                        window, current_mike_scene_img, temp_next_scene_img
                    )
                    utils.musicMike()
                    next_mike_scene_img_to_draw_after_event = temp_next_scene_img
                return  # Importante retornar para redesenhar a cena correta

    if next_mike_scene_img_to_draw_after_event:
        window.blit(next_mike_scene_img_to_draw_after_event, (0, 0))
    elif current_mike_scene_img:
        window.blit(current_mike_scene_img, (0, 0))


def gamingScene(window, main_loop_flag):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop_flag[0] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (
                event.button == 1
                and not game_state.level_completed
                and game_state.current_lifes > 0
            ):
                for i in range(len(game_state.trash_items) - 1, -1, -1):
                    item = game_state.trash_items[i]
                    if item["rect"].collidepoint(event.pos):
                        game_state.dragging_item = item
                        game_state.mouse_offset_x = item["rect"].x - event.pos[0]
                        game_state.mouse_offset_y = item["rect"].y - event.pos[1]
                        game_state.trash_items.pop(i)
                        game_state.trash_items.append(item)
                        break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and game_state.dragging_item:
                collided_with_any_bin = False
                for bin_obj in game_state.garbage_bins:
                    if game_state.dragging_item["rect"].colliderect(bin_obj["rect"]):
                        collided_with_any_bin = True
                        if game_state.dragging_item["type"] == bin_obj["type"]:
                            print(
                                f"Lixo de {game_state.dragging_item['type']} descartado corretamente!"
                            )
                            if game_state.dragging_item in game_state.trash_items:
                                game_state.trash_items.remove(game_state.dragging_item)
                        else:
                            print(
                                f"Lixeira errada para {game_state.dragging_item['type']}! Perdeu uma vida."
                            )
                            game_state.current_lifes -= 1
                            print(f"Vidas restantes: {game_state.current_lifes}")
                            game_state.dragging_item["rect"].topleft = (
                                game_state.dragging_item["initial_pos"]
                            )
                            if game_state.current_lifes <= 0:
                                print("Game Over!")
                                game_state.current_scene_name = "game_over"
                                pygame.mixer.music.stop()
                        break
                if not collided_with_any_bin:
                    game_state.dragging_item["rect"].topleft = game_state.dragging_item[
                        "initial_pos"
                    ]
                game_state.dragging_item = None
        elif event.type == pygame.MOUSEMOTION:
            if game_state.dragging_item:
                game_state.dragging_item["rect"].x = (
                    event.pos[0] + game_state.mouse_offset_x
                )
                game_state.dragging_item["rect"].y = (
                    event.pos[1] + game_state.mouse_offset_y
                )

    window.blit(assets.backGroundGaming, (0, 0))
    for bin_obj in game_state.garbage_bins:
        window.blit(bin_obj["image"], bin_obj["rect"])
    for item in game_state.trash_items:
        if item != game_state.dragging_item:
            window.blit(item["image"], item["rect"])
    if game_state.dragging_item:
        window.blit(game_state.dragging_item["image"], game_state.dragging_item["rect"])

    window.blit(assets.player_img, (0, 0))
    life_heart_width = assets.lifes_img.get_width()
    life_heart_spacing = 10
    life_start_x = 40
    life_start_y = 20
    for i in range(game_state.current_lifes):
        pos_x = life_start_x + i * (life_heart_width + life_heart_spacing)
        window.blit(assets.lifes_img, (pos_x, life_start_y))

    if (
        not game_state.trash_items
        and not game_state.dragging_item
        and game_state.current_scene_name == "gaming"
        and not game_state.level_completed
        and game_state.current_lifes > 0
    ):
        print("Nível Concluído! Todo o lixo foi coletado.")
        game_state.level_completed = True

    if game_state.current_lifes <= 0 and game_state.current_scene_name == "gaming":
        game_state.current_scene_name = "game_over"
        pygame.mixer.music.stop()


def gameOverScene(window, main_loop_flag):
    window.fill(settings.DARK_GREY)
    game_over_text_surface = assets.font_large.render("GAME OVER", True, settings.RED)
    instruction_text_surface = assets.font_large.render(
        "Pressione ENTER para reiniciar", True, settings.LIGHT_GREY
    )
    instruction_small_surface = assets.font_medium.render(
        "ou ESC para sair", True, settings.LIGHT_GREY
    )

    text_rect = game_over_text_surface.get_rect(
        center=(settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2 - 60)
    )
    instruction_rect = instruction_text_surface.get_rect(
        center=(settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2 + 40)
    )
    instruction_small_rect = instruction_small_surface.get_rect(
        center=(settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2 + 110)
    )

    window.blit(game_over_text_surface, text_rect)
    window.blit(instruction_text_surface, instruction_rect)
    window.blit(instruction_small_surface, instruction_small_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop_flag[0] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                setup_gaming_scene()
                game_state.current_scene_name = "gaming"
                utils.musicHome()
                return
            if event.key == pygame.K_ESCAPE:
                main_loop_flag[0] = False
                return
