import pygame
# Ініціалізація бібліотеки pygame
pygame.init()
# Створюємо ігрове вікно
screen = pygame.display.set_mode((400, 300)) # Ширина 400, висота 300
pygame.display.set_caption("Мій перший ігровий цикл")
# Основний колір фону
background_color = (173, 216, 230) # Світло-блакитний
# Ігровий цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Перевірка на натискання закриття вікна
            running = False
        if event.type == pygame.KEYDOWN: # Перевірка на натискання клавіші
            if event.key == pygame.K_RETURN:
                print("Helo!!!!!!!!!!!!!!!!!!!")# Якщо натиснута клавіша Enter
                screen.fill((100, 0, 0))
            elif event.key == pygame.K_w:
                screen.fill((173, 216, 230))
            else:
# Очищуємо екран заданим кольором
                screen.fill(background_color)
# Оновлюємо екран
        pygame.display.flip()
# Завершуємо роботу pygame
pygame.quit()
