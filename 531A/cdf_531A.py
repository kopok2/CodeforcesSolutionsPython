import math


class CodeforcesTask531ASolution:
    def __init__(self):
        self.result = ''
        self.a_b_c = []

    def read_input(self):
        self.a_b_c = [int(x) for x in input().split(" ")]

    def process_task(self):
        delta = self.a_b_c[1] ** 2 - 4 * self.a_b_c[0] * self.a_b_c[2]
        x1 = (- self.a_b_c[1] + math.sqrt(delta)) / self.a_b_c[0] / 2
        x2 = (- self.a_b_c[1] - math.sqrt(delta)) / self.a_b_c[0] / 2
        if x1 == x2:
            solution = [x1]
        else:
            solution = [min(x1, x2), max(x1, x2)]
        self.result = " ".join([str(x) for x in solution])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask531ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
