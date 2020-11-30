import math


class CodeforcesTask514BSolution:
    def __init__(self):
        self.result = ''
        self.n_x_y = []
        self.troopers = []

    def read_input(self):
        self.n_x_y = [int(x) for x in input().split(" ")]
        for x in range(self.n_x_y[0]):
            self.troopers.append([int(y) for y in input().split(" ")])

    def process_task(self):
        shots = 0
        troops = set()
        for trooper in self.troopers:
            troops.add(" ".join([str(x) for x in trooper]))
        while troops:
            shooting = troops.pop()
            shots += 1
            direction = [int(x) for x in shooting.split(" ")]
            vector = [self.n_x_y[1] - direction[0], self.n_x_y[2] - direction[1]]
            d = int(math.gcd(*vector))
            vector = [vector[0] // d, vector[1] // d]
            uvector = [-vector[0], -vector[1]]
            x, y = self.n_x_y[1:]
            while -10000 <= x <= 10000 and -10000 <= y <= 10000:
                t = "{0} {1}".format(x, y)
                if t in troops:
                    troops.remove(t)
                x += vector[0]
                y += vector[1]
            x, y = self.n_x_y[1:]
            while -10000 <= x <= 10000 and -10000 <= y <= 10000:
                t = "{0} {1}".format(x, y)
                if t in troops:
                    troops.remove(t)
                x += uvector[0]
                y += uvector[1]
        self.result = str(shots)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask514BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
