import math


class CodeforcesTask388ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.boxes = []

    def read_input(self):
        self.n = int(input())
        self.boxes = [int(x) for x in input().split(" ")]

    def process_task(self):
        counts = [self.boxes.count(x) for x in range(max(self.boxes) + 1)]
        constraints = [math.ceil(sum(counts[0:x + 1]) / (x + 1)) for x in range(len(counts))]
        self.result = str(max(constraints))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask388ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
