import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown(event, ship, ai_settings, screen, bullets):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        # Переместить корабль вправо.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Переместить корабль влево.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Создание новой пули и включение ее в группу bullets.
        fire_bullet(bullets, ai_settings, screen, ship)
    elif event.key == pygame.K_q:
        # Быстрое завершение игры по нажатию на Q
        sys.exit()

def check_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        # Перестать двигать корабль вправо.
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Перестать двигать корабль влево.
        ship.moving_left = False

def check_events(ship, ai_settings, screen, bullets):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран. 
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

def update_bullets(bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # Обновление позиций пуль.
    bullets.update()
    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(bullets, ai_settings, screen, ship):
    """Выпускает пулю, если максимум еще не достигнут."""
    # Создание новой пули и включение ее в группу bullets.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """Вычисление количества пришельцев в ряду."""
    # Интервал между соседними пришельцами равен ширине 0.3 пришельца.
    available_space_x = ai_settings.screen_width - alien_width
    return int(available_space_x / (1.3 * alien_width))

def create_alien(ai_settings, screen, aliens, alien_number):
    """Создание пришельца и размещение его в ряду."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width / 2 + 1.3 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление количества пришельцев в ряду.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # Создание первого ряда пришельцев.
    for alien_number in range(number_aliens_x):
        # Создание пришельца и размещение его в ряду.
        create_alien(ai_settings, screen, aliens, alien_number)
