import pygame
from funciones import *
from resources import *
import sys
import csv

def screen_game_over(screen, score, max_score, sound, fuente, key):
    sound.play(0)
    pygame.mixer.music.stop()
    screen.fill(BACKGROUNDCOLOR)
    mostrar_texto(screen, f"Last score: {score}", fuente, LAST_SCORE, PINK)
    mostrar_texto(screen, f"Max score: {max_score}", fuente, MAX_SCORE, PINK)
    screen.blit(game_over_img, rect_game_over)
    mostrar_texto(screen, "persione SPACE para continuar", fuente, MESSAGE_START, PINK)
    wait_user(K_SPACE)

    with open('scores.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([score])

