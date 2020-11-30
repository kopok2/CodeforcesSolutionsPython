class CodeforcesTask574BSolution:
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
        mn = self.n_m[0] ** 2
        found = False
        for first in range(self.n_m[0]):
            for second in list(graph[first - 1]):
                for third in list(graph[first - 1]):
                    if second != third and third in graph[second - 1]:
                        found = True
                        mn = min(mn, len(graph[first - 1]) + len(graph[second - 1]) + len(graph[third - 1]) - 6)

        self.result = "-1" if not found else str(mn)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask574BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
