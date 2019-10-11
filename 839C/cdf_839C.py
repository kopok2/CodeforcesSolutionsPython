from collections import deque


class CodeforcesTask839CSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.roads = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n - 1):
            self.roads.append([int(y) for y in input().split(" ")])

    def process_task(self):
        expected_value = 0.0
        graph = [[] for x in range(self.n)]
        for edge in self.roads:
            graph[edge[0] - 1].append(edge[1])
            graph[edge[1] - 1].append(edge[0])
        visited = [False] * self.n
        to_visit = deque([(1, 1, 0)])
        root = True
        while to_visit:
            visiting = to_visit.popleft()
            #print(visiting)
            if not visited[visiting[0] - 1]:
                visited[visiting[0] - 1] = True
                if len(graph[visiting[0] - 1]) == 1 and visited[graph[visiting[0] - 1][0] - 1]:
                    #print(visiting)
                    expected_value += visiting[1] * visiting[2]
                else:
                    l = len(graph[visiting[0] - 1]) - 1
                    if root:
                        l += 1
                    to_visit.extend([(x, visiting[1] / l, visiting[2] + 1) for x in graph[visiting[0] - 1]])
            root = False
        self.result = str(expected_value)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask839CSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
