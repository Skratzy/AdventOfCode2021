class Graph:
    graph = {}

    def __init__(self, data=None):
        if data is not None:
            for data_point in data:
                self.add_edge(data_point[0], data_point[1])

    def add_edge(self, start, end):
        self.graph.setdefault(start, [])
        if end not in self.graph[start]:
            self.graph[start].append(end)
        self.graph.setdefault(end, [])
        if start not in self.graph[end]:
            self.graph[end].append(start)

    def dfs_util(self, start, visited, lambda_add_to_visited, lambda_loop_processing, lambda_after_found_paths):
        lambda_add_to_visited(start, visited)

        for neighbor in self.graph[start]:
            lambda_loop_processing(neighbor)
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, lambda_add_to_visited, lambda_loop_processing, lambda_after_found_paths)

        lambda_after_found_paths(start, visited)

    def depth_first_search(self, start):
        self.dfs_util(start, [], lambda x, y: None, lambda x: None, lambda x, y: None)
