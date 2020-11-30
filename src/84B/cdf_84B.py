import math


def choose(n, k):
    return n - k + 1


class CodeforcesTask84BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.array = []

    def read_input(self):
        self.n = int(input())
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        magic_arrays = 0
        cr = 10 ** 10
        cn = 0
        for a in self.array:
            if a == cr:
                cn += 1
            else:
                if cn:
                    for x in range(1, cn + 1):
                        magic_arrays += choose(cn, x)
                cr = a
                cn = 1
        for x in range(1, cn + 1):
            magic_arrays += choose(cn, x)
        self.result = str(int(magic_arrays))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask84BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
