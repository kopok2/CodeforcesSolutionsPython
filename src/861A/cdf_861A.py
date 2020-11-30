import math


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


class CodeforcesTask861ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.result = str(lcm(self.n_k[0], 10 ** self.n_k[1]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask861ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
