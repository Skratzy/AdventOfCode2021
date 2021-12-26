validation = False


def convert_bounds(bounds, bounds_to_convert_to):
    if bounds[0] < bounds_to_convert_to[1] and bounds[1] > bounds_to_convert_to[0]:
        if bounds[0] < bounds_to_convert_to[0]:
            bounds[0] = bounds_to_convert_to[0]
        if bounds[1] > bounds_to_convert_to[1]:
            bounds[1] = bounds_to_convert_to[1]

        return True, bounds

    return False, [0, 0]


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        cubes = {}
        for line in file:
            operation, bounds = line.strip().split(' ')
            operation = operation == 'on'
            x_bounds, y_bounds, z_bounds = bounds.split(',')
            x_in_bounds, x_bounds = convert_bounds([int(edge) for edge in x_bounds.split('=')[1].split('..')], [-50, 50])
            x_bounds[1] += 1
            y_in_bounds, y_bounds = convert_bounds([int(edge) for edge in y_bounds.split('=')[1].split('..')], [-50, 50])
            y_bounds[1] += 1
            z_in_bounds, z_bounds = convert_bounds([int(edge) for edge in z_bounds.split('=')[1].split('..')], [-50, 50])
            z_bounds[1] += 1

            #print(operation, x_bounds, y_bounds, z_bounds, x_in_bounds and y_in_bounds and z_in_bounds)
            if x_in_bounds and y_in_bounds and z_in_bounds:
                for x in range(*x_bounds):
                    for y in range(*y_bounds):
                        for z in range(*z_bounds):
                            cubes[tuple([x, y, z])] = operation
        cubes_on = 0
        for state in cubes.values():
            if state:
                cubes_on += 1
        return cubes_on


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        boxes = []
        for line in file:
            operation, bounds = line.strip().split(' ')
            operation = operation == 'on'
            x_bounds, y_bounds, z_bounds = bounds.split(',')
            x_bounds = [int(edge) for edge in x_bounds.split('=')[1].split('..')]
            x_bounds[1] += 1
            y_bounds = [int(edge) for edge in y_bounds.split('=')[1].split('..')]
            y_bounds[1] += 1
            z_bounds = [int(edge) for edge in z_bounds.split('=')[1].split('..')]
            z_bounds[1] += 1

            new_boxes = []
            for box in boxes:
                # Check for intersections
                x_intersects = box[0][0] <= x_bounds[1] and box[0][1] >= x_bounds[0]
                y_intersects = box[1][0] <= y_bounds[1] and box[1][1] >= y_bounds[0]
                z_intersects = box[2][0] <= z_bounds[1] and box[2][1] >= z_bounds[0]

                #print(f'{x_intersects=}, {y_intersects=}, {z_intersects=}')

                # If the cubes intersect, we need to start cutting them up in smaller pieces
                if x_intersects and y_intersects and z_intersects:
                    #print("Intersection!")

                    # [12|345|67]   -> [12] and |345| and [67]
                    # [1234|567]--| -> [1234] and |567--|
                    # |-[1234|567]  -> |-1234| and [567]

                    #print(f'{box=}')

                    if box[0][0] < x_bounds[0]:
                        new_boxes.append([[box[0][0], x_bounds[0]], [*box[1]], [*box[2]]])
                        box[0][0] = x_bounds[0]

                    if box[0][1] > x_bounds[1]:
                        new_boxes.append([[x_bounds[1], box[0][1]], [*box[1]], [*box[2]]])
                        box[0][1] = x_bounds[1]

                    if box[1][0] < y_bounds[0]:
                        new_boxes.append([[*box[0]], [box[1][0], y_bounds[0]], [*box[2]]])
                        box[1][0] = y_bounds[0]

                    if box[1][1] > y_bounds[1]:
                        new_boxes.append([[*box[0]], [y_bounds[1], box[1][1]], [*box[2]]])
                        box[1][1] = y_bounds[1]

                    if box[2][0] < z_bounds[0]:
                        new_boxes.append([[*box[0]], [*box[1]], [box[2][0], z_bounds[0]]])
                        box[2][0] = z_bounds[0]

                    if box[2][1] > z_bounds[1]:
                        new_boxes.append([[*box[0]], [*box[1]], [z_bounds[1], box[2][1]]])
                        box[2][1] = z_bounds[1]

                else:
                    # If there is no intersection, append the box directly
                    new_boxes.append(box)

            #print(new_boxes)

            boxes = new_boxes

            # Only add the new box if it an "on" operation
            if operation:
                boxes.append([x_bounds, y_bounds, z_bounds])

        boxes_turned_on = 0
        for box in boxes:
            boxes_turned_on += abs(box[0][1] - box[0][0]) * abs(box[1][1] - box[1][0]) * abs(box[2][1] - box[2][0])

        #print(boxes)

        return boxes_turned_on


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 583636 and answer_part_2 == 1294137045134837)
