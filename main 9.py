import pygame
# Ініціалізація бібліотеки pygame
pygame.init()
# Створюємо ігрове вікно
screen = pygame.display.set_mode((400, 300)) # Ширина 400, висота 300
pygame.display.set_caption("ігровий цикл")
# Основний колір фону
background_color = (173, 216, 230) # Світло-блакитний
font = pygame.font.SysFont("Arial", 30) # Створюємо шрифт Arial розміру 30
text = font.render("", True, (0, 0, 0)) # Створюємо зображення тексту чорного кольору
# Ігровий цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Перевірка на натискання закриття вікна
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    text = font.render("up", True, (0, 0, 0)) # Створюємо зображення тексту чорного кольору
                elif event.key == pygame.K_DOWN:
                    text = font.render("down", True, (0, 0, 0)) # Створюємо зображення тексту чорного кольору
                elif event.key == pygame.K_RIGHT:
                    text = font.render("right", True, (0, 0, 0)) # Створюємо зображення тексту чорного кольору
                elif event.key == pygame.K_LEFT:
                    text = font.render("left", True, (0, 0, 0)) # Створюємо зображення тексту чорного кольору
        elif event.type == pygame.KEYUP:
            text = font.render("", True, (0, 0, 0)) # Створюємо зображення тексту чорного кольору

# Оновлюємо екран
        pygame.display.flip()
        screen.fill((255,255,255))
        screen.blit(text, (200, 150))  # Малюємо текст у верхньому лівому куті

# Завершуємо роботу pygame
pygame.quit()
