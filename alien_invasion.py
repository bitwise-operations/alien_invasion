import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_functions import check_events, update_screen, update_bullets


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai = Settings()
    screen = pygame.display.set_mode((ai.screen_width,
                                      ai.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание корабля.
    ship = Ship(ai, screen)
    # Создание группы для хранения пуль.
    bullets = Group()
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        check_events(ship, ai, screen, bullets)
        # Обновление корабля
        ship.update()
        # Обновление пули
        bullets.update()
        # Удаление пуль, вышедших за край экрана.
        update_bullets(bullets)
        # При каждом проходе цикла перерисовывается экран.
        update_screen(ai, screen, ship, bullets)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

run_game()
