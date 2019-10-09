class CodeforcesTask707BSolution:
    def __init__(self):
        self.result = ''
        self.n_m_k = []
        self.roads = []
        self.storages = []

    def read_input(self):
        self.n_m_k = [int(x) for x in input().split(" ")]
        for x in range(self.n_m_k[1]):
            self.roads.append([int(y) for y in input().split(" ")])
        if self.n_m_k[2]:
            self.storages = [int(x) for x in input().split(" ")]

    def process_task(self):
        graph = [[] for x in range(self.n_m_k[0])]
        for road in self.roads:
            graph[road[0] - 1].append((road[1], road[2]))
            graph[road[1] - 1].append((road[0], road[2]))
        bakeries = {}
        store_locs = set(self.storages)
        for store in self.storages:
            for loc in graph[store - 1]:
                if loc[0] not in store_locs:
                    if loc[0] in bakeries:
                        bakeries[loc[0]] = min(bakeries[loc[0]], loc[1])
                    else:
                        bakeries[loc[0]] = loc[1]
        mn = 10 ** 10
        if len(bakeries):
            for key, value in bakeries.items():
                mn = min(mn, value)
        else:
            mn = -1
        self.result = str(mn)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask707BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
