import pygame
import sys
from settings import PINK, BACKGROUNDCOLOR, CENTER_X
from resources import salida, rect_salida, score_img, rect_score, grilla_img, rect_grilla
import csv

def show_ranking(screen):
    try:
        with open('scores.csv', 'r') as file:
            reader = csv.reader(file)
            scores = [row for row in reader]
    except FileNotFoundError:
        scores = []

    is_running = True

    while is_running:
        screen.fill(BACKGROUNDCOLOR)
        screen.blit(salida, rect_salida)
        screen.blit(score_img, rect_score)
        screen.blit(grilla_img, rect_grilla)

        fuente = pygame.font.SysFont("Constantia", 20)
        distancia_y = 240

        for score in scores:
            score_text = fuente.render(f"{score[0]}", True, PINK)
            rect_scores = score_text.get_rect(center=(CENTER_X, distancia_y))
            screen.blit(score_text, rect_scores)
            distancia_y += 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_pos = event.pos
                    if click_pos[0] >= rect_salida.left and click_pos[0] <= rect_salida.right and click_pos[1] >= rect_salida.top and click_pos[1] <= rect_salida.bottom:
                        is_running = False
                        pygame.display.flip()
        pygame.display.flip()
 

