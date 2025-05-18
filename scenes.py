import pygame
import random
import settings
import assets
import utils
import game_state


def setup_gaming_scene():
    game_state.trash_items = []
    game_state.garbage_bins = []
    game_state.level_completed = False
    game_state.current_lifes = settings.MAX_LIFES
    game_state.dragging_item = None
    game_state.level_start_time = pygame.time.get_ticks()
    trash_types_to_spawn = []

    reference_bin_img_for_lvl2_width = (
        assets.organic_bin_img
        if assets.organic_bin_img
        else assets.papperGarbage_bin_img
    )  # Fallback

    if game_state.current_level == 1:
        game_state.time_remaining = settings.LEVEL_TIME_SECONDS_LVL1
        if assets.papperGarbage_bin_img:
            game_state.garbage_bins.append(
                {
                    "image": assets.papperGarbage_bin_img,
                    "rect": assets.papperGarbage_bin_img.get_rect(topleft=(450, 20)),
                    "type": "paper",
                }
            )
        if assets.metalGarbage_bin_img:
            game_state.garbage_bins.append(
                {
                    "image": assets.metalGarbage_bin_img,
                    "rect": assets.metalGarbage_bin_img.get_rect(topleft=(800, 20)),
                    "type": "metal",
                }
            )

        num_paper_trash_lvl1 = 3
        num_metal_trash_lvl1 = 3
        if assets.paper_trash_item_img:
            trash_types_to_spawn.append(
                {
                    "type": "paper",
                    "image": assets.paper_trash_item_img,
                    "count": num_paper_trash_lvl1,
                }
            )
        if assets.metal_trash_item_img:
            trash_types_to_spawn.append(
                {
                    "type": "metal",
                    "image": assets.metal_trash_item_img,
                    "count": num_metal_trash_lvl1,
                }
            )

    elif game_state.current_level == 2:
        game_state.time_remaining = settings.LEVEL_TIME_SECONDS_LVL2
        num_bins_lvl2 = 3  # Apenas 3 lixeiras
        bin_width_ref = (
            reference_bin_img_for_lvl2_width.get_width()
            if reference_bin_img_for_lvl2_width
            else settings.BIN_ORGANIC_WIDTH
        )

        total_bin_image_width = num_bins_lvl2 * bin_width_ref
        spacing_between_bins = 60  # Aumentar espaçamento
        total_spacing_width = (num_bins_lvl2 - 1) * spacing_between_bins
        block_width = total_bin_image_width + total_spacing_width
        bin_start_x = (settings.WINDOW_WIDTH - block_width) // 2
        bin_y_pos = 20

        current_x = bin_start_x
        if assets.organic_bin_img:
            game_state.garbage_bins.append(
                {
                    "image": assets.organic_bin_img,
                    "rect": assets.organic_bin_img.get_rect(
                        topleft=(current_x, bin_y_pos)
                    ),
                    "type": "organic",
                }
            )
            current_x += assets.organic_bin_img.get_width() + spacing_between_bins
        if assets.glass_bin_img:
            game_state.garbage_bins.append(
                {
                    "image": assets.glass_bin_img,
                    "rect": assets.glass_bin_img.get_rect(
                        topleft=(current_x, bin_y_pos)
                    ),
                    "type": "glass",
                }
            )
            current_x += assets.glass_bin_img.get_width() + spacing_between_bins
        if assets.plastic_bin_img:
            game_state.garbage_bins.append(
                {
                    "image": assets.plastic_bin_img,
                    "rect": assets.plastic_bin_img.get_rect(
                        topleft=(current_x, bin_y_pos)
                    ),
                    "type": "plastic",
                }
            )

        num_each_trash_lvl2 = 3
        if assets.organic_waste_item_img:
            trash_types_to_spawn.append(
                {
                    "type": "organic",
                    "image": assets.organic_waste_item_img,
                    "count": num_each_trash_lvl2,
                }
            )
        if assets.glass_waste_item_img:
            trash_types_to_spawn.append(
                {
                    "type": "glass",
                    "image": assets.glass_waste_item_img,
                    "count": num_each_trash_lvl2,
                }
            )
        if assets.plastic_waste_item_img:
            trash_types_to_spawn.append(
                {
                    "type": "plastic",
                    "image": assets.plastic_waste_item_img,
                    "count": num_each_trash_lvl2,
                }
            )

    all_trash_to_spawn_list = []
    for trash_spec in trash_types_to_spawn:
        if trash_spec["image"] is None:
            print(
                f"Aviso: Imagem para lixo tipo '{trash_spec['type']}' não carregada. Pulando spawn."
            )
            continue
        for _ in range(trash_spec["count"]):
            all_trash_to_spawn_list.append(
                {"type": trash_spec["type"], "image": trash_spec["image"]}
            )
    random.shuffle(all_trash_to_spawn_list)

    margin_x = 100
    reference_bin_height = 0
    if game_state.garbage_bins and game_state.garbage_bins[0]["image"]:
        reference_bin_height = game_state.garbage_bins[0]["image"].get_height()

    margin_y_top = reference_bin_height + 120 if reference_bin_height > 0 else 150

    margin_y_bottom = 100
    reference_trash_img = (
        assets.paper_trash_item_img
        if assets.paper_trash_item_img
        else pygame.Surface((1, 1))
    )  # Fallback

    spawn_area_x_start = margin_x
    spawn_area_x_end = (
        settings.WINDOW_WIDTH - margin_x - reference_trash_img.get_width()
    )
    spawn_area_y_start = margin_y_top
    spawn_area_y_end = (
        settings.WINDOW_HEIGHT - margin_y_bottom - reference_trash_img.get_height()
    )

    if spawn_area_x_end <= spawn_area_x_start or spawn_area_y_end <= spawn_area_y_start:
        print(
            "Aviso: Área de spawn inválida. Verifique as margens e tamanhos dos assets."
        )
        # Definir uma área de spawn mínima para evitar erro no random.randint
        spawn_area_x_end = max(spawn_area_x_start + 1, spawn_area_x_end)
        spawn_area_y_end = max(spawn_area_y_start + 1, spawn_area_y_end)

    for trash_info in all_trash_to_spawn_list:
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


