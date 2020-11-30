class CodeforcesTask791BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.connections = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.connections.append([int(y) for y in input().split(" ")])

    def process_task(self):
        graph = [[] for x in range(self.n_m[0])]

        for conn in self.connections:
            graph[conn[0] - 1].append(conn[1])
            graph[conn[1] - 1].append(conn[0])
        ld = [len(g) for g in graph]
        visited = set()
        reason = True
        for x in range(self.n_m[0]):
            if x + 1 not in visited:
                visited.add(x + 1)
                for neighbour in list(graph[x]):
                    visited.add(neighbour)
                    if ld[neighbour - 1] != ld[x]:
                        reason = False
                        break
                if not reason:
                    break
            if not reason:
                break
        self.result = "YES" if reason else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask791BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
