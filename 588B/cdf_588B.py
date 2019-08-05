import math


def is_lovely(x):
    for y in range(2, int(math.sqrt(x)) + 1):
        if not x % (y ** 2):
            return False
    return True


class CodeforcesTask588BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        if is_lovely(self.n):
            self.result = self.n
        else:
            result = 1
            for x in range(1, int(math.sqrt(self.n)) + 2):
                if not self.n % x:
                    #print(x, result, x * result)
                    if is_lovely(x * result):
                        result *= x
                    if is_lovely(result * (self.n // x)):
                        result *= self.n // x
            self.result = str(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask588BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
