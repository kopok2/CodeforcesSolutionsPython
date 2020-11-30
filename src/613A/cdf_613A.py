import math


def dist(a, b, c, d):
    return math.sqrt((a - c) ** 2 + (b - d) ** 2)


class CodeforcesTask613ASolution:
    def __init__(self):
        self.result = ''
        self.n_p = []
        self.points = []

    def read_input(self):
        self.n_p = [int(x) for x in input().split(" ")]
        for x in range(self.n_p[0]):
            self.points.append([int(y) for y in input().split(" ")])

    def process_task(self):
        rs = [dist(self.n_p[1], self.n_p[2], x[0], x[1]) for x in self.points]
        mr = min(rs)
        xr = max(rs)
        self.result = str(math.pi * (xr ** 2) - math.pi * (mr ** 2))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask613ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
