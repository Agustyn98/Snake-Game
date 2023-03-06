import os
from enum import Enum

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Direction(Enum):
    UP= 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4