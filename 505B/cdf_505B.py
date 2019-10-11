class CodeforcesTask505BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.edges = []
        self.q = 0
        self.queries = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.edges.append([int(y) for y in input().split(" ")])
        self.q = int(input())
        for x in range(self.q):
            self.queries.append([int(y) for y in input().split(" ")])

    def process_task(self):
        graphs = [[[] for x in range(self.n_m[0])] for c in range(self.n_m[1])]
        for edge in self.edges:
            graphs[edge[2] - 1][edge[0] - 1].append(edge[1])
            graphs[edge[2] - 1][edge[1] - 1].append(edge[0])
        results = []
        for query in self.queries:
            to_visit = [(query[0], c) for c in range(self.n_m[1])]
            used = set()
            visited = [[False] * self.n_m[0] for x in range(self.n_m[1])]
            while to_visit:
                visiting = to_visit.pop(-1)

                if visiting[1] not in used and not visited[visiting[1]][visiting[0] - 1]:
                    visited[visiting[1]][visiting[0] - 1] = True
                    if visiting[0] == query[1]:
                        used.add(visiting[1])
                    else:
                        to_visit.extend([(x, visiting[1]) for x in graphs[visiting[1]][visiting[0] - 1]])
            colors = len(used)
            results.append(colors)
        self.result = "\n".join([str(x) for x in results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask505BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
