import math


class CodeforcesTask304ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        trs = 0
        for c in range(1, self.n + 1):
            for b in range(1, c):
                a = math.sqrt(c ** 2 - b ** 2)
                if (a).is_integer() and a <= b:
                    trs += 1
        self.result = str(trs)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask304ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
