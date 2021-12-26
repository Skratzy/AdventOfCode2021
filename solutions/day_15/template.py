from collections import deque
from copy import deepcopy

from solutions.utilities.grid import Grid

validation = False


def djikstra(graph, start, end):
    queue = deque()
    dist = {v: 12831283218328123213 for v in graph}
    dist[start] = 0
    queue.append(start)
    prev = {}

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            new_cost = dist[node] + graph[node][neighbor]

            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                prev[neighbor] = node
                queue.append(neighbor)

    return dist, prev


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        data = [[int(char) for char in line] for line in file.read().split('\n')]
        grid = Grid(data)

        graph = {}
        for y in range(grid.size_y):
            for x in range(grid.size_x):
                start = tuple([x, y])
                graph.setdefault(start, {})
                for neighbor in grid.get_neighbors(x, y):
                    end = tuple(neighbor)
                    graph[start][end] = grid.get_value(neighbor)

        start = tuple([0, 0])
        curr_node = tuple([grid.size_x - 1, grid.size_y - 1])
        dist, path_to_search = djikstra(graph, start, end)

        shortest_path = []
        while curr_node != start:
            shortest_path.append(curr_node)
            curr_node = path_to_search[curr_node]

        path_cost = 0
        for step in shortest_path:
            path_cost += grid.get_value(step)

        return path_cost


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        data = [[int(char) for char in line] for line in file.read().split('\n')]
        new_data = deepcopy(data)
        for y in range(len(data)):
            for i in range(4):
                for x in range(len(data[y])):
                    new_data[y].append(max((new_data[y][len(data[y]) * i + x] + 1) % 10, 1))

        data = deepcopy(new_data)
        for i in range(4):
            for y in range(len(data)):
                new_x = []
                for x in range(len(data[y])):
                    new_x.append(max((new_data[len(data) * i + y][x] + 1) % 10, 1))
                new_data.append(new_x)


        grid = Grid(new_data)

        graph = {}
        for y in range(grid.size_y):
            for x in range(grid.size_x):
                start = tuple([x, y])
                graph.setdefault(start, {})
                for neighbor in grid.get_neighbors(x, y):
                    end = tuple(neighbor)
                    graph[start][end] = grid.get_value(neighbor)
        start = tuple([0, 0])
        curr_node = tuple([grid.size_x - 1, grid.size_y - 1])
        dist, path_to_search = djikstra(graph, start, end)
        shortest_path = []
        while curr_node != start:
            shortest_path.append(curr_node)
            curr_node = path_to_search[curr_node]

        path_cost = 0
        for step in shortest_path:
            path_cost += grid.get_value(step)

        return path_cost


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 498 and answer_part_2 == 2901)
