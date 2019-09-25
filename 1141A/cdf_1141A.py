import math


class CodeforcesTask1141ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]

    def process_task(self):
        res = -1
        for a in range(int(math.log(self.n_m[1], 2)) + 1):
            for b in range(int(math.log(self.n_m[1], 3)) + 1):
                if self.n_m[0] * (2 ** a) * (3 ** b) == self.n_m[1]:
                    res = a + b
                    break
            if res != -1:
                break
        self.result = str(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1141ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
