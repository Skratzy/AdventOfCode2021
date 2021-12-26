import solutions.utilities.utilities as util

validation = False


def perform_fold(points, fold_val, along_x):
    points_to_remove = []
    points_to_append = []
    for index, point in enumerate(points):
        checker = point[0] if along_x else point[1]
        if checker > fold_val:
            points_to_remove.append(index)
            new_val = fold_val - (checker - fold_val)
            unchanged_val = point[1] if along_x else point[0]
            new_point = [new_val, unchanged_val] if along_x else [unchanged_val, new_val]
            if new_point not in points:
                points_to_append.append(new_point)

    points.extend(points_to_append)
    points_to_remove.reverse()
    for to_remove in points_to_remove:
        del points[to_remove]


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        points, instructions = file.read().split('\n\n')
        points = [[int(coord) for coord in point.split(',')] for point in points.split('\n')]
        instructions = instructions.strip().split('\n')

        for fold_instruction in instructions:
            fold_val = int(fold_instruction.split('=')[1])
            perform_fold(points, fold_val, "fold along x" in fold_instruction)
            break

        return len(points)


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        points, instructions = file.read().split('\n\n')
        points = [[int(coord) for coord in point.split(',')] for point in points.split('\n')]
        instructions = instructions.strip().split('\n')

        for fold_instruction in instructions:
            fold_val = int(fold_instruction.split('=')[1])
            perform_fold(points, fold_val, "fold along x" in fold_instruction)

        return util.draw_grid_of_points([tuple(point) for point in points], char='#', do_print=False)


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=}')
print(f'answer_part_2={answer_part_2}')
assert(answer_part_1 == 675 and answer_part_2 == "\n#..#.####.#..#.#..#.####.####...##.####\n#..#....#.#.#..#..#.#....#.......#....#\n####...#..##...####.###..###.....#...#.\n#..#..#...#.#..#..#.#....#.......#..#..\n#..#.#....#.#..#..#.#....#....#..#.#...\n#..#.####.#..#.#..#.#....####..##..####\n")
