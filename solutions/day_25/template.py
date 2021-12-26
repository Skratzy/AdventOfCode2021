import copy

from solutions.utilities.grid import Grid
from solutions.utilities.utilities import draw_grid

validation = False


def move_east(grid):
    has_moved = False
    initial_state = copy.deepcopy(grid.grid)
    for y in range(grid.size_y):
        for x in range(grid.size_x):
            if initial_state[y][x] == '>':
                move_to_x = (x + 1) % grid.size_x
                if initial_state[y][move_to_x] == '.':
                    grid.grid[y][x] = '.'
                    grid.grid[y][move_to_x] = '>'
                    has_moved = True
    return has_moved


def move_south(grid):
    has_moved = False
    initial_state = copy.deepcopy(grid.grid)
    for x in range(grid.size_x):
        for y in range(grid.size_y):
            if initial_state[y][x] == 'v':
                move_to_y = (y + 1) % grid.size_y
                if initial_state[move_to_y][x] == '.':
                    grid.grid[y][x] = '.'
                    grid.grid[move_to_y][x] = 'v'
                    has_moved = True
    return has_moved


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        grid = Grid(list([char for char in line] for line in file.read().split('\n')))
        #draw_grid(grid.grid)
        has_moved = True
        steps = 0
        while has_moved:
            has_moved = move_east(grid)
            has_moved = move_south(grid) or has_moved
            steps += 1
            #if steps % 10 == 0:
            #    print(steps)
            #print('\n')
            #draw_grid(grid)
        return steps


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        # CLICK ZE BUTTON!
        return "CLICK ZE BUTTON!"


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 367 and answer_part_2 == "CLICK ZE BUTTON!")
