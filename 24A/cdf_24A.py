class CodeforcesTask24ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.roads = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.roads.append([int(y) for y in input().split(" ")])

    def process_task(self):
        connections = [[] for x in range(self.n)]
        costs = {}
        for road in self.roads:
            r_name = "{0}_{1}".format(road[0], road[1])
            r_name_alt = "{1}_{0}".format(road[0], road[1])
            costs[r_name] = 0
            costs[r_name_alt] = road[2]
            connections[road[0] - 1].append(road[1])
            connections[road[1] - 1].append(road[0])
        to_visit = [1]
        visited = []
        cost = 0
        visiting = 1
        while to_visit:
            visiting = to_visit.pop(0)
            visited.append(visiting)
            if connections[visiting - 1][0] not in visited:
                to_visit.append(connections[visiting - 1][0])
                cost += costs["{0}_{1}".format(visiting, to_visit[-1])]
            elif connections[visiting - 1][1] not in visited:
                to_visit.append(connections[visiting - 1][1])
                cost += costs["{0}_{1}".format(visiting, to_visit[-1])]
        cost += costs["{0}_1".format(visiting)]
        cost2 = sum([x[2] for x in self.roads]) - cost
        self.result = str(min(cost, cost2))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask24ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
