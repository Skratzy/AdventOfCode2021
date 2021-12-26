validation = False


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        polymer_template, insertion_rules = file.read().split('\n\n')
        polymer_template = polymer_template.strip()
        insertion_rules = [insertion_rule.split(' -> ') for insertion_rule in insertion_rules.split('\n')]
        insertion_rules_dict = {}
        for key, value in insertion_rules:
            insertion_rules_dict[key] = value

        char_set = set()

        for i in range(10):
            new_polymer_template = polymer_template[0]
            for j in range(len(polymer_template) - 1):
                letter_one = polymer_template[j]
                letter_two = polymer_template[j+1]
                char_set.add(letter_one)
                char_set.add(letter_two)
                char_test = letter_one + letter_two
                new_polymer_template += insertion_rules_dict.setdefault(char_test, '') + letter_two
            polymer_template = new_polymer_template

        highest_val = 0
        lowest_val = 123871283721873128731
        for char in char_set:
            val = polymer_template.count(char)
            if val > highest_val:
                highest_val = val
            if val < lowest_val:
                lowest_val = val

        return highest_val - lowest_val


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        polymer_template, insertion_rules = file.read().split('\n\n')
        polymer_template = polymer_template.strip()
        insertion_rules = [insertion_rule.split(' -> ') for insertion_rule in insertion_rules.split('\n')]
        insertion_rules_dict = {}
        pairs = {}
        char_count = {}
        for key, value in insertion_rules:
            insertion_rules_dict[key] = value

        print(insertion_rules)

        char_count[polymer_template[0]] = 1
        for i in range(len(polymer_template) - 1):
            letter_one = polymer_template[i]
            letter_two = polymer_template[i + 1]
            pair = letter_one + letter_two

            pairs[pair] = pairs.get(pair, 0) + 1
            char_count[letter_two] = char_count.get(letter_two, 0) + 1

        print(pairs)
        print(char_count)

        for i in range(40):
            new_pairs = dict(pairs)
            pairs_to_remove = {}

            for pair, count in pairs.items():
                if pair in insertion_rules_dict:
                    insert_char = insertion_rules_dict[pair]

                    char_count[insert_char] = char_count.get(insert_char, 0) + count

                    pair_one = pair[0] + insert_char
                    new_pairs[pair_one] = new_pairs.get(pair_one, 0) + count

                    pair_two = insert_char + pair[1]
                    new_pairs[pair_two] = new_pairs.get(pair_two, 0) + count

                    pairs_to_remove[pair] = count

            pairs = dict(new_pairs)

            for pair, val in pairs_to_remove.items():
                pairs[pair] -= val

        highest_count = max(char_count.values())
        lowest_count = min(char_count.values())

        print(char_count)

        return highest_count - lowest_count


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 2345 and answer_part_2 == 2432786807053)
