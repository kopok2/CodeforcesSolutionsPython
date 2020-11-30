import math


class CodeforcesTask1023BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.n_k[1] == self.n_k[0]:
            ways = math.ceil((self.n_k[0] * 2 - self.n_k[1]) / 2) - 1
        elif self.n_k[1] < self.n_k[0] + 1:
            ways = math.ceil(self.n_k[1] / 2) - 1
        else:
            ways = math.ceil((self.n_k[0] * 2 - self.n_k[1]) / 2)
        self.result = str(max(0, ways))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1023BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
