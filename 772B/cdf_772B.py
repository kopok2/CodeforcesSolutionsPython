import math


def dist(a, b, c, d):
    return math.sqrt((a - c) ** 2 + (b - d) ** 2)


class CodeforcesTask772BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.points = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.points.append([int(y) for y in input().split(" ")])

    def process_task(self):
        radiuses = []
        for x in range(self.n):
            x1 = x
            x2 = x + 1
            x3 = x + 2
            if x2 == self.n:
                x2 = 0
                x3 = 1
            elif x2 == self.n - 1:
                x3 = 0
            p1 = self.points[x1]
            p2 = self.points[x2]
            p3 = self.points[x3]
            if not p3[0] - p1[0]:
                radiuses.append(abs(p3[0] - p2[0]) / 2)
            elif not p3[1] - p1[1]:
                radiuses.append(abs(p3[1] - p2[1]) / 2)
            else:
                a = (p3[1] - p1[1]) / (p3[0] - p1[0])
                b = p1[1] - p1[0] * a
                d = p2[1] + a * p2[0]
                x4 = (d - b) / (2 * a)
                y4 = x4 * a + b
                radiuses.append(dist(x4, y4, p2[0], p2[1]) / 2)
        self.result = str(min(radiuses))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask772BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
