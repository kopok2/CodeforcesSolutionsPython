import math

def sum_before(x):
    result = 0
    for y in range(x):
        result += 5 * 2 ** y
    return result


class CodeforcesTask82ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
        x = 0
        while sum_before(x) < self.n:
            x += 1
        self.result = names[math.ceil((self.n - sum_before(x - 1)) / 2 ** (x - 1)) -  1]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask82ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
