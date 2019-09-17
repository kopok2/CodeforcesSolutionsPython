import math


class CodeforcesTask552BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        z = 0
        for k in range(int(math.floor(math.log10(self.n)))):
            z += 9 * (10 ** k) * (k + 1)
        z += (1 + self.n - (10 ** int(math.floor(math.log10(self.n))))) * len(str(self.n))
        self.result = str(z)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask552BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
