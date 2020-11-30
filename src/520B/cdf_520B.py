class CodeforcesTask520BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]

    def process_task(self):
        d = 20000
        graph = [set() for x in range(d)]
        for x in range(d):
            if (x + 1) * 2 < d:
                graph[x].add((x + 1) * 2)
            if x:
                graph[x].add(x)
        dists = [-1] * d
        to_visit = [(x, 1) for x in list(graph[self.n_m[0] - 1])]
        dists[self.n_m[0] - 1] = 0
        while to_visit:
            visiting = to_visit.pop(-1)
            if dists[visiting[0] - 1] == -1 or dists[visiting[0] - 1] > visiting[1]:
                dists[visiting[0] - 1] = visiting[1]
                to_visit += [(x, visiting[1] + 1) for x in list(graph[visiting[0] - 1])]
        self.result = str(dists[self.n_m[1] - 1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask520BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
