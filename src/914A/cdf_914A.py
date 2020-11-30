import math


class CodeforcesTask914ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.array = []

    def read_input(self):
        self.n = int(input())
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        not_perfect_square = [x for x in [y for y in self.array if y >= 0] if not math.sqrt(x).is_integer()]
        not_perfect_square += [y for y in self.array if y < 0]
        not_perfect_square.sort(reverse=True)
        self.result = str(not_perfect_square[0])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask914ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
