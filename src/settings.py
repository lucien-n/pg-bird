import pygame as pg
from math import floor
from pygame.math import Vector2 as vec
from .colors import Colors
from pathlib import Path
from time import time

path = Path(__file__).parent.parent


SIZE = WIDTH, HEIGHT = 1280, 720
GAME_SIZE = GAME_WIDTH, GAME_HEIGHT = 288, 512

TARGET_FPS = 120

PIPE_SPEED = 150

PIPE_GREEN_SCORE = 10
PIPE_RED_SCORE = 10

PIPE_GREEN_GAP = 130
PIPE_RED_GAP = 100

PIPE_GREEN_SCORE = 10
PIPE_RED_SCORE = 25

BIRD_GRAVITY = 18
BIRD_JUMP_FORCE = 500
BIRD_JUMP_COOLDOWN_MS = 150

TEXT_SPACING = 4
