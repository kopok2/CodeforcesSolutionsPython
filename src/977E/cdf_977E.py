from collections import deque


class CodeforcesTask977ESolution:
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
        lens = [0] * self.n_m[0]
        for edge in self.edges:
            graph[edge[0] - 1].append(edge[1])
            graph[edge[1] - 1].append(edge[0])
            lens[edge[0] - 1] += 1
            lens[edge[1] - 1] += 1
        comp_cnt = 0
        component = [0] * self.n_m[0]
        for x in range(self.n_m[0]):
            if not component[x]:
                comp_cnt += 1
                to_visit = deque([x + 1])
                while to_visit:
                    visiting = to_visit.popleft()
                    if not component[visiting - 1]:
                        component[visiting - 1] = comp_cnt
                        for g in graph[visiting - 1]:
                            if not component[g - 1]:
                                to_visit.append(g)
        can_be = [1] * comp_cnt
        for x in range(self.n_m[0]):
            if lens[x] != 2:
                can_be[component[x] - 1] = 0
        self.result = str(sum(can_be))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask977ESolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
