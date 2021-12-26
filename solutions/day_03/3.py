import numpy as np

validation = False


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        data = file.read().split('\n')
        gamma_binary = ""
        epsilon_binary = ""
        for i in range(len(data[0])):
            ones = 0
            zeros = 0
            for j in range(len(data)):
                if '1' in data[j][i]:
                    ones += 1
                elif '0' in data[j][i]:
                    zeros += 1
            if ones > zeros:
                gamma_binary += '1'
                epsilon_binary += '0'
            elif ones < zeros:
                gamma_binary += '0'
                epsilon_binary += '1'
        # Solution here
        return int(gamma_binary, 2) * int(epsilon_binary, 2)


def update_array(data, most_common_value):
    for i in range(len(data[0])):
        ones = 0
        zeros = 0
        most_common = 0
        least_common = 0
        for j in range(len(data)):
            if '1' in data[j][i]:
                ones += 1
            elif '0' in data[j][i]:
                zeros += 1
        if ones > zeros:
            most_common = 1
            least_common = 0
        elif ones < zeros:
            most_common = 0
            least_common = 1
        elif ones == zeros:
            most_common = 1
            least_common = 0

        print(f'{most_common=} {least_common}')

        if most_common_value:
            data = [val for val in data if int(val[i]) == most_common]
        else:
            data = [val for val in data if int(val[i]) == least_common]
        print(f'{data}')

        if len(data) == 1:
            return data

    return data


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        data = file.read().split('\n')
        oxygen_gen_rating_numbers = list(data)
        co2_scrub_rating_numbers = list(data)
        print(f'{oxygen_gen_rating_numbers=} {co2_scrub_rating_numbers=}')
        oxygen_gen_rating_number = int(update_array(oxygen_gen_rating_numbers, True)[0], 2)
        co2_scrub_rating_number = int(update_array(co2_scrub_rating_numbers, False)[0], 2)
        print(f'{oxygen_gen_rating_number=} {co2_scrub_rating_number=}')
        return oxygen_gen_rating_number * co2_scrub_rating_number


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 2967914 and answer_part_2 == 7041258)
