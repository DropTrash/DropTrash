import pygame
import settings


def musicHome():
    try:
        pygame.mixer.music.load(settings.MUSIC_NATURE)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
    except pygame.error as e:
        print(f"Erro ao carregar/tocar música da home: {e}")


def musicMike():
    try:
        pygame.mixer.music.load(settings.MUSIC_MIKE)
        pygame.mixer.music.play()  # Toca uma vez
        pygame.mixer.music.set_volume(0.5)
    except pygame.error as e:
        print(f"Erro ao carregar/tocar música do Mike: {e}")


def fade_transition(surface, currentImg, nextImg, speed=10):
    if not currentImg or not nextImg:
        print("Aviso: Imagem de transição ausente, pulando fade.")
        if nextImg:
            surface.blit(nextImg, (0, 0))
            pygame.display.update()
        return

    fade_surface = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    fade_surface.fill(settings.BLACK)
    clock = pygame.time.Clock()

    for alpha in range(0, 255 + speed, speed):
        alpha = min(alpha, 255)
        surface.blit(currentImg, (0, 0))
        fade_surface.set_alpha(alpha)
        surface.blit(fade_surface, (0, 0))
        pygame.display.update()
        clock.tick(60)

    for alpha in range(255, 0 - speed, -speed):
        alpha = max(alpha, 0)
        surface.blit(nextImg, (0, 0))
        fade_surface.set_alpha(alpha)
        surface.blit(fade_surface, (0, 0))
        pygame.display.update()
        clock.tick(60)

    surface.blit(nextImg, (0, 0))
    pygame.display.update()
