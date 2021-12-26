import math
from time import perf_counter

validation = False


flat_values = []
value_depths = []
curr_depth = 1


def parse_array(line, curr_index):
    pairs = []
    global flat_values
    global value_depths
    global curr_depth
    while True:
        curr_char = line[curr_index]
        curr_index += 1
        if curr_char == '[':
            curr_depth += 1
            # Start of new sub pair
            sub_pair, curr_index = parse_array(line, curr_index)
            pairs.append(sub_pair)
        elif curr_char == ']':
            curr_depth -= 1
            # End of current pair
            return pairs, curr_index
        elif curr_char == ',':
            pass
        else:
            # Number
            pairs.append(int(curr_char))
            flat_values.append(int(curr_char))
            value_depths.append(curr_depth)
            pass


def explode():
    global flat_values
    global value_depths

    try:
        index = next(i for i, v in enumerate(value_depths) if v > 4)

        new_value_depths = value_depths[0: index]
        new_flat_values = flat_values[0: index]

        left_value = flat_values[index]
        right_value = flat_values[index + 1]
        if index - 1 > -1:
            new_flat_values[index - 1] += left_value
        if index + 2 < len(flat_values):
            flat_values[index + 2] += right_value

        new_value_depths.append(value_depths[index] - 1)
        new_value_depths.extend(value_depths[index + 2:])
        new_flat_values.append(0)
        new_flat_values.extend(flat_values[index + 2:])

        flat_values = new_flat_values
        value_depths = new_value_depths

        return True

    except StopIteration:
        return False


def split():
    global flat_values
    global value_depths

    try:
        index = next(i for i, v in enumerate(flat_values) if v > 9)

        new_value_depths = value_depths[0: index]
        new_flat_values = flat_values[0: index]

        flat_value = flat_values[index]
        new_flat_values.append(math.floor(flat_value / 2))
        new_flat_values.append(math.ceil(flat_value / 2))
        new_flat_values.extend(flat_values[index + 1:])

        value_depth = value_depths[index]
        new_value_depths.append(value_depth + 1)
        new_value_depths.append(value_depth + 1)
        new_value_depths.extend(value_depths[index + 1:])

        flat_values = new_flat_values
        value_depths = new_value_depths

        return True

    except StopIteration:
        return False


def reduce():
    if explode():
        return True
    if split():
        return True
    return False


def append_to_val_stack_dict(val_stack_dict, depth, val):
    if len(val_stack_dict[depth]):
        append_to_val_stack_dict(val_stack_dict, depth - 1, val_stack_dict[depth].pop() * 3 + val * 2)
    else:
        val_stack_dict[depth].append(val)


def part_1():
    time_start = perf_counter()
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        global value_depths
        global flat_values
        global curr_depth

        pairs, index = parse_array(file.readline().strip(), 1)

        for line in file:
            curr_depth += 1

            curr_pairs, index = parse_array(line.strip(), 1)
            new_pairs = [pairs, curr_pairs]
            pairs = new_pairs

            for i in range(len(value_depths)):
                value_depths[i] += 1

            something_happened = True
            while something_happened:
                something_happened = reduce()

                # print('Depths: ' + str(value_depths))
                # print('Values: ' + str(flat_values))
                # #print(pairs)
                # print('')

        print('Depths: ' + str(value_depths))
        print('Values: ' + str(flat_values))
        # print(pairs)
        print('')

        my_iter = iter(range(1, len(value_depths)))
        last_depth = value_depths[0]
        val_stack_dict = {0: [], 1: [], 2: [], 3: [], 4: []}
        val_stack_dict[last_depth].append(flat_values[0])
        for i in my_iter:
            #print(last_depth, value_depths[i])
            curr_depth = value_depths[i]
            if last_depth == curr_depth:
                # Same level
                if len(val_stack_dict[curr_depth]) > 0:
                    val = 3 * val_stack_dict[curr_depth].pop() + 2 * flat_values[i]
                    append_to_val_stack_dict(val_stack_dict, curr_depth - 1, val)
                else:
                    val_stack_dict[curr_depth].append(flat_values[i])
            elif last_depth < curr_depth:
                val_stack_dict[curr_depth].append(flat_values[i])
            else:
                if len(val_stack_dict[curr_depth]) > 0:
                    curr_depth_stack_val = val_stack_dict[curr_depth].pop()
                    val = 3 * curr_depth_stack_val + 2 * flat_values[i]
                    append_to_val_stack_dict(val_stack_dict, curr_depth - 1, val)
                else:
                    val_stack_dict[curr_depth].append(flat_values[i])
            last_depth = curr_depth

        print(f'part_1 took {perf_counter() - time_start} seconds.')

        return val_stack_dict[0][0]


def part_2():
    time_start = perf_counter()
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        print('\n' + '-'*20 + '\n')
        # Solution here
        lines = file.read().split('\n')
        largest_magnitude = 0
        global value_depths
        global flat_values
        global curr_depth
        print(lines)

        val_stack_tot_seconds = 0

        for i in range(len(lines)):
            value_depths = []
            flat_values = []
            curr_depth = 1
            _ = parse_array(lines[i], 1)
            base_val_depths_at_i = list(value_depths)
            base_flat_values_at_i = list(flat_values)
            for j in range(len(lines)):
                if i != j:
                    value_depths = list(base_val_depths_at_i)
                    flat_values = list(base_flat_values_at_i)

                    curr_depth = 1
                    _ = parse_array(lines[j], 1)

                    for k in range(len(value_depths)):
                        value_depths[k] += 1

                    val_stack_perf_start = perf_counter()
                    something_happened = True
                    while something_happened:
                        something_happened = reduce()
                    val_stack_tot_seconds += perf_counter() - val_stack_perf_start


                    my_iter = iter(range(1, len(value_depths)))
                    last_depth = value_depths[0]
                    val_stack_dict = {0: [], 1: [], 2: [], 3: [], 4: []}
                    val_stack_dict[last_depth].append(flat_values[0])
                    for l in my_iter:
                        curr_depth = value_depths[l]
                        if last_depth == curr_depth:
                            # Same level
                            if len(val_stack_dict[curr_depth]) > 0:
                                val = 3 * val_stack_dict[curr_depth].pop() + 2 * flat_values[l]
                                append_to_val_stack_dict(val_stack_dict, curr_depth - 1, val)
                            else:
                                val_stack_dict[curr_depth].append(flat_values[l])
                        elif last_depth < curr_depth:
                            val_stack_dict[curr_depth].append(flat_values[l])
                        else:
                            if len(val_stack_dict[curr_depth]) > 0:
                                curr_depth_stack_val = val_stack_dict[curr_depth].pop()
                                val = 3 * curr_depth_stack_val + 2 * flat_values[l]
                                append_to_val_stack_dict(val_stack_dict, curr_depth - 1, val)
                            else:
                                val_stack_dict[curr_depth].append(flat_values[l])
                        last_depth = curr_depth
                    largest_magnitude = max(val_stack_dict[0][0], largest_magnitude)
        print(f'{val_stack_tot_seconds}')
        print(f'part_2 took {perf_counter() - time_start} seconds.')

        return largest_magnitude


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 3884 and answer_part_2 == 4595)
# Before
# part_1 took 0.069 seconds.
# part_2 took 1.226 seconds.

# Small optimization
# part_1 took 0.043 seconds.
# part_2 took 0.799 seconds.