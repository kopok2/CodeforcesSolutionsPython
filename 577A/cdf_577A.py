import math


def factors(x):
    result = set()
    for y in range(1, int(math.sqrt(x)) + 1):
        if not x % y:
            result.add(y)
            result.add(x // y)
    return list(result)


class CodeforcesTask577ASolution:
    def __init__(self):
        self.result = ''
        self.n_x = []

    def read_input(self):
        self.n_x = [int(x) for x in input().split(" ")]

    def process_task(self):
        in_table = 0
        num_factors = factors(self.n_x[1])
        for fac in num_factors:
            if fac <= self.n_x[0] and self.n_x[1] // fac <= self.n_x[0]:
                in_table += 1
        self.result = str(in_table)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask577ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
