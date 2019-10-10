class CodeforcesTask862BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.tree = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n - 1):
            self.tree.append([int(y) for y in input().split(" ")])

    def process_task(self):
        graph = [[] for x in range(self.n)]
        label = [0] * (self.n )
        for edge in self.tree:
            graph[edge[0] - 1].append(edge[1])
            graph[edge[1] - 1].append(edge[0])
        to_visit = [(1, True)]
        while to_visit:
            visiting = to_visit.pop(-1)
            if label[visiting[0] - 1] == 0:
                label[visiting[0] - 1] = visiting[1]
                to_visit += [(x, not visiting[1]) for x in graph[visiting[1] - 1]]
        b1 = label.count(True)
        b2 = label.count(False)
        self.result = str(b1 * b2 - self.n + 1)



    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask862BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
