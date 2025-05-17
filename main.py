import pygame
import settings
import assets
import utils
import scenes
import game_state  # Para acessar o nome da cena atual


def main():
    pygame.init()
    window = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    pygame.display.set_caption(settings.GAME_CAPTION)
    clock = pygame.time.Clock()  # Para controlar o FPS

    assets.load_all_assets()  # Carrega todos os assets uma vez
    utils.musicHome()  # Inicia a música da home

    # Para controlar o loop principal a partir das cenas
    # Usamos uma lista para que a modificação dentro da função seja refletida aqui
    main_loop_running = [True]

    while main_loop_running[0]:
        if game_state.current_scene_name == "home":
            scenes.homeScene(window, main_loop_running)
        elif game_state.current_scene_name == "maike":
            scenes.mikeScenes(window, main_loop_running)
        elif game_state.current_scene_name == "gaming":
            scenes.gamingScene(window, main_loop_running)
        elif game_state.current_scene_name == "game_over":
            scenes.gameOverScene(window, main_loop_running)

        pygame.display.update()
        clock.tick(60)  # Limita o jogo a 60 FPS

    pygame.quit()


if __name__ == "__main__":
    main()
