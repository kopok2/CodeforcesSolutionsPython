import math


class CodeforcesTask617ASolution:
    def __init__(self):
        self.result = ''
        self.x = 0

    def read_input(self):
        self.x = int(input())

    def process_task(self):
        steps = self.x // 5 + math.ceil(self.x % 5 / 5)
        self.result = str(steps)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask617ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
