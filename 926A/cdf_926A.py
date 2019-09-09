import math


class CodeforcesTask926ASolution:
    def __init__(self):
        self.result = ''
        self.l_r = []

    def read_input(self):
        self.l_r = [int(x) for x in input().split(" ")]

    def process_task(self):
        x = 0
        y = 0
        cnt23 = 0
        for a in range(int(max(0.0, math.log(self.l_r[1], 2) + 2))):
            for b in range(int(max(0.0, math.log(self.l_r[1], 3) + 2))):
                if self.l_r[0] <= (2 ** a) * (3 ** b) <= self.l_r[1]:
                    cnt23 += 1
        self.result = str(cnt23)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask926ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