def homeScene(window, main_loop_flag):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop_flag[0] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                next_img = (
                    assets.mikeScene01
                    if assets.mikeScene01
                    else assets.backGroundGaming
                )
                utils.fade_transition(window, assets.backGround, next_img)
                pygame.mixer.music.stop()
                if assets.mikeScene01:
                    utils.musicMike()
                    game_state.current_scene_name = "maike_intro_lvl1"
                    game_state.control_mike_scenes = 1
                else:  # Fallback se a cena do Mike não carregou
                    game_state.current_scene_name = "gaming"
                    setup_gaming_scene()  # Configura para o nível 1
                    utils.musicHome()
                game_state.current_level = 1
                return
    if assets.backGround:
        window.blit(assets.backGround, (0, 0))


def mikeScenes_Intro_Lvl1(window, main_loop_flag):
    current_mike_scene_img = None
    next_mike_scene_img_to_draw_after_event = None
    scenes_map = {
        1: assets.mikeScene01,
        2: assets.mikeScene02,
        3: assets.mikeScene03,
        4: assets.mikeScene04,
        5: assets.mikeScene05,
    }
    current_mike_scene_img = scenes_map.get(game_state.control_mike_scenes)

    if not current_mike_scene_img:
        print(
            f"Erro: Imagem para control_mike_scenes = {game_state.control_mike_scenes} não carregada. Pulando para jogo Nível 1."
        )
        game_state.current_scene_name = "gaming"
        game_state.current_level = 1
        setup_gaming_scene()
        utils.musicHome()
        return

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop_flag[0] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                next_control_state = game_state.control_mike_scenes + 1
                if next_control_state > 5:
                    utils.fade_transition(
                        window, current_mike_scene_img, assets.backGroundGaming
                    )
                    game_state.current_level = 1
                    setup_gaming_scene()
                    utils.musicHome()
                    game_state.current_scene_name = "gaming"
                    return
                else:
                    temp_next_scene_img = scenes_map.get(next_control_state)
                    if (
                        temp_next_scene_img and current_mike_scene_img
                    ):  # Garante que ambas imagens existem para fade
                        utils.fade_transition(
                            window, current_mike_scene_img, temp_next_scene_img
                        )
                        utils.musicMike()
                        game_state.control_mike_scenes = next_control_state
                        next_mike_scene_img_to_draw_after_event = temp_next_scene_img
                    else:
                        print(
                            f"Aviso: Próxima imagem da cena do Mike ({next_control_state}) não carregada. Pulando para jogo."
                        )
                        utils.fade_transition(
                            window,
                            (
                                current_mike_scene_img
                                if current_mike_scene_img
                                else assets.backGround
                            ),
                            assets.backGroundGaming,
                        )
                        game_state.current_level = 1
                        setup_gaming_scene()
                        utils.musicHome()
                        game_state.current_scene_name = "gaming"
                    return
    if next_mike_scene_img_to_draw_after_event:
        window.blit(next_mike_scene_img_to_draw_after_event, (0, 0))
    elif current_mike_scene_img:
        window.blit(current_mike_scene_img, (0, 0))


