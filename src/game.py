from resources import *
from settings import * 
from funciones import *
from bloques import *
from pygame.locals import *
from sys import exit
from random import choice
from game_over import *

def dibujar_pantalla(screen, proyectiles, proyectil_speed, player, bees, items, health, special_items,fire, score, fuente, playing_music):
    screen.fill(BACKGROUNDCOLOR)
    for decoration in decoraciones:
        screen.blit(decoration["img"], decoration["rect"])
    for platform in plataformas:
        screen.blit(platform["img"], platform["rect"])

    for proyectil in proyectiles[:]:
        proyectil["rect"].x += proyectil_speed * proyectil["direct"]
        screen.blit(proyectil_img, proyectil["rect"])

        if proyectil["rect"].x < 0 or proyectil["rect"].x > WIDTH:
            proyectiles.remove(proyectil)

    screen.blit(player["img"], player["rect"])

    for bee in bees:
        screen.blit(bee["img"], bee["rect"])

    for item in items:
        screen.blit(item["img"], item["rect"])

    for hongo in special_items:
        screen.blit(hongo["img"], hongo["rect"])

    for heart in health:
        screen.blit(heart["img"], heart["rect"])


    screen.blit(fire["img"], fire["rect"])

    mostrar_texto(screen, f"Score: {score}", fuente, SCORE_POS, PINK)

    if not playing_music:
        mostrar_texto(screen, "MUTE", fuente, MUTE_POS, PINK)

