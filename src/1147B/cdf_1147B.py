import math


class CodeforcesTask1147BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.points = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.points.append([int(y) for y in input().split(" ")])

    def process_task(self):
        can = False
        segm = {}
        for point in self.points:
            segm["{0}_{1}".format(*point)] = True
            segm["{1}_{0}".format(*point)] = True
        for k in range(1, self.n_m[0]):
            if not self.n_m[0] % k:
                #print(k)
                do = True
                for p in self.points:
                    a, b = (p[0] + k) % self.n_m[0], (p[1] + k) % self.n_m[0]
                    if not a:
                        a = self.n_m[0]
                    if not b:
                        b = self.n_m[0]
                    if not "{0}_{1}".format(a, b) in segm:
                        do = False
                        break
                if do:
                    can = do
                    break
        self.result = "Yes" if can else "No"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1147BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
