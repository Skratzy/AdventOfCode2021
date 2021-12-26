from solutions.utilities.grid import Grid
from solutions.utilities.utilities import draw_grid

validation = False


def get_neighbors(x, y):
    return [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1],
            [x - 1, y], [x, y], [x + 1, y],
            [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]


def output_from_input(input_grid, enhancement, iteration):
    output = ['.' * (input_grid.size_x + 2)] * (input_grid.size_y + 2)
    for y in range(len(output)):
        output_x = ''
        for x in range(len(output[0])):
            # Since we have a larger output grid, we need to remap the coordinates to the input grid
            grid_x = x - 1
            grid_y = y - 1
            neighbors = get_neighbors(grid_x, grid_y)
            enhancement_bin = ''
            for neighbor in neighbors:
                if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] >= input_grid.size_x or neighbor[1] >= input_grid.size_y:
                    if enhancement[0] == '.':
                        enhancement_bin += '0'
                    else:
                        enhancement_bin += str(iteration % 2)
                else:
                    enhancement_bin += '0' if input_grid.get_value(neighbor) == '.' else '1'

            output_x += enhancement[int(enhancement_bin, 2)]
        output[y] = output_x

    return output




def both_parts():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        enhancement, input_image = file.read().split('\n\n')

        input_image = input_image.split('\n')
        #print(input_image)

        grid = Grid(input_image)
        #draw_grid(grid.grid)
        first_part = 0
        second_part = 0
        output = grid
        for i in range(50):
            output = Grid(output_from_input(output, enhancement, i))
            lit_pixels = 0
            for y in range(output.size_y):
                lit_pixels += output.grid[y].count('#')
            if i == 1:
                first_part = lit_pixels
                #print(f'First part: {lit_pixels=}')
            if i == 49:
                second_part = lit_pixels
                #print(f'Second part: {lit_pixels=}')

        return first_part, second_part


answer_part_1, answer_part_2 = both_parts()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 5622 and answer_part_2 == 20395)