def game_loop():
    clock = pygame.time.Clock()

    #config
    pygame.display.set_caption("Primer juego")
    SCREEN = pygame.display.set_mode(SIZE)

    fuente = pygame.font.SysFont("Constantia", 20)

    player = new_block(personaje_r,
                    50, 
                    785,
                    rect_w, 
                    rect_h)
    bees = []
    load_bee_list(bees, CANT_BEES,bee_img)

    items = []
    load_item_list(items, 0, item_vida)

    special_items = []
    load_item_list(special_items, 0, special_item)

    fire = new_block(fire_img, randrange(50, WIDTH-50), 0, 20,20)

    vidas = 3

    health = []
    for i in range(vidas):
        heart_x = LIVES_POS[0] + i * (LIVES_SIZE[0] + LIVES_SPACE)
        heart_y = LIVES_POS[1]
        heart = new_block(vida_img, heart_x, heart_y, *LIVES_SIZE)
        health.append(heart)

    proyectiles = []
    proyectil_speed = 10
    direc_bullet = 1

    pygame.mixer.music.load(r".\src\assets\game-music-loop-7-145285.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    playing_music = True

    jumping = False
    desplazamiento_y = 0
    potencia_salto = -26
    limite_velocidad_salto = 26
    gravedad = 2.1

    score = 0
    max_score = 0

    TIMERITEM = USEREVENT + 1
    GAME_TIME_OUT = USEREVENT + 2
    SPECIALITEM = USEREVENT + 3
    INVULNERABLE_TIME_OUT = USEREVENT + 4

    invulnerable = False

    pygame.time.set_timer(TIMERITEM, 15000, -1)
    pygame.time.set_timer(GAME_TIME_OUT, 45000, -1)
    pygame.time.set_timer(SPECIALITEM, 10000, -1)

    move_left = False
    move_right = False

    is_running = True
    while is_running:

        clock.tick(FPS)
        eventos = pygame.event.get()
        for event in eventos:
            if event.type == pygame.QUIT:
                salir_programa()
            if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    move_left = True
                    move_right = False
                    direc_bullet = -1
                if event.key == K_d:
                    move_right = True
                    move_left = False
                    direc_bullet = 1
                if event.key == K_SPACE:
                    if not jumping:
                        jumping = True
                        desplazamiento_y = potencia_salto
                        jump.play()
                if event.key == K_e:
                    proyectil = new_block(proyectil_img, player["rect"].centerx, player["rect"].centery + 15, 10,10, direc= direc_bullet)
                    proyectiles.append(proyectil)
                    laser.play(0)
                if event.key == K_m:
                    if playing_music:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    playing_music = not playing_music

                if event.key == K_p:
                    pygame.mixer.music.pause()
                    mostrar_texto(SCREEN, "PAUSE", fuente, CENTER, PINK)
                    wait_user(K_p)
                    if playing_music:
                        pygame.mixer.music.unpause()

            if event.type == pygame.KEYUP:
                if event.key == K_a:
                    move_left = False
                if event.key == K_d:
                    move_right = False

            if event.type == GAME_TIME_OUT:
                is_running = False 

            if event.type == TIMERITEM:
                if vidas < 3:
                    tulip = new_item(item_vida)
                    platforma = choice(plataformas)
                    tulip["rect"].bottom = platforma["rect"].top
                    tulip["rect"].x = platforma["rect"].x
                    items.append(tulip)

            if event.type == SPECIALITEM:
                fungus = new_item(special_item)
                platforma = choice(plataformas)
                fungus["rect"].bottom = platforma["rect"].top
                fungus["rect"].x = platforma["rect"].x + 30
                special_items.append(fungus)

            if event.type == INVULNERABLE_TIME_OUT:
                invulnerable = False

        if move_left and player["rect"].left > 0:
            if player["rect"].left - SPEED <= 0:
                player["rect"].left = 0
            else:
                player["rect"].left -= SPEED
                player["img"] = personaje_l

        if move_right and player["rect"].right < WIDTH:
            if player["rect"].right >= WIDTH:
                player["rect"].right = WIDTH
            else:    
                player["rect"].right += SPEED
                player["img"] = personaje_r

        if player["rect"].top >= HEIGHT:
            vidas -= 1
            health.pop()
            hit.play(0)
            player = new_block(personaje_r, 50, 785, rect_w, rect_h)
            if vidas == 0:
                is_running= False

        if jumping:
            player["rect"].y += desplazamiento_y
            if desplazamiento_y + gravedad < limite_velocidad_salto:
                desplazamiento_y += gravedad

        for platform in plataformas:
            if player["rect"].colliderect(platform["rect"]):
                if desplazamiento_y > 0: 
                    player["rect"].bottom = platform["rect"].top - 10
                    desplazamiento_y = 0
                    jumping = False
                elif desplazamiento_y < 0: 
                    player["rect"].top = platform["rect"].bottom
                    desplazamiento_y = 0

                if player["rect"].top <= 0:
                    player["rect"].y += gravedad
                    desplazamiento_y = 0

        for platform in plataformas:
            if player["rect"].colliderect(platform["rect"]):
                if player["rect"].right > platform["rect"].left and move_right:
                    player["rect"].right = platform["rect"].left
                elif player["rect"].left < platform["rect"].right and move_left:
                    player["rect"].left = platform["rect"].right

        for bee in bees:
            bee["rect"].move_ip(bee["speed_x"], 0)
            if bee["rect"].left > WIDTH:
                bee["rect"].right = 0

        fire["speed_y"] = randint(min_speed, max_speed)
        fire["rect"].move_ip(0, fire["speed_y"])
        if fire["rect"].top > HEIGHT:
            fire = new_block(fire_img, randrange(50, WIDTH-50), 0, 20,20, speed_y= randint(min_speed, max_speed))

        if colision_circulos(fire["rect"], player["rect"]):
            hit.play(0)
            health.pop()
            fire = new_block(fire_img, randrange(50, WIDTH-50), 0, 20,20)
            vidas = 0
            player = new_block(personaje_r, 50, 785, rect_w, rect_h)
            if vidas == 0:
                is_running= False

        for bee in bees[:]:
            for proyectil in proyectiles[:]:
                if colision_circulos(bee["rect"], proyectil["rect"]):
                    bees.remove(bee)
                    proyectiles.remove(proyectil)
                    score += 1
                    item_sound.play(0)

                    if len(bees) == 0:
                        win_sound.play(0)
                        load_bee_list(bees, CANT_BEES, bee_img)
            if colision_circulos(bee["rect"], player["rect"]):
                if not invulnerable:
                    bees.remove(bee)
                    health.pop()
                    move_left = False
                    move_right = False
                    jumping = False
                    hit.play(0)
                    if vidas > 0:
                        vidas -=1
                        player = new_block(personaje_r, 50, 785, rect_w, rect_h)
                    if vidas == 0:
                        is_running= False
                    if len(bees) == 0:
                        win_sound.play(0)
                        load_bee_list(bees, CANT_BEES, bee_img)
                else:
                    pass

        for hongo in special_items[:]:
            if colision_circulos(hongo["rect"], player["rect"]):
                special_item_sound.play(0)
                special_items.remove(hongo)
                invulnerable = True
                pygame.time.set_timer(INVULNERABLE_TIME_OUT, 5000)

        for item in items:
            if colision_circulos(item["rect"], player["rect"]):
                item_sound.play(0)
                items.remove(item)
                vidas += 1
                health.append(new_block(vida_img, heart_x, heart_y, *LIVES_SIZE))

        dibujar_pantalla(SCREEN, proyectiles, proyectil_speed, player,bees,items,health,special_items,fire, score,fuente,playing_music)

        #actualizo pantalla
        pygame.display.flip() 

    if score > max_score:
        max_score = score

    #pantalla game over
    screen_game_over(SCREEN, score, max_score, game_over_sound, fuente, K_SPACE)

