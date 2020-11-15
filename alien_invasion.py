import sys
import pygame

from settings import Settings
from ship import Ship
from game_functions import check_events, update_screen


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai = Settings()
    screen = pygame.display.set_mode((ai.screen_width,
                                      ai.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание корабля.
    ship = Ship(screen)

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        check_events(ship)
        ship.update()
        # При каждом проходе цикла перерисовывается экран.
        update_screen(ai, screen, ship)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

run_game()
