from collections import deque


class CodeforcesTask1106DSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.edges = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.edges.append([int(y) for y in input().split(" ")])

    def process_task(self):
        graph = [[] for x in range(self.n_m[0])]
        for edge in self.edges:
            graph[edge[0] - 1].append(edge[1])
            graph[edge[0] - 1].append(edge[0])
        visited = [False] * self.n_m[0]
        visited[0] = True
        q = deque()
        s = []
        q.append(1)
        while q:
            now = q.pop()
            s.append(now)
            for g in graph[now - 1]:
                if not visited[g - 1]:
                    q.append(g)
                    visited[g - 1] = True
        self.result = " ".join([str(x) for x in list(s)])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1106DSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
