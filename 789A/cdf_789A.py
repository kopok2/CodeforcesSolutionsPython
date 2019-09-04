import math


class CodeforcesTask789ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.w = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.w = [int(x) for x in input().split(" ")]

    def process_task(self):
        pockets = [math.ceil(x / self.n_k[1]) for x in self.w]
        self.result = str(int(math.ceil(sum(pockets) / 2)))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask789ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
