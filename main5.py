import pygame
# Ініціалізація pygame
pygame.init()
# Встановлення розміру вікна
screen = pygame.display.set_mode((800, 600))
# Створення об'єкта: прямокутник
rect_position = pygame.math.Vector2(0, 0)
rect_position2 = pygame.math.Vector2(0, 300)# Початкова позиція
screen.fill((255, 255, 255))
# Основний цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # Перевірка на натискання клавіші
            if event.key == pygame.K_RETURN:  # Якщо натиснута клавіша Enter
                for i in range(255):# Малюємо прямокутники
                    pygame.draw.rect(screen, (0, 0, 255), (rect_position.x, rect_position.y, 50, 300))
                    pygame.draw.rect(screen, (255, 255, 0), (rect_position2.x, rect_position2.y, 50, 300))
                    rect_position += pygame.math.Vector2(5, 0)
                    rect_position2 += pygame.math.Vector2(5, 0)
    # Очищуємо екран
        #screen.fill((255, 255, 255))

    # Оновлення екрана
        pygame.display.flip()
pygame.quit()