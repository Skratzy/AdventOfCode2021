import math
import solutions.utilities.utilities as util


class Grid:
    """ Grid class """
    size_x = 0
    size_y = 0
    keys = []

    grid = []

    def __init__(self, data, from_points=False):
        if from_points:
            self.size_y = max(data, key=lambda point: point[1])[1] + 1
            self.size_x = max(data, key=lambda point: point[0])[0] + 1

            for y in range(self.size_y):
                self.grid.append([])
                for x in range(self.size_x):
                    self.grid[y].append(1 if [x, y] in data else 0)

        else:
            self.grid = data
            self.size_x = len(self.grid[0])
            self.size_y = len(self.grid)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                self.keys.append([x, y])

    def get_neighbors(self, x, y, get_diagonal=False, out_of_bounds=None, deg_start=0, deg_negative=False):
        """ Get a list of valid neighbors """
        valid_neighbors = []

        sign = 1

        start = deg_start
        end = deg_start + 360
        if deg_negative:
            tmp = start
            start = end
            end = tmp
            sign = -1

        for deg in range(start, end, sign * 45 if get_diagonal else sign * 90):
            rad = math.radians(deg)
            ox = x + round(math.sin(rad))
            oy = y + round(math.cos(rad))
            in_bounds = self.is_in_bounds(ox, oy)
            if out_of_bounds or in_bounds:
                valid_neighbors.append([ox, oy])

        return valid_neighbors

    def is_in_bounds(self, x, y):
        """ Check if x and y is within the bounds of the grid """
        return -1 < y < len(self.grid) and -1 < x < len(self.grid[y])

    def get_value(self, *args, out_of_bounds=None):
        """ Get value from 'x, y' or [x, y] """
        x, y = util.get_x_y_from_args(args)

        try:
            return self.grid[y][x]
        except IndexError:
            if out_of_bounds:
                return out_of_bounds
            else:
                print(f"Error! [{[x, y]}] was out of bounds. {self.size_y=} {self.size_x}")
                raise

    def set_value(self, value, *args):
        x, y = util.get_x_y_from_args(args)

        try:
            self.grid[y][x] = value
        except IndexError:
            print(f"[{[x, y]}] was out of bounds. {self.size_y=} {self.size_x}")
            exit(1)