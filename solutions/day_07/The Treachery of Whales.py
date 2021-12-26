import statistics

validation = False


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        crabs = [int(crab_pos) for crab_pos in file.read().strip().split(',')]
        target = statistics.median(crabs)
        total_cost = 0
        for crab in crabs:
            total_cost += abs(crab - target)
        return total_cost


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        crabs = [int(crab_pos) for crab_pos in file.read().strip().split(',')]

        lowest_total_cost = 123872138721387123872138
        # Runs quick enough to brute force
        for i in range(min(crabs), max(crabs) + 1):
            total_cost = 0
            for crab in crabs:
                total_cost += sum(range(1, abs(crab - i) + 1))
            if total_cost < lowest_total_cost:
                lowest_total_cost = total_cost

        # You can also get the correct position by ceiling the mean of all crabs while on input, and flooring when
        # doing the same on the validation. Not entirely sure why, but the brute force technique works best.

        return lowest_total_cost


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 355592 and answer_part_2 == 101618069)
