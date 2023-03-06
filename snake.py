from utils import Direction
from apple import Apple
from game import rows, cols, frame, block_increase_per_apple


class Snake():
    def __init__(self, init_position: list = None) -> None:
        self.score = 0
        if init_position is None:
            self.positions = [self._get_middle_position()]
        else:
            self.positions = [init_position]

    def set_initial_snake(self, snake_initial_lenght=3) -> list[list]:
        inital_position = self._get_middle_position()
        initial_row, inital_col = inital_position
        for i in range(1, snake_initial_lenght, 1):
            self.positions.append([initial_row, inital_col - i])

        return self.positions

    def increase_size(self):
        new_x, new_y = self.positions[-1][0], self.positions[-1][1]

        if new_x >= rows:
            new_x = rows - 1
        elif new_x < 0:
            new_x = 0
        if new_y >= cols:
            new_y = cols - 1
        elif new_y < 0:
            new_y = 0

        self.positions.append([new_x, new_y])

    next_move_direction = Direction.RIGHT

    can_move = True

    def move(self, direction: int = next_move_direction):
        if self.can_move == False:
            return
        snake_tail_x, snake_tail_y = self.positions[-1]
        frame[snake_tail_x][snake_tail_y] = None
        self.positions.pop()
        if direction == Direction.UP:
            self.positions.insert(
                0, [self.positions[0][0] - 1, self.positions[0][1]])
        elif direction == Direction.DOWN:
            self.positions.insert(
                0, [self.positions[0][0] + 1, self.positions[0][1]])
        elif direction == Direction.LEFT:
            self.positions.insert(
                0, [self.positions[0][0], self.positions[0][1] - 1])
        elif direction == Direction.RIGHT:
            self.positions.insert(
                0, [self.positions[0][0], self.positions[0][1] + 1])

        self.check_apple()

    out_of_bounds = False

    def check_out_of_bounds(self):
        if self.positions[0][1] >= cols or self.positions[0][1] < 0 or self.positions[0][0] >= rows or self.positions[0][0] < 0:
            self.out_of_bounds = True
            return True

    def check_body_clash(self):
        snake_head = self.positions[0]
        snake_body = self.positions[1:]
        if snake_head in snake_body:
            return True

    def check_apple(self):
        if self.positions[0][0] >= rows or self.positions[0][1] >= cols:
            return
        if frame[self.positions[0][0]][self.positions[0][1]] == '#':
            self.score += 1
            for _ in range(block_increase_per_apple):
                self.increase_size()
            apple = Apple(self.positions)
            apple.set_apple()

    def _get_middle_position(self):
        return [int((rows-1) / 2), int((cols-1) / 2)]
