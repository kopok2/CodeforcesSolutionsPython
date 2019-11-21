from collections import deque


class CodeforcesTask1006ESolution:
    def __init__(self):
        self.result = ''
        self.n_q = []
        self.command = []
        self.queries = []

    def read_input(self):
        self.n_q = [int(x) for x in input().split(" ")]
        self.command = [int(x) for x in input().split(" ")]
        for _ in range(self.n_q[1]):
            self.queries.append([int(x) for x in input().split(" ")])

    def process_task(self):
        tree = [[] for _ in range(self.n_q[0])]
        for x in range(1, self.n_q[0]):
            tree[self.command[x - 1] - 1].append(x + 1)
        starts = {}
        stops = {}
        called = []
        to_visit = deque([1, -1])
        while to_visit:
            visiting = to_visit.popleft()
            if visiting < 0:
                stops[abs(visiting)] = len(called)
            else:
                called.append(visiting)
                starts[visiting] = len(called)
                n = sorted(tree[visiting - 1], reverse=True)
                to_visit.appendleft(-visiting)
                for a in n:
                   to_visit.appendleft(a)
        ranges = [stops[x] - starts[x] + 1 for x in range(1, self.n_q[0] + 1)]
        for query in self.queries:
            if ranges[query[0] - 1] >= query[1]:
                print(called[starts[query[0]] + query[1] - 2])
            else:
                print('-1')


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1006ESolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
