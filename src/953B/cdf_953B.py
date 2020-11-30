from math import gcd
from functools import reduce


def find_gcd(list):
    x = reduce(gcd, list)
    return x


class CodeforcesTask953BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.sequence.sort()
        distances = [self.sequence[x + 1] - self.sequence[x] for x in range(self.n - 1)]
        min_dist = find_gcd(distances)
        min_add = (self.sequence[-1] - self.sequence[0]) // min_dist - self.n + 1
        self.result = str(min_add)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask953BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
