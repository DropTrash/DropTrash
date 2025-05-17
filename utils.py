import pygame
import settings


def musicHome():
    pygame.mixer.music.load(settings.MUSIC_NATURE)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)


def musicMike():
    pygame.mixer.music.load(settings.MUSIC_MIKE)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)


def fade_transition(surface, currentImg, nextImg, speed=10):
    fade_surface = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    fade_surface.fill(settings.BLACK)
    for alpha in range(0, 255, speed):
        surface.blit(currentImg, (0, 0))
        fade_surface.set_alpha(alpha)
        surface.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(
            5
        )  
    for alpha in range(255, 0, -speed):
        surface.blit(nextImg, (0, 0))
        fade_surface.set_alpha(alpha)
        surface.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)
    surface.blit(nextImg, (0, 0))
    pygame.display.update()
