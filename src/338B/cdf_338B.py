class CodeforcesTask338BSolution:
    def __init__(self):
        self.result = ''
        self.n_m_d = []
        self.affected = []
        self.paths = []

    def read_input(self):
        self.n_m_d = [int(x) for x in input().split(" ")]
        self.affected = [int(x) for x in input().split(" ")]
        for x in range(self.n_m_d[0] - 1):
            self.paths.append([int(x) for x in input().split(" ")])

    def process_task(self):
        #print(self.paths)
        graph = [[x, [], -1] for x in range(self.n_m_d[0])]
        for af in self.affected:
            graph[af - 1][2] = 0
        for path in self.paths:
            graph[path[0] - 1][1].append(path[1])
            graph[path[1] - 1][1].append(path[0])
        #print(graph)
        to_visit = [(pos, 0, -1, 1) for pos in self.affected]
        evil_locations = 0
        while to_visit:
            visiting = to_visit.pop(0)
            if not visiting[3]:
                if graph[visiting[0] - 1][2] <= visiting[1]:
                    for neigh in graph[visiting[0] - 1][1]:
                        if neigh != visiting[2]:
                            to_visit.append((neigh, visiting[1] + 1, visiting[0], 0))
                    graph[visiting[0] - 1][2] = visiting[1]
            else:
                for neigh in graph[visiting[0] - 1][1]:
                    if neigh != visiting[2]:
                        to_visit.append((neigh, visiting[1] + 1, visiting[0], 0))
                graph[visiting[0] - 1][2] = visiting[1]

        for edge in graph:
            if 0 < edge[2] <= self.n_m_d[2]:
                evil_locations += 1
        #print(graph)
        #print(evil_locations)
        self.result = str(evil_locations)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask338BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
