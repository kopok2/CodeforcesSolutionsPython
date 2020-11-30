class CodeforcesTask893CSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.costs = []
        self.connections = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.costs = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.connections.append([int(y) for y in input().split(" ")])

    def process_task(self):
        graph = [[] for x in range(self.n_m[0])]
        for conn in self.connections:
            graph[conn[0] - 1].append(conn[1])
            graph[conn[1] - 1].append(conn[0])
        comp_cnt = 0
        comp_costs = []
        component = [0] * self.n_m[0]
        for x in range(self.n_m[0]):
            if not component[x]:
                comp_cnt += 1
                mn = 10 ** 10
                to_visit = [x + 1]
                while to_visit:
                    visiting = to_visit.pop(-1)
                    if not component[visiting - 1]:
                        component[visiting - 1] = comp_cnt
                        to_visit += graph[visiting - 1]
                        mn = min(mn, self.costs[visiting - 1])
                comp_costs.append(mn)
        self.result = str(sum(comp_costs))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask893CSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
