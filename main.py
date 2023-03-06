from pynput.keyboard import Key
from pynput import keyboard
from utils import Direction
from time import sleep
from utils import clear_screen
from apple import Apple
from snake import Snake
from game import Game, sleep_interval

game = Game()

snake = Snake()
snake.set_initial_snake()
apple = Apple(snake_positions=snake.positions)
apple.set_apple()


last_key = Key.right


def on_key_press(key):
    global last_key
    if key == Key.right:
        if last_key == Key.left:
            return
        snake.next_move_direction = Direction.RIGHT
        snake.move(snake.next_move_direction)
    elif key == Key.left:
        if last_key == Key.right:
            return
        snake.next_move_direction = Direction.LEFT
        snake.move(snake.next_move_direction)
    elif key == Key.up:
        if last_key == Key.down:
            return
        snake.next_move_direction = Direction.UP
        snake.move(snake.next_move_direction)
    elif key == Key.down:
        if last_key == Key.up:
            return
        snake.next_move_direction = Direction.DOWN
        snake.move(snake.next_move_direction)

    snake.can_move = False
    last_key = key


listener = keyboard.Listener(on_press=on_key_press)
listener.start()

while True:
    clear_screen()
    snake.move(snake.next_move_direction)
    game.put_snake_in_frame(snake)
    snake.can_move = True
    game.render_frame()
    if snake.check_out_of_bounds() or snake.check_body_clash():
        print(f'Game Over\nScore: {snake.score}\n')
        break
    sleep(sleep_interval)
