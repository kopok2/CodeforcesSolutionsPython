import math


def in_crust(x, y, s, d, r):
    return r - d <= math.sqrt(x ** 2 + y ** 2) - s and math.sqrt(x ** 2 + y ** 2) + s <= r


class CodeforcesTask842BSolution:
    def __init__(self):
        self.result = ''
        self.r_d = []
        self.n = 0
        self.circles = []

    def read_input(self):
        self.r_d = [int(x) for x in input().split(" ")]
        self.n = int(input())
        for x in range(self.n):
            self.circles.append([int(y) for y in input().split(" ")])

    def process_task(self):
        is_ = [1 if in_crust(cru[0], cru[1], cru[2], self.r_d[1], self.r_d[0]) else 0 for cru in self.circles]
        self.result = str(sum(is_))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask842BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
