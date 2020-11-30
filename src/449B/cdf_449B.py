class CodeforcesTask449BSolution:
    def __init__(self):
        self.result = ''
        self.n_m_k = []
        self.roads = []
        self.trains = []

    def read_input(self):
        self.n_m_k = [int(x) for x in input().split(" ")]
        for x in range(self.n_m_k[1]):
            self.roads.append([int(y) for y in input().split(" ")])
        for x in range(self.n_m_k[2]):
            self.trains.append([int(y) for y in input().split(" ")])

    def process_task(self):
        adj = [[] for x in range(self.n_m_k[0])]
        dist = [-1] * self.n_m_k[0]
        for road in self.roads:
            adj[road[0] - 1].append((road[1], road[2]))
            adj[road[1] - 1].append((road[0], road[2]))
        to_visit = [(1, 0)]
        while to_visit:
            visiting = to_visit.pop(-1)
            if dist[visiting[0] - 1] == -1 or dist[visiting[0] - 1] > visiting[1]:
                dist[visiting[0] - 1] = visiting[1]
                for a in adj[visiting[0] - 1]:
                    to_visit.append((a[0], a[1] + visiting[1]))
        open_trains = [0] * self.n_m_k[0]
        for train in self.trains:
            if dist[train[0] - 1] > train[1]:
                open_trains[train[0] - 1] = 1
        closed = max(0, self.n_m_k[2] - sum(open_trains))
        self.result = str(closed)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask449BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
