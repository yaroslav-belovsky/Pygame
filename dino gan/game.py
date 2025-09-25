import random
import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))

pygame.mixer.init()



pygame.mixer.music.load('musik/background.mp3')
pygame.mixer.music.set_volume(0.3)  # 50% гучність

pygame.mixer.music.play(-1)  # -1 означає безкінечне повторення
shoot_sound = pygame.mixer.Sound('musik/shoot.mp3')
# Налаштування гучності звукових ефектів
shoot_sound.set_volume(0.7)

pygame.mixer.music.play(-1)  # -1 означає безкінечне повторення
boom = pygame.mixer.Sound('musik/explosion-with-fire-flame.mp3')
# Налаштування гучності звукових ефектів
boom.set_volume(0.3)

pygame.mixer.music.play(-1)  # -1 означає безкінечне повторення
dron_atak = pygame.mixer.Sound('musik/05-weaponry-extraterrestrial-railgun-static-firing-343782.mp3')
# Налаштування гучності звукових ефектів
dron_atak.set_volume(0.7)

pygame.mixer.music.play(-1)  # -1 означає безкінечне повторення
game_ower = pygame.mixer.Sound('musik/game-over-deep-male-voice-clip-352695.mp3')
# Налаштування гучності звукових ефектів
game_ower.set_volume(0.7)

font = pygame.font.SysFont("Arial", 30) # Створюємо шрифт Arial розміру 30
score_text = font.render("рахунок: 0", True, (0, 0, 0)) # Створюємо зображення тексту чорного кольору

speed_down = 0
gravity = 2.5
jump_speed = -40
obstacles = []
obstacle_timer = 0
last_clock = 0
time = pygame.time.get_ticks()
dron_moow = True
last_dron = 0
deley = 1000
last_dron_wustril = 0
perhui = True
speed = 60

dino_img = pygame.image.load("imig.png").convert_alpha()
dino_img = pygame.transform.smoothscale(dino_img, (100, 100))
dino = dino_img.get_rect()
dino.topleft = (100, 100)

Boom_img = pygame.image.load("e3705e91-90b2-4c4c-813f-90dde4a24a27.png").convert_alpha()
Boom_img = pygame.transform.smoothscale(Boom_img, (100, 100))
Boom = Boom_img.get_rect()
Boom.topleft = (800, 100)

dron_img = pygame.image.load("dron.png").convert_alpha()
dron_img = pygame.transform.smoothscale(dron_img, (100, 100))
dron = dron_img.get_rect()
dron.topleft = (800, 0)

background_img = pygame.image.load("Gemini_Generated_Image_qd7cwfqd7cwfqd7c.png").convert()
background_img = pygame.transform.scale(background_img, (800, 600))
randing = True

score = 0

