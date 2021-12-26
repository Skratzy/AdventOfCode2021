validation = False


def is_lowest_adjacent(points, x, y):
    curr_point = points[y][x]
    # left
    if x - 1 > -1:
        if points[y][x - 1] <= curr_point:
            return False
    # right
    if x + 1 < len(points[y]):
        if points[y][x + 1] <= curr_point:
            return False
    # up
    if y - 1 > -1:
        if points[y - 1][x] <= curr_point:
            return False
    # down
    if y + 1 < len(points):
        if points[y + 1][x] <= curr_point:
            return False
    return True


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        points = [[int(char) for char in line] for line in file.read().split('\n')]
        #for line in points:
        #    print(line)
        risk_levels = 0
        for y in range(len(points)):
            for x in range(len(points[y])):
                if is_lowest_adjacent(points, x, y):
                    risk_levels += points[y][x] + 1
        return risk_levels


def get_basin(points, x, y, adjacent_basin_points):
    # left
    check_x = x - 1
    check_y = y
    if check_x > -1:
        if points[check_y][check_x] < 9:
            points[check_y][check_x] = 9
            adjacent_basin_points.append([check_x, check_y])
            adjacent_basin_points.extend(get_basin(points, check_x, check_y, []))

    # right
    check_x = x + 1
    if check_x < len(points[check_y]):
        if points[check_y][check_x] < 9:
            points[check_y][check_x] = 9
            adjacent_basin_points.append([check_x, check_y])
            adjacent_basin_points.extend(get_basin(points, check_x, check_y, []))

    # up
    check_x = x
    check_y = y - 1
    if check_y > -1:
        if points[check_y][check_x] < 9:
            points[check_y][check_x] = 9
            adjacent_basin_points.append([check_x, check_y])
            adjacent_basin_points.extend(get_basin(points, check_x, check_y, []))

    # down
    check_y = y + 1
    if check_y < len(points):
        if points[check_y][check_x] < 9:
            points[check_y][check_x] = 9
            adjacent_basin_points.append([check_x, check_y])
            adjacent_basin_points.extend(get_basin(points, check_x, check_y, []))

    return adjacent_basin_points


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        points = [[int(char) for char in line] for line in file.read().split('\n')]
        basins = []
        for y in range(len(points)):
            for x in range(len(points[y])):
                if points[y][x] < 9:
                    points[y][x] = 9
                    basins.append(get_basin(points, x, y, []))
        basins = sorted(basins, key=lambda x: len(x), reverse=True)
        product = 1
        for i in range(0, min(len(basins), 3)):
            product *= (len(basins[i]) + 1)
        return product


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 462 and answer_part_2 == 1397760)
