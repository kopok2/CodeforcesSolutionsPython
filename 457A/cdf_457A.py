import math


def conv(x):
    res = 0
    q = (math.sqrt(5) + 1) / 2
    for i in range(len(x)):
        res += int(x[i]) * (q ** (len(x) - 1 - i))
    return res


class CodeforcesTask457ASolution:
    def __init__(self):
        self.result = ''
        self.first = ''
        self.second = ''

    def read_input(self):
        self.first = input()
        self.second = input()

    def process_task(self):
        a = conv(self.first)
        b = conv(self.second)
        if a > b:
            self.result = ">"
        elif a < b:
            self.result = "<"
        else:
            self.result = "="

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask457ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
