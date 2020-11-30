class CodeforcesTask292BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.connections = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.connections.append([int(y) for y in input().split(" ")])

    def process_task(self):
        graph = [set() for x in range(self.n_m[0])]
        for conn in self.connections:
            graph[conn[0] - 1].add(conn[1])
            graph[conn[1] - 1].add(conn[0])
        conn_cnt = [len(a) for a in graph]
        if conn_cnt.count(1) == 2 and conn_cnt.count(2) == self.n_m[0] - 2:
            self.result = "bus topology"
        elif conn_cnt.count(1) == self.n_m[0] - 1 and conn_cnt.count(self.n_m[0] - 1) == 1:
            self.result = "star topology"
        elif conn_cnt.count(2) == self.n_m[0]:
            self.result = "ring topology"
        else:
            self.result = "unknown topology"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask292BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
