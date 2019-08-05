import math


class CodeforcesTask1080ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        mats = [x * self.n_k[0] for x in [2, 5, 8]]
        nbs = [x // self.n_k[1] + math.ceil(x % self.n_k[1] / self.n_k[1]) for x in mats]
        self.result = str(sum(nbs))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1080ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
