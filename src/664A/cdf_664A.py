import math


class CodeforcesTask664ASolution:
    def __init__(self):
        self.result = ''
        self.a_b = []

    def read_input(self):
        self.a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.result = "1" if self.a_b[0] != self.a_b[1] else str(self.a_b[0])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask664ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
