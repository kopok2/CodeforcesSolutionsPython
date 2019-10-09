class CodeforcesTask129BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.edges = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.edges.append([int(y) for y in input().split(" ")])

    def process_task(self):
        kicked = True
        kicked_cnt = 0
        graph = [set() for x in range(self.n_m[0])]
        for edge in self.edges:
            graph[edge[0] - 1].add(edge[1])
            graph[edge[1] - 1].add(edge[0])

        while kicked:
            kicked = False
            trm = []
            for x in range(self.n_m[0]):
                if len(graph[x]):
                    if len(graph[x]) == 1:
                        kicked = True
                        conn = graph[x].pop()
                        trm.append((conn - 1, x + 1))
            for tr in trm:
                if tr[1] in graph[tr[0]]:
                    graph[tr[0]].remove(tr[1])
            if kicked:
                kicked_cnt += 1

        self.result = str(kicked_cnt)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask129BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
