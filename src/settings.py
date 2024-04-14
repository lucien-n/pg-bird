import pygame as pg
from math import floor
from pygame.math import Vector2 as vec
from .colors import Colors
from pathlib import Path
from time import time

path = Path(__file__).parent.parent


SIZE = WIDTH, HEIGHT = 1280, 720
CANVAS_SIZE = 400
TARGET_FPS = 120

PIPE_GAP = 120
PIPE_WIDTH = 48
PIPE_SPEED = 150

BIRD_GRAVITY = 18
BIRD_JUMP_FORCE = 500

TEXT_SPACING = 4
