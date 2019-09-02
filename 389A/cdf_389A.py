from math import gcd
from functools import reduce


def find_gcd(l):
    x = reduce(gcd, l)
    return x



class CodeforcesTask389ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.nums = []

    def read_input(self):
        self.n = int(input())
        self.nums = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.result = str(self.n * find_gcd(self.nums))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask389ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
