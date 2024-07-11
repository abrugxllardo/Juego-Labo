import pygame
from settings import *
from bloques import *
from pygame.locals import *

pygame.init()
#cargo imagenes
personaje_r = pygame.image.load(r".\src\assets\0.png")
personaje_l = pygame.transform.flip(personaje_r, True, False)

fondo_nivel = pygame.image.load(r".\src\assets\fondo_nuevo.jpg")
fondo_nivel = pygame.transform.scale(fondo_nivel, SIZE)

title = pygame.image.load(r".\src\assets\title.jpeg")
title = pygame.transform.scale(title, TITLE_SIZE)
rect_title = title.get_rect(center = TITLE_POS)

game_over_img = pygame.image.load(r".\src\assets\game_over.jpeg")
game_over_img = pygame.transform.scale(game_over_img, GAME_OVER_SIZE)
rect_game_over = game_over_img.get_rect(center = GAME_OVER_POS)

start_button = pygame.image.load(r".\src\assets\startbutton (2).png")
start_button = pygame.transform.scale(start_button, START_BUTTON)
rect_start = start_button.get_rect(center = START_BUTTON_POS)

music_button = pygame.image.load(r".\src\assets\music_boton.png")
music_button = pygame.transform.scale(music_button, (80,80))
rect_music= music_button.get_rect(center = MUSIC_POS)

ranking_button = pygame.image.load(r".\src\assets\ranking.png")
ranking_button = pygame.transform.scale(ranking_button, (90,80))
rect_ranking = ranking_button.get_rect(center = RANKING_POS)

muted = pygame.image.load(r".\src\assets\muted.png")
muted = pygame.transform.scale(ranking_button, (80,80))

score_img = pygame.image.load(r".\src\assets\scores.jpeg")
score_img = pygame.transform.scale(score_img, SCORE_SIZE)
rect_score = score_img.get_rect(center = SCORE_POS_2)

grilla_img = pygame.image.load(r".\src\assets\grilla.jpeg")
grilla_img = pygame.transform.scale(grilla_img, GRILLA_SIZE)
rect_grilla = grilla_img.get_rect(center = GRILLA_POS)

item_vida = pygame.image.load(r".\src\assets\tulip.png")

special_item = pygame.image.load(r".\src\assets\special.png")

proyectil_img = pygame.image.load(r".\src\assets\bullet.jpeg")
proyectil_img = pygame.transform.scale(proyectil_img, (20,10))

vida_img = pygame.image.load(r".\src\assets\heart.png")
vida_img = pygame.transform.scale(vida_img, LIVES_SIZE)

bee_img = pygame.image.load(r".\src\assets\bee.png")

fire_img = pygame.image.load(r".\src\assets\fire.png")
fire_img = pygame.transform.scale(fire_img, (20,30))

salida = pygame.image.load(r".\src\assets\exit.png")
salida = pygame.transform.scale(salida, QUIT_SIZE)
rect_salida = salida.get_rect(center = QUIT_POS)
#cargo sonidos
item_sound = pygame.mixer.Sound(r".\src\assets\item-pick-up-38258.mp3")
pygame.mixer.Sound.set_volume(item_sound, 0.2)

special_item_sound = pygame.mixer.Sound(r".\src\assets\3-up-2-89189.mp3")
pygame.mixer.Sound.set_volume(special_item_sound, 0.2)

win_sound = pygame.mixer.Sound(r".\src\assets\winSonido.mp3")
pygame.mixer.Sound.set_volume(win_sound, 0.2)

game_over_sound = pygame.mixer.Sound(r".\src\assets\sonido_gameOver.mp3")
pygame.mixer.Sound.set_volume(game_over_sound, 0.2)

jump = pygame.mixer.Sound(r".\src\assets\cartoon-jump-6462.mp3")
pygame.mixer.Sound.set_volume(jump, 0.2)

laser = pygame.mixer.Sound(r".\src\assets\laser.mp3")
pygame.mixer.Sound.set_volume(laser, 0.2)

hit = pygame.mixer.Sound(r".\src\assets\ouch-116112.mp3")
pygame.mixer.Sound.set_volume(hit, 0.2)

button_pressed = pygame.mixer.Sound(r".\src\assets\button-pressed-38129.mp3")
pygame.mixer.Sound.set_volume(button_pressed, 0.2)

deco = pygame.image.load(r".\src\assets\arbolDeco1.png")
deco2 = pygame.image.load(r".\src\assets\arbolDeco2.png")
deco3 = pygame.image.load(r".\src\assets\arbolDeco3.png")
arbol_1 = new_platform(deco, 10, 650, 100,200)
arbol_2 = new_platform(deco3, 720, 470, 90,190)
arbol_3 = new_platform(deco2, 350, 150, 80,190)
decoraciones = [arbol_1, arbol_2, arbol_3]

img_start = pygame.image.load(r".\src\assets\platInicio.png")
img_platform1 = pygame.image.load(r".\src\assets\plat1.png")
img_platform2 = pygame.image.load(r".\src\assets\plat2.png")
img_platform3 = pygame.image.load(r".\src\assets\plat3.png")
img_platform4 = pygame.image.load(r".\src\assets\plat4.png")
img_platform5 = pygame.image.load(r".\src\assets\plat5.png")
img_platform6 = pygame.image.load(r".\src\assets\plat6.png")

plat_start = new_platform(img_start, 0, HEIGHT -50, 200, 30)
platform_1 = new_platform(img_platform1, 200, 760, 200,100)
platform_2 = new_platform(img_platform3, 480, 700, 170,100)
platform_3 = new_platform(img_platform4, 710, 660, 90,70)
platform_4 = new_platform(img_platform4, 850, 620, 90,70)
platform_5 = new_platform(img_platform3, 970, 520, 200,90)
platform_6= new_platform(img_platform4, 1070, 390, 70, 50)
platform_7 = new_platform(img_start, 700, 300, 250, 30)
platform_8 = new_platform(img_platform5, 580, 340, 50,40)
platform_9 = new_platform(img_platform5, 470, 340, 50,40)
platform_10 = new_platform(img_platform5, 360, 340, 50,40)
platform_11 = new_platform(img_platform6, 220, 290, 70,120)
platform_12 = new_platform(img_platform4, 100, 190, 90,70)
plataformas = [plat_start, platform_1, platform_2, platform_3, platform_4, platform_5,platform_6, platform_7, platform_8, platform_9, platform_10, platform_11, platform_12]