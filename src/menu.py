from game import game_loop
from settings import *
from funciones import *
from resources import * 
import pygame

pygame.init()

pygame.display.set_caption("Primer juego")
SCREEN = pygame.display.set_mode(SIZE)

fuente = pygame.font.SysFont("Constantia", 20)

def main_menu():
    while True:
        SCREEN.fill(BACKGROUNDCOLOR)
        SCREEN.blit(title, rect_title)
        SCREEN.blit(salida, rect_salida)
        SCREEN.blit(start_button, rect_start)
        SCREEN.blit(ranking_button, rect_ranking)
        SCREEN.blit(music_button, rect_music)
        pygame.display.flip()

        playing_music = True

        if playing_music:
            pygame.mixer.music.load(r".\src\assets\game_menu.mp3")
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)

        wait_user_click(SCREEN, playing_music, rect_start, rect_salida, rect_ranking, rect_music)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        game_loop()

        pygame.display.flip()
    salir_programa()

if __name__ == "__main__":
    main_menu()