def mikeScenes_Intro_Lvl2(window, main_loop_flag):
    current_scene_image = assets.mike_lvl2_intro_img
    if not current_scene_image:
        print(
            "Erro: Imagem da cutscene Mike Nível 2 Intro não carregada. Indo para o jogo Nível 2."
        )
        game_state.current_level = 2
        setup_gaming_scene()
        utils.musicHome()
        game_state.current_scene_name = "gaming"
        return

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop_flag[0] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                utils.fade_transition(
                    window, current_scene_image, assets.backGroundGaming
                )
                game_state.current_level = 2
                setup_gaming_scene()
                utils.musicHome()
                game_state.current_scene_name = "gaming"
                return
    window.blit(current_scene_image, (0, 0))


def mikeScenes_Explain_Lvl2_GameOver(window, main_loop_flag):
    current_scene_image = assets.mike_lvl2_explain_img
    if not current_scene_image:
        print(
            "Erro: Imagem da cutscene Mike Nível 2 Explain (Game Over) não carregada. Indo para tela de Game Over."
        )
        game_state.current_scene_name = "game_over_final"
        return

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop_flag[0] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                next_img_for_fade = (
                    assets.gameOver_bg_img
                    if assets.gameOver_bg_img
                    else assets.backGroundGaming
                )  # Fallback
                utils.fade_transition(window, current_scene_image, next_img_for_fade)
                game_state.current_scene_name = "game_over_final"
                return
    window.blit(current_scene_image, (0, 0))


