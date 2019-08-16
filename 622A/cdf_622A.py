import math


class CodeforcesTask622ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        n = int(math.sqrt(self.n))
        a = (n + n ** 2) / 2
        while a < self.n:
            n += 1
            a = (n + n ** 2) / 2
        n -= 1
        x = self.n - (n + n ** 2) / 2
        self.result = str(int(x))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask622ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
