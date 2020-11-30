class CodeforcesTask334BSolution:
    def __init__(self):
        self.result = ''
        self.points = []

    def read_input(self):
        for x in range(8):
            self.points.append([int(x) for x in input().split(" ")])

    def process_task(self):
        xs = [x[0] for x in self.points]
        xs.sort()
        ys = [x[1] for x in self.points]
        ys.sort()
        if xs[0] == xs[1] == xs[2] < xs[3] == xs[4] < xs[5] == xs[6] == xs[7] and \
                ys[0] == ys[1] == ys[2] < ys[3] == ys[4] < ys[5] == ys[6] == ys[7] and \
                not sum([1 if self.points.count(x) > 1 else 0 for x in self.points]):
            self.result = "respectable"
        else:
            self.result = "ugly"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask334BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
