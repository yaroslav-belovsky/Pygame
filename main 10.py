import pygame

# Ініціалізація pygame
pygame.init()
# Встановлення розміру вікна
screen = pygame.display.set_mode((800, 600))
# Створення об'єкта: прямокутник
rect_position = pygame.math.Vector2(400, 300)
screen.fill((255, 255, 255))
pygame.draw.rect(screen,
                 (0, 0, 255),
                 (rect_position.x, rect_position.y, 50, 50))
# Основний цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:  # Якщо натиснута клавіша Enter
            rect_position += pygame.math.Vector2(0, -50)
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen,
                                 (0, 0, 255),
                                 (rect_position.x, rect_position.y, 50, 50))
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:  # Якщо натиснута клавіша Enter
            rect_position += pygame.math.Vector2(0, 50)
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen,
                                 (0, 0, 255),
                                 (rect_position.x, rect_position.y, 50, 50))
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]: # Якщо натиснута клавіша Enter
            rect_position += pygame.math.Vector2(-50, 0)
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen,
                                 (0, 0, 255),
                                 (rect_position.x, rect_position.y, 50, 50))
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Якщо натиснута клавіша Enter
            rect_position += pygame.math.Vector2(50, 0)
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen,
                                 (0, 0, 255),
                                 (rect_position.x, rect_position.y, 50, 50))
        if rect_position.x <= -50:
            rect_position += pygame.math.Vector2(50, 0)
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen,
                             (255, 0, 0),
                             (rect_position.x, rect_position.y, 50, 50))
        if rect_position.x >= 800:
            rect_position += pygame.math.Vector2(-50, 0)
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen,
                             (255, 0, 0),
                             (rect_position.x, rect_position.y, 50, 50))
        if rect_position.y <= -50:
            rect_position += pygame.math.Vector2(0, 50)
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen,
                             (255, 0, 0),
                             (rect_position.x, rect_position.y, 50, 50))
        if rect_position.y >= 600:
            rect_position += pygame.math.Vector2(0, -50)
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen,
                             (255, 0, 0),
                             (rect_position.x, rect_position.y, 50, 50))
            #y = x = max(0, min(x, 600 - width))  y = max(0, min(y, 400 - height)

        # Оновлення екрана
        pygame.display.flip()
pygame.quit()

