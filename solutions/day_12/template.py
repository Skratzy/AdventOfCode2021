validation = False


def depth_first_search(start_of_path, visited, paths):
    possible_paths = 0

    # Check if small cave
    start_of_path_is_lower = start_of_path.islower()

    # Add current cave to visited if small
    if start_of_path_is_lower:
        visited.append(start_of_path)

    # Loop through all possible paths
    for target_location in paths[start_of_path]:
        # If the target location is 'end', then we have found a possible path
        if target_location == 'end':
            possible_paths += 1
        # Otherwise, keep searching
        elif target_location not in visited:
            possible_paths += depth_first_search(target_location, visited, paths)

    # Found all possible paths for this start so remove the
    #   start cave from visited so we can visit it in other possible paths
    if start_of_path_is_lower:
        visited.remove(start_of_path)

    return possible_paths


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        caves = [line.split('-') for line in file.read().split('\n')]
        paths = {}
        for path in caves:
            if path[1] != 'start' and path[0] != 'end':
                paths.setdefault(path[0], []).append(path[1])
            if path[0] != 'start' and path[1] != 'end':
                paths.setdefault(path[1], []).append(path[0])
        return depth_first_search('start', [], paths)



def depth_first_search_2nd(start_of_path, visited, paths, visited_small_cave_twice):
    possible_paths = 0

    start_of_path_is_lower = start_of_path.islower()
    # Check if start is a small cave
    if start_of_path_is_lower:
        visited[start_of_path] += 1

    # Loop through all possible caves for the start cave
    for target_location in paths[start_of_path]:
        if target_location == 'end':
            possible_paths += 1
        else:
            # Already visited a small cave twice for this path
            if visited_small_cave_twice:
                if visited[target_location] < 1:
                    possible_paths += depth_first_search_2nd(target_location, visited, paths, True)
            # Have not visited a small cave twice for this path
            elif visited[target_location] < 2:

                if visited[target_location] == 1:
                    possible_paths += depth_first_search_2nd(target_location, visited, paths, True)
                else:
                    possible_paths += depth_first_search_2nd(target_location, visited, paths, False)

    # Found all possible paths for this start so remove 1 visit from the start cave so it can be visited in other paths
    if start_of_path_is_lower:
        visited[start_of_path] -= 1

    return possible_paths


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        caves = [line.split('-') for line in file.read().split('\n')]
        paths = {}
        for path in caves:
            if path[1] != 'start' and path[0] != 'end':
                paths.setdefault(path[0], []).append(path[1])
            if path[0] != 'start' and path[1] != 'end':
                paths.setdefault(path[1], []).append(path[0])
        visited = {}
        for cave in paths:
            visited[cave] = 0
        return depth_first_search_2nd('start', visited, paths, False)


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 3495 and answer_part_2 == 94849)
