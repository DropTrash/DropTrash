import pygame
import settings
import assets
import utils
import scenes
import game_state


def main():
    pygame.init()
    pygame.mixer.init()

    window = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    pygame.display.set_caption(settings.GAME_CAPTION)
    clock = pygame.time.Clock()

    assets.load_all_assets()
    utils.musicHome()

    main_loop_running = [True]

    while main_loop_running[0]:
        current_scene = game_state.current_scene_name
        if current_scene == "home":
            scenes.homeScene(window, main_loop_running)
        elif current_scene == "maike_intro_lvl1":
            scenes.mikeScenes_Intro_Lvl1(window, main_loop_running)
        elif current_scene == "maike_intro_lvl2":
            scenes.mikeScenes_Intro_Lvl2(window, main_loop_running)
        elif current_scene == "mike_explain_lvl1_gameover":  
            scenes.mikeScenes_Explain_Lvl1_GameOver(window, main_loop_running)
        elif current_scene == "mike_explain_lvl2_gameover":
            scenes.mikeScenes_Explain_Lvl2_GameOver(window, main_loop_running)
        elif current_scene == "gaming":
            scenes.gamingScene(window, main_loop_running)
        elif current_scene == "game_over_final":
            scenes.gameOverScene_Final(window, main_loop_running)
        elif current_scene == "victory_screen":
            scenes.victoryScreen(window, main_loop_running)
        else:
            print(f"ERRO: Cena desconhecida '{current_scene}'. Voltando para home.")
            game_state.current_scene_name = "home"

        pygame.display.update()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
