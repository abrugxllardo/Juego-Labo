import pygame
from settings import *
from random import randint, choice

def new_block(imagen = None, rect_x:int = 50, rect_y:int = 50, rect_w:int = 50, rect_h:int = 50, color:tuple = (255,255,255), direc:int = False, borde:int = 0, radio:int = -1, speed_x = 0, speed_y = 0) -> dict:
    player = {}
    player["rect"] = pygame.rect.Rect(rect_x, rect_y, rect_w, rect_h)
    player["color"] = color
    player["direct"] = direc
    player["border"] = borde
    player["radio"] = radio
    player["img"] = imagen
    player["speed_x"] = speed_x
    player["speed_y"] = speed_y

    if imagen:
        imagen = pygame.transform.scale(imagen, (rect_w, rect_h))
    
    return player

def new_bee(imagen = None):
    if imagen:
        imagen = pygame.transform.scale(imagen, (bee_w, bee_h))
    return new_block(imagen, randint(100, WIDTH - 100), randint(200,680), bee_w, bee_h, YELLOW,0, 0, radio = bee_h // 2, speed_x= randint(min_speed, max_speed))

def new_item(imagen = None):
    if imagen:
        imagen = pygame.transform.scale(imagen, (item_w, item_h))
    return new_block(imagen, randint(100, WIDTH - 100), randint(70,700), item_w, item_h, YELLOW, 0, 0, radio = item_h // 2)

def new_platform(imagen: str, rect_x: int = 50, rect_y: int = 50, rect_w: int = 100, rect_h: int = 20) -> dict:
    imagen = pygame.transform.scale(imagen, (rect_w, rect_h))
    return new_block(imagen, rect_x, rect_y, rect_w, rect_h)

def load_bee_list(lista:list, cant:int, imagen = None):
    for _ in range(cant):
        lista.append(new_bee(imagen))

def load_item_list(lista:list, cant:int, imagen = None):
    for _ in range(cant):
        lista.append(new_item(imagen))