def pereshkoda():
    global last_clock, obstacle_timer, speed_down, score, deley, speed, clock
    last_clock += 10000
    x = 800
    y = 500
    for i in range(100):
        boom.play()

        x -= 10
        pygame.display.update()
        time = pygame.time.get_ticks()
        speed_down += gravity
        dino.y += speed_down
        dino.y = max(0, min(dino.y, 600 - 100))
        screen.blit(background_img, (0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (x, y, x - 50, y + 100))
        screen.blit(dino_img, dino.topleft)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if dino.y <= 400:
                    pass
                else:
                    speed_down = jump_speed
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                shoot_sound.play()
                Boom.x, Boom.y = event.pos
                screen.blit(Boom_img, Boom.topleft)
                clock.tick(1000)
            else:
                Boom.x, Boom.y = -100, -100
        obstacle_timer += 1

        if x >= dino.x and x <= dino.x and y <= dino.y:
            print("Game Over!")

            with open("record", "r") as record:
                my_record = record.read()
                if int(my_record) < score:
                    with open("record", "w") as zapus:
                        score_text = font.render(f"рахунок: {score}",
                                                 True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                        score_text2 = font.render(f"ти побив рекорд!",
                                                  True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                        score_text3 = font.render(f"попередній рекорд: {my_record}",
                                                  True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                        zapus.write(str(score))
                else:
                    with open("record", "r") as record:
                        my_record = record.read()
                    score_text = font.render(f"рахунок: {score}",
                                             True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                    score_text2 = font.render(f"ти не побив рекорд...",
                                             True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                    score_text3 = font.render(f"попередній рекорд: {my_record}",
                                             True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
            pygame.draw.rect(screen, (255, 130, 0), (100, 100, 600, 400))
            screen.blit(score_text, (300, 200))
            screen.blit(score_text2, (300, 250))
            screen.blit(score_text3, (300, 300))
            pygame.display.flip()  # Оновлюємо екран
            game_ower.play()
            clock.tick(0.1)
            pygame.quit()
            exit()
        if dino.colliderect(Boom):
            print("Game Over!")

            with open("record", "r") as record:
                my_record = record.read()
                if int(my_record) < score:
                    with open("record", "w") as zapus:
                        score_text = font.render(f"рахунок: {score}",
                                                 True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                        score_text2 = font.render(f"ти побив рекорд!",
                                                  True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                        score_text3 = font.render(f"попередній рекорд: {my_record}",
                                                  True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                        zapus.write(str(score))
                else:
                    with open("record", "r") as record:
                        my_record = record.read()
                    score_text = font.render(f"рахунок: {score}",
                                             True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                    score_text2 = font.render(f"ти не побив рекорд...",
                                              True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                    score_text3 = font.render(f"попередній рекорд: {my_record}",
                                              True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
            pygame.draw.rect(screen, (255, 130, 0), (100, 100, 600, 400))
            screen.blit(score_text, (300, 200))
            screen.blit(score_text2, (300, 250))
            screen.blit(score_text3, (300, 300))
            pygame.display.flip()  # Оновлюємо екран
            game_ower.play()
            clock.tick(0.1)
            pygame.quit()
            exit()
        if dron.colliderect(Boom):
            dron_moow = False
        screen.blit(dino_img, dino.topleft)

        score_text = font.render(f"рахунок: {score}", True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
        screen.blit(score_text, (10, 10))
        pygame.display.flip()  # Оновлюємо екран
        pygame.display.update()
        clock.tick(speed)
    deley -=  10
    score += 1
    speed += 1


def Dron():
    dron_naw = True
    global speed_down, last_dron_wustril, time, perhui, cord_w_x, cord_w_y, deley, score_text, score, speed, clock
    step = 0
    while dron_naw:
        time = pygame.time.get_ticks()
        speed_down += gravity
        dino.y += speed_down
        dino.y = max(0, min(dino.y, 600 - 100))
        dron.y = max(0, min(dron.y, 500 - 100))
        dron.x = max(200, min(dron.x, 500 - 100))
        if step <= 0:
            delta_x = random.randint(-5, 5)
            delta_y = random.randint(-5, 5)
            step = 120

        dron.x += delta_x
        dron.y += delta_y
        step -= 1
        # dron.x = random.randint(dron.x - 10, dron.x + 10)
        # dron.y = random.randint(dron.y - 10, dron.y + 10)
        screen.blit(background_img, (0, 0))
        screen.blit(dino_img, dino.topleft)
        screen.blit(dron_img, dron.topleft)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if dino.y <= 400:
                    pass
                else:
                    speed_down = jump_speed
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                shoot_sound.play()
                Boom.x, Boom.y = event.pos
                screen.blit(Boom_img, Boom.topleft)
                clock.tick(1000)
            else:
                Boom.x, Boom.y = -100, 800
        if time - last_dron_wustril >= 5000:
            dron_atak.play()
            if perhui:
                cord_w_x, cord_w_y = dino.x+50, dino.y+50
            perhui = False
            pygame.draw.circle(screen, (255, 0, 0), (cord_w_x, cord_w_y), 50)
        if time - last_dron_wustril >= 10000:
            Boom.x, Boom.y = cord_w_x-50, cord_w_y-50
            screen.blit(Boom_img, Boom.topleft)
            screen.blit(background_img, (0, 0))
            last_dron_wustril += 10000
            perhui = True





        if dino.colliderect(Boom):
            print("Game Over!")

            with open("record", "r") as record:
                my_record = record.read()
                if int(my_record) < score:
                    with open("record", "w") as zapus:
                        score_text = font.render(f"рахунок: {score}",
                                                 True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                        score_text2 = font.render(f"ти побив рекорд!",
                                                  True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                        score_text3 = font.render(f"попередній рекорд: {my_record}",
                                                  True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                        zapus.write(str(score))
                else:
                    with open("record", "r") as record:
                        my_record = record.read()
                    score_text = font.render(f"рахунок: {score}",
                                             True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                    score_text2 = font.render(f"ти не побив рекорд...",
                                              True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                    score_text3 = font.render(f"попередній рекорд: {my_record}",
                                              True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
            pygame.draw.rect(screen, (255, 130, 0), (100, 100, 600, 400))
            screen.blit(score_text, (300, 200))
            screen.blit(score_text2, (300, 250))
            screen.blit(score_text3, (300, 300))
            pygame.display.flip()  # Оновлюємо екран
            game_ower.play()
            clock.tick(0.1)
            pygame.quit()
            exit()
        if dron.colliderect(Boom):
            dron_naw = False
        screen.blit(dino_img, dino.topleft)
        score_text = font.render(f"рахунок: {score}", True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
        screen.blit(score_text, (10, 10))
        pygame.display.flip()  # Оновлюємо екран
        pygame.display.update()
        clock.tick(speed)
    deley -= 10
    score += 1
    speed += 1


while randing:
    time = pygame.time.get_ticks()
    speed_down += gravity
    dino.y += speed_down
    dino.y = max(0, min(dino.y, 600 - 100))
    dron_atak.stop()

    screen.blit(background_img, (0, 0))
    screen.blit(dino_img, dino.topleft)
    score_text = font.render(f"рахунок: {score}", True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            randing = False


        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if dino.y <= 400:
                pass
            else:
                speed_down = jump_speed
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            shoot_sound.play()
            Boom.x, Boom.y = event.pos
            screen.blit(Boom_img, Boom.topleft)
            clock.tick(1000)
        else:
            Boom.x, Boom.y = -100, -100
    obstacle_timer += 1
    if time - last_clock > deley:
        wubir = ["pereshcoda"], ["dron"]
        random_wariant = random.choice(wubir)
        if random_wariant == ["pereshcoda"]:
            pereshkoda()
        elif random_wariant == ["dron"]:
            last_dron_wustril = time
            Dron()
    if dino.colliderect(Boom):
        print("Game Over!")

        with open("record", "r") as record:

            with open("record", "r") as record:
                my_record = record.read()
                if int(my_record) < score:
                    with open("record", "w") as zapus:
                        score_text = font.render(f"рахунок: {score}",
                                                 True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                        score_text2 = font.render(f"ти побив рекорд!",
                                                  True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                        score_text3 = font.render(f"попередній рекорд: {my_record}",
                                                  True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                        zapus.write(str(score))
                else:
                    with open("record", "r") as record:
                        my_record = record.read()
                    score_text = font.render(f"рахунок: {score}",
                                             True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                    score_text2 = font.render(f"ти не побив рекорд...",
                                              True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
                    score_text3 = font.render(f"попередній рекорд: {my_record}",
                                              True, (0, 0, 0))  # Створюємо зображення тексту чорного кольору
            pygame.draw.rect(screen, (255, 130, 0), (100, 100, 600, 400))
            screen.blit(score_text, (300, 200))
            screen.blit(score_text2, (300, 250))
            screen.blit(score_text3, (300, 300))
            pygame.display.flip()  # Оновлюємо екран
            game_ower.play()
            clock.tick(0.1)
            pygame.quit()
            exit()
    if dron.colliderect(Boom):
        dron_naw = False
    screen.blit(dino_img, dino.topleft)
    pygame.display.flip()
    screen.blit(score_text, (10, 10))  # Оновлюємо екран
    pygame.display.update()

    clock.tick(speed)
