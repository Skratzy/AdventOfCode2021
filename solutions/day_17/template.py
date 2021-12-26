from solutions.utilities.utilities import draw_grid_of_points

validation = False


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        zones = file.read().split(': ')[1]
        x_zone, y_zone = [[int(zone_val) for zone_val in zone_def.split('=')[1].split('..')] for zone_def in zones.split(', ')]
        top_left = [x_zone[0], y_zone[1]]
        bottom_right = [x_zone[1], y_zone[0]]

        highest_y = 0
        for y in range(0, abs(bottom_right[1])):
            curr_y = 0
            y_vel = y
            height = 0
            while bottom_right[1] < curr_y:
                curr_y += y_vel
                y_vel -= 1
                height = max(curr_y, height)
                if curr_y < top_left[1]:
                    # Hit
                    highest_y = max(height, highest_y)

        return highest_y


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        zones = file.read().split(': ')[1]
        x_zone, y_zone = [[int(zone_val) for zone_val in zone_def.split('=')[1].split('..')] for zone_def in zones.split(', ')]
        top_left = [x_zone[0], y_zone[1]]
        bottom_right = [x_zone[1], y_zone[0]]

        target_area_hits = 0
        for x in range(0, bottom_right[0] + 1):
            for y in range(-abs(bottom_right[1]), abs(bottom_right[1]) + 1):
                curr_x, curr_y = [0, 0]
                vel_x, vel_y = [x, y]
                hit = False
                while bottom_right[1] <= curr_y and curr_x <= bottom_right[0] and not hit:
                    curr_x += vel_x
                    vel_x -= 1 if vel_x > 0 else 0
                    curr_y += vel_y
                    vel_y -= 1
                    if bottom_right[1] <= curr_y <= top_left[1] and top_left[0] <= curr_x <= bottom_right[0]:
                        target_area_hits += 1
                        hit = True

        return target_area_hits


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 7626 and answer_part_2 == 2032)
