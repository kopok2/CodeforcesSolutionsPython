import math


class CodeforcesTask1032ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.utens = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.utens = [int(x) for x in input().split(" ")]

    def process_task(self):
        cnts = [self.utens.count(x) for x in list(set(self.utens))]
        all = len(set(self.utens)) * math.ceil(max(cnts) / self.n_k[1]) * self.n_k[1]
        missing = all - sum(cnts)
        self.result = str(missing)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1032ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
