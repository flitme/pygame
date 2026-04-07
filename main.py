import pygame
import time

MAIN_BG = (255, 0, 0)


if __name__ == '__main__':
    pygame.display.init()
    pygame.font.init()
    pygame.mouse.set_visible(False)
    # Get size of screen and create main rendering surface.
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    # Display splash screen.
    screen.fill(MAIN_BG)
    pygame.display.update()
    time.sleep(10.0)