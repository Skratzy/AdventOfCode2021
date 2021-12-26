def draw_grid_of_points(points, bounds=None, char='o', do_print=True):
    """ Draw a grid based on the values in points, empty spots are drawn as [.] """
    if bounds is None:
        bounds = get_bounds_from_points(points)
    top_left = bounds[0]
    bottom_right = bounds[1]
    string = "\n"
    for y in range(top_left[1], bottom_right[1] + 1):
        row = ""
        for x in range(top_left[0], bottom_right[0] + 1):
            if tuple([x, y]) in points:
                row += char
            else:
                row += '.'
        if do_print:
            print(row)
        string += row + '\n'
    return string


def get_bounds_from_points(points):
    """ Returns two points, top left and bottom right of grid """
    x_max = -12398218372183123
    x_min = 213123123123
    y_max = -9342238429383984
    y_min = 213123213213
    for x, y in points:
        if x_min > x:
            x_min = x
        if x_max < x:
            x_max = x
        if y_min > y:
            y_min = y
        if y_max < y:
            y_max = y
    return [[x_min, y_min], [x_max, y_max]]


def draw_grid(grid):
    for line in grid:
        print("".join(line))


def get_x_y_from_args(*args):
    if len(args[0]) == 1:
        return [args[0][0][0], args[0][0][1]]
    else:
        return [args[0][0], args[0][1]]
