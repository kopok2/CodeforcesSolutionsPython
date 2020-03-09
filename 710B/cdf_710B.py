import math


class CodeforcesTask710BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.numbers = []

    def read_input(self):
        self.n = int(input())
        self.numbers = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.numbers.sort()
        if self.n % 2:
            self.result = self.numbers[self.n // 2]
        else:
            self.result = self.numbers[self.n // 2  - 1]
            #self.result = (self.numbers[self.n // 2 - 1] + self.numbers[self.n // 2]) // 2

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask710BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
