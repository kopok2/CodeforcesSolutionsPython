from collections import deque


class CodeforcesTask1167CSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.groups = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.groups.append([int(y) for y in input().split(" ")][1:])

    def process_task(self):
        graph = [[] for x in range(self.n_m[0] + self.n_m[1])]
        for x in range(self.n_m[1]):
            for member in self.groups[x]:
                graph[member - 1].append(self.n_m[0] + x + 1)
                graph[self.n_m[0] + x].append(member)
        comp_cnt = 0
        component = [0] * (self.n_m[0] + self.n_m[1])
        for x in range(self.n_m[0]):
            if not component[x]:
                comp_cnt += 1
                component[x] = comp_cnt
                to_visit = deque(graph[x])
                while to_visit:
                    visiting = to_visit.pop()
                    if not component[visiting - 1]:
                        component[visiting - 1] = comp_cnt
                        for a in graph[visiting - 1]:
                            if len(graph[a - 1]) > 1:
                                to_visit.append(a)
                            else:
                                component[a - 1] = comp_cnt
        counts = [0] * comp_cnt
        for a in component[:self.n_m[0]]:
            counts[a - 1] += 1

        self.result = " ".join([str(counts[x - 1]) for x in component[:self.n_m[0]]])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1167CSolution()
    Solution.read_input()
    Solution.process_task()
    import os
    os.write(1, bytes(Solution.get_result(), "utf-8"))
