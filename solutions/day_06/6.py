validation = False


# Number of days per new lanternfish
# New lanternfish takes two more days
def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        fishes = [int(num) for num in file.read().strip().split(',')]
        #print(len(fishes))
        # 5934 345387
        for i in range(80):
            new_fishes = list(fishes)
            for index, fish in enumerate(fishes):
                if fish == 0:
                    new_fishes.append(8)
                    new_fishes[index] = 6
                else:
                    new_fishes[index] -= 1
            fishes = list(new_fishes)
        return len(fishes)


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        fishes = [int(num) for num in file.read().strip().split(',')]
        fish_dict = [0 for i in range(9)]

        for fish in fishes:
            fish_dict[fish] += 1

        for i in range(256):
            fishes_giving_birth = fish_dict[0]
            for j in range(0, 8):
                fish_dict[j] = fish_dict[j + 1]
            fish_dict[8] = fishes_giving_birth
            fish_dict[6] += fishes_giving_birth

        return sum(fish_dict)


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 345387 and answer_part_2 == 1574445493136)
