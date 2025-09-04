import random as r
import pygame
# Ініціалізація бібліотеки pygame
pygame.init()
# Створюємо ігрове вікно
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Ширина 400, висота 300
pygame.display.set_caption("Ярослав")
color = {"red": (255, 0, 0),
         "green": (0, 255, 0),
         "blue": (0, 0, 255),
         "yellow": (255, 255, 0),
         "white": (255, 255, 255)
         }
color_list = ["red", "green", "blue","yellow", "white"]
# Основний колір фону
background_color = (0,0,0)
# Ігровий цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Перевірка на натискання закриття вікна
            running = False
        if event.type == pygame.KEYDOWN: # Перевірка на натискання клавіші
            if event.key == pygame.K_RETURN:
                screen.fill(color[r.choice(color_list)])
            else:
# Очищуємо екран заданим кольором
                screen.fill(background_color)
# Оновлюємо екран
    pygame.display.flip()
# Завершуємо роботу pygame
pygame.quit()
