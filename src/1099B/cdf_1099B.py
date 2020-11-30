import math


class CodeforcesTask1099BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        first = self.n / (math.ceil(math.sqrt(self.n)) ** 2)
        second = math.ceil(math.sqrt(self.n))
        #print(first, second, first * second)
        self.result = str(math.ceil(first * second + second))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1099BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