def gamingScene(window, main_loop_flag):
    time_limit_for_level = (
        settings.LEVEL_TIME_SECONDS_LVL1
        if game_state.current_level == 1
        else settings.LEVEL_TIME_SECONDS_LVL2
    )
    if (
        not game_state.level_completed
        and game_state.current_lifes > 0
        and game_state.current_scene_name == "gaming"
    ):
        current_ticks = pygame.time.get_ticks()
        elapsed_seconds = (current_ticks - game_state.level_start_time) // 1000
        game_state.time_remaining = time_limit_for_level - elapsed_seconds
        if game_state.time_remaining <= 0:
            game_state.time_remaining = 0
            if game_state.current_scene_name == "gaming":
                print("Tempo esgotado! Game Over.")
                game_state.current_scene_name = (
                    "game_over_final"  # Direto para a tela final
                )
                pygame.mixer.music.stop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop_flag[0] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (
                event.button == 1
                and not game_state.level_completed
                and game_state.current_lifes > 0
                and game_state.time_remaining > 0
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
                            if game_state.dragging_item in game_state.trash_items:
                                game_state.trash_items.remove(game_state.dragging_item)
                        else:
                            game_state.current_lifes -= 1
                            print(
                                f"Lixeira errada! Vidas restantes: {game_state.current_lifes}"
                            )
                            game_state.dragging_item["rect"].topleft = (
                                game_state.dragging_item["initial_pos"]
                            )
                            if (
                                game_state.current_lifes <= 0
                                and game_state.current_scene_name == "gaming"
                            ):
                                print("Game Over! (Sem vidas)")
                                game_state.current_scene_name = "mike_explain_lvl2_gameover"  # Vai para cutscene de explicação
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
        if bin_obj["image"]:
            window.blit(bin_obj["image"], bin_obj["rect"])
    for item in game_state.trash_items:
        if item != game_state.dragging_item and item["image"]:
            window.blit(item["image"], item["rect"])
    if game_state.dragging_item and game_state.dragging_item["image"]:
        window.blit(game_state.dragging_item["image"], game_state.dragging_item["rect"])

    if assets.lifes_img:
        life_heart_width = assets.lifes_img.get_width()
        life_heart_spacing = 10
        life_start_x = 40
        life_start_y = 20
        for i in range(game_state.current_lifes):
            pos_x = life_start_x + i * (life_heart_width + life_heart_spacing)
            window.blit(assets.lifes_img, (pos_x, life_start_y))
    if (
        assets.player_img and assets.lifes_img
    ):  # Verifica se lifes_img existe para posicionamento
        life_heart_width = assets.lifes_img.get_width()
        player_pos_x = (
            life_start_x
            + (life_heart_width // 2)
            - (assets.player_img.get_width() // 2)
        )
        player_pos_y = life_start_y + assets.lifes_img.get_height() + 5
        window.blit(assets.player_img, (player_pos_x, player_pos_y))

    if assets.font_medium:
        timer_text_surface = assets.font_medium.render(
            f"Tempo: {max(0, game_state.time_remaining)}s", True, settings.BLACK
        )
        timer_text_rect = timer_text_surface.get_rect(
            topright=(settings.WINDOW_WIDTH - 20, 20)
        )
        window.blit(timer_text_surface, timer_text_rect)

    if (
        not game_state.trash_items
        and not game_state.dragging_item
        and game_state.current_scene_name == "gaming"
        and not game_state.level_completed
        and game_state.current_lifes > 0
        and game_state.time_remaining > 0
    ):
        game_state.level_completed = True
        pygame.mixer.music.stop()
        if game_state.current_level == 1:
            print("Nível 1 Concluído! Indo para a introdução do Nível 2.")
            next_image_for_fade = (
                assets.mike_lvl2_intro_img
                if assets.mike_lvl2_intro_img
                else assets.backGroundGaming
            )
            if (
                assets.backGroundGaming and next_image_for_fade
            ):  # Garante que ambas imagens existem
                utils.fade_transition(
                    window, assets.backGroundGaming, next_image_for_fade
                )
            utils.musicMike()
            game_state.current_scene_name = "maike_intro_lvl2"
        elif game_state.current_level == 2:
            print("Nível 2 Concluído! Você zerou o jogo!")
            game_state.current_scene_name = "victory_screen"


def gameOverScene_Final(window, main_loop_flag):
    if assets.gameOver_bg_img:
        scaled_game_over_bg = pygame.transform.scale(
            assets.gameOver_bg_img, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
        )
        window.blit(scaled_game_over_bg, (0, 0))
    else:
        window.fill(settings.DARK_GREY)
        if assets.font_large:
            game_over_text_surface = assets.font_large.render(
                "GAME OVER", True, settings.RED
            )
            text_rect = game_over_text_surface.get_rect(
                center=(settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2)
            )
            window.blit(game_over_text_surface, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop_flag[0] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                if settings.GAMEOVER_RETRY_BUTTON_RECT.collidepoint(mouse_pos):
                    print("Botão Retry clicado")
                    game_state.current_scene_name = "home"
                    game_state.control_mike_scenes = 1
                    game_state.current_level = 1
                    utils.musicHome()
                    return
                elif settings.GAMEOVER_QUIT_BUTTON_RECT.collidepoint(mouse_pos):
                    print("Botão Quit clicado")
                    main_loop_flag[0] = False
                    return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_state.current_scene_name = "home"
                game_state.control_mike_scenes = 1
                game_state.current_level = 1
                utils.musicHome()
                return
            if event.key == pygame.K_ESCAPE:
                main_loop_flag[0] = False
                return


def victoryScreen(window, main_loop_flag):
    window.fill(settings.WHITE)
    if assets.font_large and assets.font_medium:
        victory_text_surface = assets.font_large.render(
            "PARABÉNS!", True, settings.BLACK
        )
        text_rect = victory_text_surface.get_rect(
            center=(settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2 - 50)
        )
        instruction_text = assets.font_medium.render(
            "Você completou todos os níveis!", True, settings.BLACK
        )
        instruction_rect = instruction_text.get_rect(
            center=(settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2 + 20)
        )
        home_text = assets.font_medium.render(
            "Pressione ENTER para voltar à Home", True, settings.BLACK
        )
        home_rect = home_text.get_rect(
            center=(settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2 + 80)
        )
        window.blit(victory_text_surface, text_rect)
        window.blit(instruction_text, instruction_rect)
        window.blit(home_text, home_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop_flag[0] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                game_state.current_scene_name = "home"
                game_state.control_mike_scenes = 1
                game_state.current_level = 1
                utils.musicHome()
                return
