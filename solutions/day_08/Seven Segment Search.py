from itertools import permutations

validation = False


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        one = 2
        four = 4
        seven = 3
        eight = 7
        signal_patterns = [[patterns.split() for patterns in signal_pattern.split('|')] for signal_pattern in file.read().split('\n')]

        correct_lengths = 0
        for input_segment, output_values in signal_patterns:
            for output_value in output_values:
                if one == len(output_value) or four == len(output_value) or seven == len(output_value) or eight == len(output_value):
                    correct_lengths += 1
        return correct_lengths


def string_contains_all_set(string, char_set):
    return False not in ([c in char_set for c in string])


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        signal_patterns = [[patterns.split() for patterns in signal_pattern.split('|')] for signal_pattern in file.read().split('\n')]

        total_val = 0
        for input_values, output_values in signal_patterns:
            words = {}
            for input_value in input_values:
                index = len(input_value)
                words.setdefault(index, []).append(set(input_value))

            integer_mappings = ["" for i in range(0, 10)]
            integer_mappings[1] = words.pop(2)[0]
            integer_mappings[4] = words.pop(4)[0]
            integer_mappings[7] = words.pop(3)[0]
            integer_mappings[8] = words.pop(7)[0]

            # Input with 6 in length is 0, 6 and 9 - testing those first
            # 9
            index_to_remove = 0
            for index, word in enumerate(words[6]):
                if integer_mappings[4] <= word and integer_mappings[7] <= word:
                    integer_mappings[9] = word
                    index_to_remove = index
                    break

            words[6].pop(index_to_remove)

            # 0 and 6
            for word in words[6]:
                # 1 is a subset of 0
                if integer_mappings[1] <= word:
                    integer_mappings[0] = word
                # If 1 is not a subset, then the word is 6
                else:
                    integer_mappings[6] = word

            words.pop(6)

            # Input with 5 in length is 2, 3 and 5 - testing those now
            index_to_remove = 0
            for index, word in enumerate(words[5]):
                # 1 is a subset of 3
                if integer_mappings[1] <= word:
                    integer_mappings[3] = word
                    index_to_remove = index
                    break

            words[5].pop(index_to_remove)

            # 2 and 5 left
            for word in words[5]:
                # 5 is a subset of 6
                if word <= integer_mappings[6]:
                    integer_mappings[5] = word
                # anything else is a 2
                else:
                    integer_mappings[2] = word

            code = ""
            for output_value in output_values:
                code += str(integer_mappings.index(set(output_value)))

            print(code)
            total_val += int(code)

        # Solution here
        return total_val


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 473 and answer_part_2 == 1097568)
