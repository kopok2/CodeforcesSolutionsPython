from collections import deque


class CodeforcesTask580CSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.wrong = []
        self.edges = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.wrong = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0] - 1):
            self.edges.append([int(y) for y in input().split(" ")])

    def process_task(self):
        tree = [[] for x in range(self.n_m[0])]
        visited = [False for x in range(self.n_m[0])]
        for edge in self.edges:
            tree[edge[0] - 1].append(edge[1])
            tree[edge[1] - 1].append(edge[0])
        to_visit = deque([(x, (self.wrong[0] + 1) * self.wrong[x - 1]) for x in tree[0]])
        leaves = 0
        visited[0] = True
        while to_visit:
            visiting = to_visit.popleft()
            # print(visiting)
            if not visited[visiting[0] - 1]:
                visited[visiting[0] - 1] = True
                if 1 == len(tree[visiting[0] - 1]) and visiting[1] <= self.n_m[1]:
                    leaves += 1
                elif visiting[1] <= self.n_m[1]:
                    to_visit.extend([(x, (visiting[1] + 1) * self.wrong[x - 1]) for x in tree[visiting[0] - 1]])
        self.result = str(leaves)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask580CSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
