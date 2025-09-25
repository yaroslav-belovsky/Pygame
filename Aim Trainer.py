import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Налаштування екрана
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")
font = pygame.font.SysFont("Arial", 30) # Створюємо шрифт Arial розміру 30
score_text = font.render("влучань: 0", True, (0, 0, 0)) # Створюємо зображення тексту чорного кольору
font = pygame.font.SysFont("Arial", 30) # Створюємо шрифт Arial розміру 30
score_p_text = font.render("промахів: 0", True, (0, 0, 0)) # Створюємо зображення тексту чорного кольору
dabl_text = font.render("", True, (0, 0, 0))

promahiv = 0
dabl = 0
score = 0

# Кольори
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
color = "RED"

# Початкові координати фігури
x, y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
RADIUS = 30

# Змінні для таймера
last_move_time = 0
MOVE_INTERVAL = 1000 # Інтервал у мілісекундах


# Основний цикл гри
running = True
start_time = pygame.time.get_ticks()

def generator():
    return (random.randint(1, 450), random.randint(1, 450))

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #print(f"{mouse_x=} {mouse_y=}")
            distance = ((mouse_x - x) ** 2 + (mouse_y - y) ** 2) ** 0.5
            if distance <= RADIUS:
                print("ти влучив!")
                if color == "GREEN":
                    score += 2 * dabl
                    dabl += 1
                    dabl_text = font.render(f"{dabl}", True, (0, 0, 0))
                else:
                    score += 1
                    dabl = 0
                color = "GREEN"
                score_text = font.render(f"влучань: {score}", True, (0, 0, 0))
                x, y = (random.randint(50, WIDTH - 50),
                        random.randint(50, HEIGHT - 50))
                last_move_time = current_time
                # Створюємо зображення тексту чорного кольору
            else:
                print("ти не влучив!")
                color = "RED"
                dabl = 0
                promahiv += 1
                score_p_text = font.render(f"промахів: {promahiv}", True, (0, 0, 0))
                # Створюємо зображення тексту чорного кольору


# Записуємо в змінну поточний час
    current_time = pygame.time.get_ticks()

# Переміщуємо фігуру у випадкове місце щосекунди
    if current_time - last_move_time >= MOVE_INTERVAL - dabl * 10:
        color = "RED"
        dabl = 0


        x, y = (random.randint(50, WIDTH - 50),
                random.randint(50, HEIGHT - 50))
        last_move_time = current_time
    elapsed_time = (current_time - start_time) // 1000  # Рахуємо, скільки секунд гри минуло
    time_text = font.render(f"Час: {elapsed_time} с", True, (0, 0, 0))  # Перетворюємо текст на картинку


    # Очищаємо екран і малюємо нову фігурку
    screen.fill(WHITE)
    screen.fill((146, 101, 0))
    radius = 30
    pygame.draw.rect(screen, (255, 130, 0), (0, 0, 400, 100), border_radius=radius)
    if color == "GREEN":
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 500, 500))
        pygame.draw.rect(screen, (255, 250, 250), (50, 50, 400, 400), 50)
        pygame.draw.rect(screen, (255, 250, 250), (125, 125, 250, 250), 50)
        pygame.draw.rect(screen, (255, 250, 250), (200, 200, 100, 100), 25)
        pygame.draw.rect(screen, (255, 250, 250), (235, 235, 30, 30), 10)
        pygame.draw.rect(screen, (255, 250, 250), (235, 235, 30, 30), 10)
        pygame.draw.rect(screen, (255, 130, 0), (200, 450, 100, 40))
        screen.blit(dabl_text, (250, 450))  # Малюємо текст у верхньому лівому куті
    cord = generator()
    pygame.draw.rect(screen, (255, 0, 0), (cord[0],cord[1],cord[0],cord[1]))
    pygame.draw.circle(screen, color, (x, y), RADIUS)
    pygame.draw.circle(screen, (255,255,255), (x, y), 15, 10)
    screen.blit(score_text, (10, 10))  # Малюємо текст у верхньому лівому куті
    screen.blit(score_p_text, (200, 10))  # Малюємо текст у верхньому лівому куті
    screen.blit(time_text, (10, 40))  # Відображаємо створену картинку на
    pygame.display.flip() # Оновлюємо екран


pygame.quit()