import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Кольори
GREY = (125, 125, 125)
GREEN = (0, 163, 108)

# Завантаження зображення кота та фону
cat_img = pygame.image.load("дино.png").convert_alpha()
cat_img = pygame.transform.smoothscale(cat_img, (100, 100))
cat = cat_img.get_rect()
cat.topleft = (100, 100)

# Завантаження фону
background_img = pygame.image.load("unnamed (3).png").convert()
background_img = pygame.transform.scale(background_img, (800, 600))

# Параметри швидкості
speed = 0
gravity = 0.5
jump_speed = -8

# Основний цикл
running = True
while running:
    # --- обробка подій ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed = jump_speed

    # --- логіка руху ---
    speed += gravity
    cat.y += speed

    if cat.y > 500:  # земля
        cat.y = 500
        speed = 0

    # --- малювання ---
    screen.blit(background_img, (0, 0))
    screen.blit(cat_img, cat.topleft)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
