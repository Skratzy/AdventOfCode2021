validation = False


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        prev_measurement = 12873178238
        increases_in_depth = 0
        for line in file:
            curr_measurement = int(line.strip())
            increases_in_depth += 1 if curr_measurement > prev_measurement else 0
            prev_measurement = curr_measurement
        return increases_in_depth


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        file_input = file.read().split('\n')
        prev_sum_of_three = 999999999999999
        increases_in_depth = 0
        for i in range(2, len(file_input), 1):
            #print(f'{file_input[i - 2]} + {file_input[i - 1]} + {file_input[i]}')
            sum_of_three = int(file_input[i - 2].strip()) + int(file_input[i - 1].strip()) + int(file_input[i].strip())
            #print(sum_of_three)
            increases_in_depth += 1 if sum_of_three > prev_sum_of_three else 0
            prev_sum_of_three = sum_of_three
        return increases_in_depth


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 1477 and answer_part_2 == 1523)
