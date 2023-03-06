rows = 13
cols = 25
block_increase_per_apple = 5
sleep_interval = 0.2

frame = [[None for j in range(cols)] for k in range(rows)]

from utils import Direction

class Game():
    def render_frame(self):
        output = ''
        for index, row in enumerate(frame):
            render_row = '|'
            if index == 0:
                first_row = ' ' + '_' * len(frame[0]) + ' ' + '\n'
                output += first_row
    
            for col in row:
                if col is None:
                    render_row += ' '
                else:
                    render_row += col
    
            output += render_row + '|\n'
    
            if index == len(frame) - 1:
                last_row = ' ' + '¯' * len(frame[0]) + ' ' + '\n'
                output += last_row
    
        print(output)
        return output
    
    
    def put_snake_in_frame(self, snake):
        for snake_index, (cord_x, cord_y) in enumerate(snake.positions):
            if cord_x >= rows or cord_y >= cols:
                return
            elif cord_x < 0 or cord_y < 0:
                return
            
            head_char = '<'
            if snake.next_move_direction == Direction.UP:
                head_char = 'ʌ'
            elif snake.next_move_direction == Direction.DOWN:
                head_char = 'v'
            elif snake.next_move_direction == Direction.RIGHT:
                head_char = '>'
            else:
                head_char = '<'
            snake_char = head_char if snake_index == 0 else 'O'
            frame[cord_x][cord_y] = snake_char
    
    
    