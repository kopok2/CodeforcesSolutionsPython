import math


class CodeforcesTask47ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        x = (-1 + math.sqrt(1+8*self.n)) / 2
        if x.is_integer():
            self.result = "YES"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask47ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
