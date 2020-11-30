from math import gcd
from functools import reduce


def find_gcd(l):
    x = reduce(gcd, l)
    return x



class CodeforcesTask926BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.points = []

    def read_input(self):
        self.n = int(input())
        self.points = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.points.sort()
        dists = [self.points[x] - self.points[x - 1] for x in range(1, self.n)]
        should_dist = int(find_gcd(dists))
        cnt = (self.points[-1] - self.points[0]) // should_dist - self.n + 1
        self.result = str(cnt)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask926BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
