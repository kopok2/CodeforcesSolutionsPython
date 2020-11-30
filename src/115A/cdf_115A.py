class CodeforcesTask115ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.superior = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.superior.append(int(input()))

    def process_task(self):
        graph = [[[], 1] for x in range(self.n)]
        for x in range(self.n):
            if self.superior[x] > 0:
                graph[self.superior[x] - 1][0].append(x + 1)
        for x in range(self.n):
            if graph[x][1] == 1:
                to_visit = [(y, graph[x][1] + 1) for y in graph[x][0]]
                while to_visit:
                    visiting = to_visit.pop(-1)
                    graph[visiting[0] - 1][1] = max(graph[visiting[0] - 1][1], visiting[1])
                    for nxt in graph[visiting[0] - 1][0]:
                        to_visit.append((nxt, visiting[1] + 1))
        levels = [x[1] for x in graph]
        self.result = str(max(levels))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask115ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
