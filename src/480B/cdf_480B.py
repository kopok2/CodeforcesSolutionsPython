class CodeforcesTask480BSolution:
    def __init__(self):
        self.result = ''
        self.n_l_x_y = []
        self.ruler = []

    def read_input(self):
        self.n_l_x_y = [int(x) for x in input().split(" ")]
        self.ruler = [int(x) for x in input().split(" ")]

    def process_task(self):
        dists = {}
        for a in self.ruler:
            dists[a] = True
        hasx = False
        hasy = False
        for a in self.ruler:
            try:
                if dists[a - self.n_l_x_y[2]]:
                    hasx = True
            except KeyError:
                pass
            try:
                if dists[a + self.n_l_x_y[2]]:
                    hasx = True
            except KeyError:
                pass
            try:
                if dists[a - self.n_l_x_y[3]]:
                    hasy = True
            except KeyError:
                pass
            try:
                if dists[a - self.n_l_x_y[3]]:
                    hasy = True
            except KeyError:
                pass
            if hasx and hasy:
                break
        if hasx and hasy:
            self.result = "0"
        elif hasx:
            self.result = "1\n{0}".format(self.n_l_x_y[3])
        elif hasy:
            self.result = "1\n{0}".format(self.n_l_x_y[2])
        else:
            res = [0, 0]
            sgn = False
            dst = self.n_l_x_y[2] + self.n_l_x_y[3]
            diff = self.n_l_x_y[3] - self.n_l_x_y[2]
            for a in self.ruler:
                try:
                    if dists[a - dst]:
                        if a - self.n_l_x_y[2] > 0:
                            sgn = True
                            res = a - self.n_l_x_y[2]
                except KeyError:
                    pass
                try:
                    if dists[a + dst]:
                        if a + self.n_l_x_y[2] < self.n_l_x_y[1]:
                            sgn = True
                            res = a + self.n_l_x_y[2]
                except KeyError:
                    pass
                try:
                    if dists[a - diff]:
                        if a + self.n_l_x_y[2] < self.n_l_x_y[1]:
                            sgn = True
                            res = a + self.n_l_x_y[2]
                except KeyError:
                    pass
                try:
                    if dists[a + diff]:
                        if a - self.n_l_x_y[2] > 0:
                            sgn = True
                            res = a - self.n_l_x_y[2]
                except KeyError:
                    pass
                if sgn:
                    break
            if sgn:
                self.result = "1\n{0}".format(res)
            else:
                self.result = "2\n{0} {1}".format(self.n_l_x_y[2], self.n_l_x_y[3])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask480BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
