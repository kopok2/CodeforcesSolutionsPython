class CodeforcesTask596ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.points = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.points.append([int(y) for y in input().split(" ")])

    def process_task(self):
        if self.n < 2:
            self.result = "-1"
        elif self.n == 2:
            if self.points[0][0] != self.points[1][0] and self.points[0][1] != self.points[1][1]:
                self.result = str(abs(self.points[0][0] - self.points[1][0]) * abs(self.points[1][1] - self.points[0][1]))
            else:
                self.result = "-1"
        else:
            xs = [x[0] for x in self.points]
            ys = [x[1] for x in self.points]
            xs.sort()
            ys.sort()
            self.result = str(abs(xs[0] - xs[-1]) * abs(ys[0] - ys[-1]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask596ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
