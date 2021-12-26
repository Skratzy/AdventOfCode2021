from solutions.utilities.grid import Grid

validation = False


def draw_grid(grid):
    for line in grid:
        print("".join(list([str(integer) for integer in line])))
    print('\n')


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        grid = Grid([[int(char) for char in line] for line in file.read().split('\n')])
        total_flashes = 0
        #draw_grid(grid.grid)

        for i in range(100):
            to_flash = []
            has_flashed = 0
            for x, y in grid.keys:
                grid.grid[y][x] += 1
                if grid.grid[y][x] > 9:
                    to_flash.append([x, y])
                    grid.grid[y][x] = 0

            while len(to_flash) > 0:
                x, y = to_flash.pop()
                has_flashed += 1
                for neighbor_x, neighbor_y in grid.get_neighbors(x, y, get_diagonal=True):
                    if grid.grid[neighbor_y][neighbor_x] > 0:
                        grid.grid[neighbor_y][neighbor_x] += 1
                        if grid.grid[neighbor_y][neighbor_x] > 9:
                            to_flash.append([neighbor_x, neighbor_y])
                            grid.grid[neighbor_y][neighbor_x] = 0
            #draw_grid(grid.grid)

            total_flashes += has_flashed

        return total_flashes


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        energy_levels = [[int(char) for char in line] for line in file.read().split('\n')]
        total_energy_levels = len(energy_levels[0]) * len(energy_levels)
        total_flashes = 0

        step = 0
        while True:
            to_flash = []
            has_flashed = []
            for y in range(len(energy_levels)):
                for x in range(len(energy_levels[y])):
                    energy_levels[y][x] += 1
                    if energy_levels[y][x] > 9:
                        to_flash.append([x, y])
                        has_flashed.append([x, y])

            while len(to_flash) > 0:
                x, y = to_flash.pop()
                for x_check in range(x - 1, x + 2):
                    for y_check in range(y - 1, y + 2):
                        if -1 < y_check < len(energy_levels) and -1 < x_check < len(energy_levels[y]):
                            if [x_check, y_check] not in has_flashed:
                                energy_levels[y_check][x_check] += 1
                                if energy_levels[y_check][x_check] > 9:
                                    to_flash.append([x_check, y_check])
                                    has_flashed.append([x_check, y_check])
            for flashed in has_flashed:
                energy_levels[flashed[1]][flashed[0]] = 0

            step += 1

            if len(has_flashed) == total_energy_levels:
                return step


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 1705 and answer_part_2 == 265)
