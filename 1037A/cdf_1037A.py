import math


class CodeforcesTask1037ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        res = 0
        while self.n >= 2 ** res:
            self.n -= 2 ** res
            res += 1
        if self.n:
            res += 1
        self.result = str(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1037ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
