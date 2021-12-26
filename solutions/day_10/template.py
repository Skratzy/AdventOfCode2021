import statistics
import math

validation = False


def get_first_corrupted_chunk(line):
    openers = []
    for index, char in enumerate(line):
        if char == '}':
            last_opener = openers.pop()
            if last_opener != '{':
                return 1197
        elif char == ']':
            last_opener = openers.pop()
            if last_opener != '[':
                return 57
        elif char == ')':
            last_opener = openers.pop()
            if last_opener != '(':
                return 3
        elif char == '>':
            last_opener = openers.pop()
            if last_opener != '<':
                return 25137
        else:
            openers.append(char)
    return 0


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        stack_dict = {'{': [], '}': [], '[': [], ']': [], '(': [], ')': [], '<': [], '>': []}
        total_score = 0
        for line in file:
            total_score += get_first_corrupted_chunk(line.strip())

        return total_score


def get_all_unfinished_openers(line):
    openers = []
    for index, char in enumerate(line):
        if char == '}':
            last_opener = openers.pop()
            if last_opener != '{':
                return []
        elif char == ']':
            last_opener = openers.pop()
            if last_opener != '[':
                return []
        elif char == ')':
            last_opener = openers.pop()
            if last_opener != '(':
                return []
        elif char == '>':
            last_opener = openers.pop()
            if last_opener != '<':
                return []
        else:
            openers.append(char)
    return openers


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        scores = []
        for index, line in enumerate(file):
            score = 0
            openers = get_all_unfinished_openers(line.strip())
            print(index, openers)
            if len(openers) > 0:
                openers.reverse()
                for opener in openers:
                    match opener:
                        case '(':
                            score *= 5
                            score += 1
                        case '[':
                            score *= 5
                            score += 2
                        case '{':
                            score *= 5
                            score += 3
                        case '<':
                            score *= 5
                            score += 4
                #print(openers, score)
                scores.append(score)
        scores.sort()
        print(scores[int(math.floor(len(scores) / 2))])
        return statistics.median(scores)


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 392043 and answer_part_2 == 1605968119)
