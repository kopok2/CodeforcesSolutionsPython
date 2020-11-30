class CodeforcesTask780CSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.edges = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.n_m.append(self.n_m[0] - 1)
        for x in range(self.n_m[1]):
            self.edges.append([int(y) for y in input().split(" ")])

    def process_task(self):
        lens = [0] * self.n_m[0]
        graph = [[] for x in range(self.n_m[0])]
        for edge in self.edges:
            graph[edge[0] - 1].append(edge[1])
            graph[edge[1] - 1].append(edge[0])
            lens[edge[0] - 1] += 1
            lens[edge[1] - 1] += 1
        d = 1 + max(lens)
        to_visit = [(1, 1, d)]
        u = 2
        colors = [0] * self.n_m[0]
        while to_visit:
            visiting = to_visit.pop(-1)
            if not colors[visiting[0] - 1]:
                colors[visiting[0] - 1] = visiting[1]
                for g in graph[visiting[0] - 1]:
                    to_visit.append((g, u, visiting[1]))
                    u += 1
                    if u == visiting[2]:
                        u += 1
                    if u > d:
                        u = 1
                    if u == visiting[2]:
                        u += 1
        self.result = "{0}\n{1}".format(d, " ".join([str(x) for x in colors]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask780CSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
