import time

validation = False
hallway_to_stack_indices = [2, 4, 6, 8]
hallway_length = 11
cost_to_move = [1, 10, 100, 1000]
stack_depth = 2
COST_CACHE = {}
RECURSION_DEPTH = 0


def get_hallway_index_from_stack_index(stack_index):
    return 2 + 2 * stack_index


def get_possible_moves_from_stack(stack_index, hallway):
    hallway_start = get_hallway_index_from_stack_index(stack_index)
    possible_hallway_targets = []
    # Check all possible positions to the left
    for i in range(hallway_start - 1, -1, -1):
        if hallway[i] != '.':
            break
        if i not in hallway_to_stack_indices:
            possible_hallway_targets.append(i)
    possible_hallway_targets.reverse()

    # Check all possible positions to the right
    for i in range(hallway_start + 1, hallway_length):
        if hallway[i] != '.':
            break
        if i not in hallway_to_stack_indices:
            possible_hallway_targets.append(i)

    return possible_hallway_targets


def hallway_index_to_stack_index(hallway_index):
    try:
        return hallway_to_stack_indices.index(hallway_index)
    except ValueError:
        return None


def get_stack_index_from_character(char):
    return ord(char) - ord("A")


def can_move_to_target_stack(hallway_index, char, stacks, hallway):
    stack_index = get_stack_index_from_character(char)
    for stack_char in stacks[stack_index]:
        if stack_char != char:
            return False, -1

    hallway_target_index = hallway_to_stack_indices[stack_index]
    # Look to the left
    if hallway_target_index < hallway_index:
        # Move to left
        for i in range(hallway_index - 1, hallway_target_index - 1, -1):
            if hallway[i] != '.':
                return False, -1
    else:
        # Move to right
        for i in range(hallway_index + 1, hallway_target_index + 1):
            if hallway[i] != '.':
                return False, -1

    return True, stack_index


def should_pop_top_of_stack(stack_index, stack):
    # Check all characters in stack, if any of them shouldn't be there the top one should be moved
    for char in stack:
        if get_stack_index_from_character(char) != stack_index:
            return True
    return False


def check_if_done(stacks):
    for index, stack in enumerate(stacks):
        if len(stack) != stack_depth or should_pop_top_of_stack(index, stack):
            return False
    return True


def find_lowest_cost(stacks, hallway):
    global RECURSION_DEPTH
    RECURSION_DEPTH += 1
    cost = COST_CACHE.get((stacks, hallway))
    if cost is not None:
        return cost

    if check_if_done(stacks):
        return 0

    lowest_cost = float("inf")
    # Search all possible moves from hallway
    for index, char in enumerate(hallway):
        if char != '.':
            # Check if the character can be moved to its desired stack index
            can_move, stack_index = can_move_to_target_stack(index, char, stacks, hallway)
            if can_move:
                # Distance moved = hallway indices moved
                dist = abs(get_hallway_index_from_stack_index(stack_index) - index)
                # plus the depth to move
                dist += stack_depth - len(stacks[stack_index])
                # Lowest cost of all universes for this move
                new_hallway = list(hallway)
                new_stacks = []
                for stack in stacks:
                    new_stacks.append(list(stack))
                new_hallway[index] = '.'
                new_stacks[stack_index].append(char)

                for i in range(len(new_stacks)):
                    new_stacks[i] = tuple(new_stacks[i])

                # Perform search from current state and return the lowest cost
                cost = dist * cost_to_move[stack_index]
                cost += find_lowest_cost(tuple(new_stacks), tuple(new_hallway))
                if cost < lowest_cost:
                    lowest_cost = cost

    # Search all possible moves from stack
    for stack_index, stack in enumerate(stacks):
        if len(stack) > 0 and should_pop_top_of_stack(stack_index, stack):
            possible_hallway_targets = get_possible_moves_from_stack(stack_index, hallway)
            for hallway_target in possible_hallway_targets:
                new_hallway = list(hallway)
                new_stacks = []
                for new_stack in stacks:
                    new_stacks.append(list(new_stack))
                char = new_stacks[stack_index].pop()
                new_hallway[hallway_target] = char

                for i in range(len(new_stacks)):
                    new_stacks[i] = tuple(new_stacks[i])

                dist = stack_depth - len(stacks[stack_index]) + 1
                dist += abs(get_hallway_index_from_stack_index(stack_index) - hallway_target)

                cost = dist * cost_to_move[get_stack_index_from_character(char)]
                cost += find_lowest_cost(tuple(new_stacks), tuple(new_hallway))
                if cost < lowest_cost:
                    lowest_cost = cost

    COST_CACHE[(stacks, hallway)] = lowest_cost
    return lowest_cost


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        hallway = tuple(['.'] * hallway_length)

        lines = file.read().split('\n')

        stacks = tuple([tuple([lines[3][3], lines[2][3]]), tuple([lines[3][5], lines[2][5]]),
                        tuple([lines[3][7], lines[2][7]]), tuple([lines[3][9], lines[2][9]])])

        print(hallway)
        print(stacks)

        return find_lowest_cost(stacks, hallway)


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        hallway = tuple(['.'] * hallway_length)

        lines = file.read().split('\n')
        global stack_depth
        stack_depth = 4

        stacks = tuple([tuple([lines[3][3], 'D', 'D', lines[2][3]]),
                        tuple([lines[3][5], 'B', 'C', lines[2][5]]),
                        tuple([lines[3][7], 'A', 'B', lines[2][7]]),
                        tuple([lines[3][9], 'C', 'A', lines[2][9]])])

        print(hallway)
        print(stacks)

        return find_lowest_cost(stacks, hallway)


time_start = time.perf_counter()
answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 13558 and answer_part_2 == 56982)
print(f'Both parts took {time.perf_counter() - time_start} seconds.')
