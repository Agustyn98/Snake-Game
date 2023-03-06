import random
from game import rows, cols, frame

class Apple():
    def __init__(self, snake_positions) -> None:
        self.position = [random.randint(
            0, rows - 1), random.randint(0, cols - 1)]
        while self.position in snake_positions:
            self.position = [random.randint(
                0, rows - 1), random.randint(0, cols - 1)]

    def set_apple(self):
        # print(f'putting apple at: {self.position} ')
        # print(f'where there is:{frame[self.position[0]][self.position[1]]}')
        frame[self.position[0]][self.position[1]] = '#'

