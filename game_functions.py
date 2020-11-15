import sys
import pygame


def check_keydown(event, ship):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        # Переместить корабль вправо.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Переместить корабль влево.
        ship.moving_left = True

def check_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        # Перестать двигать корабль вправо.
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Перестать двигать корабль влево.
        ship.moving_left = False

def check_events(ship):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)

def update_screen(ai_settings, screen, ship):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран. 
    screen.fill(ai_settings.bg_color)
    ship.blitme()