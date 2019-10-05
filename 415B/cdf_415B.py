import math


class CodeforcesTask415BSolution:
    def __init__(self):
        self.result = ''
        self.n_a_b = []
        self.tokens = []

    def read_input(self):
        self.n_a_b = [int(x) for x in input().split(" ")]
        self.tokens = [int(x) for x in input().split(" ")]

    def process_task(self):
        result = []
        for x in range(self.n_a_b[0]):
           result.append(((self.tokens[x] * self.n_a_b[1]) % self.n_a_b[2]) // self.n_a_b[1])
        self.result = " ".join([str(x) for x in result])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask415BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
