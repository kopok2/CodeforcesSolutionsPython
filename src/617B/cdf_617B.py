from operator import mul
from functools import reduce


class CodeforcesTask617BSolution:
    def __init__(self):
        self.result = ''
        self.chocolate = []

    def read_input(self):
        input()
        self.chocolate = "".join(input().split(" "))

    def process_task(self):
        result = 1
        if self.chocolate.count("1") > 1:
            usefull_bar = self.chocolate.split("1", 1)[1][::-1].split("1", 1)[1][::-1]
            ways = [len(x) + 1 for x in usefull_bar.split("1")]
            result = reduce(mul, ways, 1)
        elif not self.chocolate.count("1"):
            result = 0
        self.result = str(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask617BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
