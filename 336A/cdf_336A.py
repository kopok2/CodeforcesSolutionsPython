import math


class CodeforcesTask336ASolution:
    def __init__(self):
        self.result = ''
        self.x_y = []

    def read_input(self):
        self.x_y = [int(x) for x in input().split(" ")]

    def process_task(self):
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0
        val = abs(self.x_y[0]) + abs(self.x_y[1])
        x1 = val * math.copysign(1, self.x_y[0])
        y2 = val * math.copysign(1, self.x_y[1])
        if x1 >= x2:
            swap = x2
            x2 = x1
            x1 = swap
            swap = y2
            y2 = y1
            y1 = swap
        self.result = "{} {} {} {}".format(int(x1), int(y1), int(x2), int(y2))


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask336ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
