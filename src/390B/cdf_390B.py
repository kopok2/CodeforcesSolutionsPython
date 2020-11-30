import math


class CodeforcesTask390BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.a = []
        self.b = []

    def read_input(self):
        self.n = int(input())
        self.a = [int(x) for x in input().split(" ")]
        self.b = [int(x) for x in input().split(" ")]

    def process_task(self):
        joy = 0
        for note in range(self.n):
            if self.a[note] * 2 < self.b[note] or self.b[note] == 1:
                joy -= 1
            else:
                if not self.b[note] % 2:
                    joy += (self.b[note] // 2) ** 2
                else:
                    joy += ((self.b[note] // 2) * (self.b[note] // 2 + 1))
        self.result = str(joy)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask390BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
