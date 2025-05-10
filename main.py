import pygame
import random
import os

# Инициализация Pygame
pygame.init()

# Параметры окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Проверка изображений
if not os.path.exists("img/icon.jpg") or not os.path.exists("img/target.png"):
    print("Ошибка: необходимые файлы отсутствуют!")
    exit()

# Установка иконки
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

# Загрузка и масштабирование мишени
target_width = 80
target_height = 80
target_img = pygame.image.load("img/target.png")
target_img = pygame.transform.scale(target_img, (target_width, target_height))

# Начальные параметры
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
score = 0
running = True
clock = pygame.time.Clock()

# Функции
def draw_screen():
    screen.fill(color)
    screen.blit(target_img, (target_x, target_y))
    # Отображение счёта
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

def process_events():
    global running, target_x, target_y, color, score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                score += 1

# Игровой цикл
while running:
    process_events()
    draw_screen()
    clock.tick(60)

pygame.quit()