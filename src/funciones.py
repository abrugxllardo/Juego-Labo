from random import randint, randrange, choice
import pygame
from settings import *
from ranking import show_ranking
from resources import *

def punto_en_rect(punto, rect) -> bool:
    x, y = punto
    if x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom:
        return True
    else:
        return False

def detectar_colision(rect_1, rect_2) ->bool:
    if punto_en_rect(rect_1.topleft, rect_2) or \
        punto_en_rect(rect_1.topright, rect_2) or\
        punto_en_rect(rect_1.bottomleft, rect_2)or\
        punto_en_rect(rect_1.bottomright, rect_2) or\
        punto_en_rect(rect_2.topleft, rect_1) or \
        punto_en_rect(rect_2.topright, rect_1) or\
        punto_en_rect(rect_2.bottomleft, rect_1)or\
        punto_en_rect(rect_2.bottomright, rect_1):
        return True
    else:
        return False

def distancia_puntos(punto_1:tuple[int, int], punto_2:tuple[int, int])->float:
    ca = punto_1[0] - punto_2[0]
    co = punto_1[1] - punto_2[1]

    distancia = (ca ** 2 + co ** 2) ** 0.5
    return distancia

def colision_circulos(rect_1 , rect_2)->bool:
    r1 = rect_1.width // 2
    r2 =rect_2.width // 2 
    distancia = distancia_puntos(rect_1.center, rect_2.center)
    return distancia <= r1 + r2

def mostrar_texto(superficie: pygame.Surface, texto:str, fuente: pygame.font.Font, pos:tuple[int,int], color: tuple[int, int,int], color_fondo:tuple[int, int,int]= None) :
    sup_texto = fuente.render(texto, True, color, color_fondo) 
    rect_texto = sup_texto.get_rect(center = pos)
    superficie.blit(sup_texto, rect_texto)
    pygame.display.flip()

def wait_user(key):
    continuar = True
    while continuar:
        eventos = pygame.event.get()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    continuar = False

def wait_user_click(screen, playing_music, rect:pygame.Rect = None, rect2:pygame.Rect = None, rect3:pygame.Rect = None, rect4:pygame.Rect = None):
    continuar = True
    while continuar:
        eventos = pygame.event.get()
        for event in eventos:
            if event.type == pygame.QUIT:
                salir_programa()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_pos = event.pos
                    if punto_en_rect(click_pos, rect):
                        pygame.mixer.music.stop()
                        button_pressed.play(0)
                        continuar = False
                    elif punto_en_rect(click_pos, rect2):
                        salir_programa()
                    elif punto_en_rect(click_pos, rect3):
                        button_pressed.play(0)
                        show_ranking(screen)
                    elif punto_en_rect(click_pos, rect4):
                        if playing_music:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                        playing_music = not playing_music

def salir_programa():
    pygame.quit()
    exit()
