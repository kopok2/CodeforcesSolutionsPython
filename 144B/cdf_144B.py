import math


def dist(a, b, c, d):
    return math.sqrt((a - c) ** 2 + (b - d) ** 2)


class CodeforcesTask144BSolution:
    def __init__(self):
        self.result = ''
        self.x_y_x_y = []
        self.n = 0
        self.radiators = []

    def read_input(self):
        self.x_y_x_y = [int(x) for x in input().split(" ")]
        self.n = int(input())
        for x in range(self.n):
            self.radiators.append([int(y) for y in input().split(" ")])

    def process_task(self):
        generals = []
        self.x_y_x_y[0], self.x_y_x_y[2] = min(self.x_y_x_y[0], self.x_y_x_y[2]), max(self.x_y_x_y[0], self.x_y_x_y[2])
        self.x_y_x_y[1], self.x_y_x_y[3] = min(self.x_y_x_y[1], self.x_y_x_y[3]), max(self.x_y_x_y[1], self.x_y_x_y[3])
        for x in range(self.x_y_x_y[0], self.x_y_x_y[2] + 1):
            generals.append((x, self.x_y_x_y[1]))
            generals.append((x, self.x_y_x_y[3]))
        for y in range(self.x_y_x_y[1] + 1, self.x_y_x_y[3]):
            generals.append((self.x_y_x_y[0], y))
            generals.append((self.x_y_x_y[2], y))
        for radiator in self.radiators:
            ngen = []
            if generals:
                while generals:
                    checking = generals.pop(-1)
                    if dist(radiator[0], radiator[1], *checking) > radiator[2]:
                        ngen.append(checking)
                generals = ngen
            else:
                break
        self.result = str(len(generals))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask144BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
