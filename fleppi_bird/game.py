import pygame
import random as r

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Кольори
GREY = (125, 125, 125)
GREEN = (0, 163, 108)

# Завантаження зображення кота та фону
dino_img = pygame.image.load("дино.png").convert_alpha()
dino_img = pygame.transform.smoothscale(dino_img, (100, 100))
dino = dino_img.get_rect()
dino.topleft = (100, 100)

# Завантаження фону
background_img = pygame.image.load("unnamed (3).png").convert()
background_img = pygame.transform.scale(background_img, (800, 600))

font = pygame.font.SysFont("Arial", 30) # Створюємо шрифт Arial розміру 30
score_text = font.render("рахунок: 0", True, (0, 0, 0)) # Створюємо зображення тексту чорного кольору

# Параметри швидкості
speed = 0
gravity = 0.5
jump_speed = -8
hard_cor = False
obstacle_timer = 0 # Таймер для контролю інтервалу часу між перешкодами

obstacles = [] # Список перешкод
obstacle_width = 50 # Ширина перешкоди
gap_height = 225 # Відстань між верхньою та нижньою перешкодами
min_distance = 250 # Мінімальна горизонтальна відстань між перешкодами
score = 0
last_dark_score = 0
# Основний цикл
running = True
while running:
    # --- обробка подій ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            speed = jump_speed

    # --- логіка руху ---
    speed += gravity
    dino.y += speed

    dino.y = max(0, min(dino.y, 600 - 100))

    current_time = pygame.time.get_ticks()



    obstacle_timer += 1

    # Додамо нову перешкоду тільки коли пройде достатньо часу:

    if obstacle_timer > min_distance:

        top_obstacle_height = r.randint(100, 400)  # Випадкова висота верхньої перешкоди

        bottom_obstacle_height = screen.get_height() - top_obstacle_height - gap_height  # Рахуємо висоту нижньої перешкоди

        top_obstacle = pygame.Rect(800, 0, obstacle_width, top_obstacle_height)

        bottom_obstacle = pygame.Rect(800, screen.get_height() - bottom_obstacle_height, obstacle_width,
                                  bottom_obstacle_height)

        obstacles.append((top_obstacle, bottom_obstacle))

        obstacle_timer = 0

    # Далі переміщаємо перешкоди та перевіряємо на зіткнення:
    for top_obstacle, bottom_obstacle in obstacles:

        top_obstacle.x -= 5  # Переміщаємо перешкоду трохи вліво

        bottom_obstacle.x -= 5  # Переміщаємо нижню перешкоду трохи вліво

    # Перевірка на зіткнення з перешкодою
        if dino.colliderect(top_obstacle) or dino.colliderect(bottom_obstacle):

            print("Game Over!")
            pygame.quit()
            exit()

        if top_obstacle.x < -obstacle_width:  # Видаляємо перешкоду, якщо вона вийшла за межі екрану

            obstacles.remove((top_obstacle, bottom_obstacle))
            score += 1
            score_text = font.render(f"рахунок: {score}", True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору


    # Лишилося відмалювати самі перешкоди:


      # --- малювання ---
    screen.blit(background_img, (0, 0))
    screen.blit(dino_img, dino.topleft)

    if score - last_dark_score >= 5 and score - last_dark_score <= 10:
        pygame.draw.rect(screen, (0, 0, 0), (0,0, 800, 600))
        hard_cor = True
        if score - last_dark_score == 9:
            last_dark_score += 10
    else:
        hard_cor = False


    for top_obstacle, bottom_obstacle in obstacles:
        if hard_cor:
            pygame.draw.rect(screen, (10 , 10, 10), top_obstacle)  # Верхня перешкода
            pygame.draw.rect(screen, (10, 10, 10), bottom_obstacle)  # Нижня перешкода
        elif hard_cor == False:
            pygame.draw.rect(screen, GREEN, top_obstacle)  # Верхня перешкода
            pygame.draw.rect(screen, GREEN, bottom_obstacle)  # Нижня перешкода
    screen.blit(score_text, (10, 10))  # Малюємо текст у верхньому лівому куті
    screen.blit(dino_img, dino.topleft)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
