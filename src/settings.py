import pygame
import json
from random import randint


with open('settings.json', 'r') as a:
    settings = json.load(a)


WIDTH = settings["WIDTH"]
HEIGHT = settings["HEIGHT"]
SIZE = tuple(settings["SIZE"])
CENTER = tuple(settings["CENTER"])
CENTER_X = settings["CENTER_X"]
ORIGIN_SCREEN = tuple(settings["ORIGIN_SCREEN"])
SCORE_POS = tuple(settings["SCORE_POS"])
LAST_SCORE = tuple(settings["LAST_SCORE"])
MAX_SCORE = tuple(settings["MAX_SCORE"])
MUTE_POS = tuple(settings["MUTE_POS"])
MESSAGE_START = tuple(settings["MESSAGE_START"])
START_BUTTON = tuple(settings["START_BUTTON"])
START_BUTTON_POS = tuple(settings["START_BUTTON_POS"])
RANKING_POS = tuple(settings["RANKING_POS"])
MUSIC_POS = tuple(settings["MUSIC_POS"])
SCORE_POS_2 = tuple(settings["SCORE_POS_2"])
SCORE_SIZE = tuple(settings["SCORE_SIZE"])
GRILLA_SIZE = tuple(settings["GRILLA_SIZE"])
GRILLA_POS = tuple(settings["GRILLA_POS"])
QUIT_SIZE = tuple(settings["QUIT_SIZE"])
QUIT_POS = tuple(settings["QUIT_POS"])
TITLE_SIZE = tuple(settings["TITLE_SIZE"])
TITLE_POS = tuple(settings["TITLE_POS"])
LIVES_POS = tuple(settings["LIVES_POS"])
LIVES_SIZE = tuple(settings["LIVES_SIZE"])
LIVES_SPACE = settings["LIVES_SPACE"]
TIME_POS = tuple(settings["TIME_POS"])
GAME_OVER_POS = tuple(settings["GAME_OVER_POS"])
GAME_OVER_SIZE = tuple(settings["GAME_OVER_SIZE"])

FPS = settings["FPS"]
SPEED = settings["SPEED"]

YELLOW = tuple(settings["YELLOW"])
PINK = tuple(settings["PINK"])
BACKGROUNDCOLOR = settings["BACKGROUNDCOLOR"]

rect_w = settings["rect_w"]
rect_h = settings["rect_h"]

bee_w = settings["bee_w"]
bee_h = settings["bee_h"]

min_speed = settings["min_speed"]
max_speed = settings["max_speed"]
speed_bee = randint(min_speed, max_speed)

item_w = settings["item_w"]
item_h = settings["item_h"]

move_left = settings["move_left"]
move_right = settings["move_right"]

borde = settings["borde"]

CANT_BEES = settings["CANT_BEES"]