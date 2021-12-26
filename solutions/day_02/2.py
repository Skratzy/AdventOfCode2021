validation = False


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        horizontal = 0
        depth = 0
        for line in file:
            direction, val = line.split()
            val = int(val)
            if "forward" in direction:
                horizontal += val
            elif "down" in direction:
                depth += val
            elif "up" in direction:
                depth -= val
        return horizontal * depth


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        # Solution here
        horizontal = 0
        depth = 0
        aim = 0
        for line in file:
            direction, val = line.split()
            val = int(val)
            if "forward" in direction:
                horizontal += val
                depth += aim * val
            elif "down" in direction:
                aim += val
            elif "up" in direction:
                aim -= val
        return horizontal * depth


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 1561344 and answer_part_2 == 1848454425)
