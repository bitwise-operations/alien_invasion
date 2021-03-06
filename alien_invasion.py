import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_functions import (check_events,
                            update_screen, update_bullets, create_fleet,
                            update_aliens)


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
    # Создание группы пришельцев.
    aliens = Group()
    # Создание флота пришельцев.
    create_fleet(ai, screen, aliens, ship)
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
        # Обновление пришельцев
        update_aliens(aliens, ai)
        # При каждом проходе цикла перерисовывается экран.
        update_screen(ai, screen, ship, aliens, bullets)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

run_game()
