validation = False


def print_diagram(diagram, highest_x):
    for y in range(len(diagram)):
        for x in range(highest_x):
            print(diagram[y].get(x, '.'), end='')
        print('')


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        diagram = []
        highest_x = 0
        highest_y = 0
        for line in file:
            start, end = line.strip().split('->')
            x1, y1 = [int(val) for val in start.strip().split(',')]
            x2, y2 = [int(val) for val in end.strip().split(',')]
            x_arr = [x1, x2]
            x_arr.sort()
            y_arr = [y1, y2]
            y_arr.sort()

            x_equal = x1 == x2
            y_equal = y1 == y2

            if x_equal:
                x2 = x2 + 1
            if y_equal:
                y2 = y2 + 1

            highest_x = max(x1, x2, highest_x)
            highest_y = max(y1, y2, highest_y)

            for i in range(highest_y - (len(diagram) - 1)):
                diagram.append({})

            if x_equal or y_equal:
                for x in range(x_arr[0], x_arr[1] + 1):
                    for y in range(y_arr[0], y_arr[1] + 1):
                        if x in diagram[y]:
                            diagram[y][x] += 1
                        else:
                            diagram[y][x] = 1

        num_points = 0
        for row in diagram:
            for _, point in row.items():
                if point > 1:
                    num_points += 1

        return num_points


def get_points(x1, y1, x2, y2):
    start = [x1, y1]
    end = [x2, y2]

    if x1 > x2:
        tmp = list(start)
        start = list(end)
        end = list(tmp)

    # Only 45 degree diagonal lines so number of x's must equal number of y's
    if start[1] < end[1]:
        y_parts = range(start[1], end[1])
    else:
        y_parts = range(start[1], end[1], -1)
    x_parts = range(start[0], end[0])

    if start[0] == end[0]:
        return [[x1, y] for y in y_parts] + [[end[0], end[1]]]
    if start[1] == end[1]:
        return [[x, y1] for x in x_parts] + [[end[0], end[1]]]

    return [[x_parts[i], y_parts[i]] for i in range(len(x_parts))] + [[end[0], end[1]]]


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:

        # Solution here
        diagram = []
        highest_x = 0
        highest_y = 0
        for line in file:
            start, end = line.strip().split('->')
            x1, y1 = [int(val) for val in start.strip().split(',')]
            x2, y2 = [int(val) for val in end.strip().split(',')]
            x_arr = [x1, x2]
            y_arr = [y1, y2]

            x_equal = x1 == x2
            y_equal = y1 == y2

            if x_equal:
                x2 = x2 + 1
            if y_equal:
                y2 = y2 + 1

            highest_x = max(x1, x2, highest_x)
            highest_y = max(y1, y2, highest_y)

            for i in range(highest_y - (len(diagram) - 1)):
                diagram.append({})

            for x, y in get_points(x_arr[0], y_arr[0], x_arr[1], y_arr[1]):
                if x in diagram[y]:
                    diagram[y][x] += 1
                else:
                    diagram[y][x] = 1

        num_points = 0
        for row in diagram:
            for _, point in row.items():
                if point > 1:
                    num_points += 1

        return num_points


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 7318 and answer_part_2 == 19939)
