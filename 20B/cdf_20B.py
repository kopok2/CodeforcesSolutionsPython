class CodeforcesTask20BSolution:
    def __init__(self):
        self.result = ''
        self.a_b_c = []

    def read_input(self):
        self.a_b_c = [int(x) for x in input().split(" ")]

    def process_task(self):
        if not self.a_b_c[0]:
            if not self.a_b_c[1]:
                if not self.a_b_c[2]:
                    self.result = "-1"
                else:
                    self.result = "0"
            else:
                self.result = "1\n{0:.6f}".format(-self.a_b_c[2] / self.a_b_c[1])
        else:
            delta = self.a_b_c[1] ** 2 - 4 * self.a_b_c[0] * self.a_b_c[2]
            if not delta:
                import math
                root = math.sqrt(self.a_b_c[2] / self.a_b_c[0])
                if self.a_b_c[0] * (root ** 2) + self.a_b_c[1] * root + self.a_b_c[2] != 0:
                    root = -root
                self.result = "1\n{0:.6f}".format(root)
            elif delta < 0:
                self.result = "0"
            else:
                import math
                s_delta = math.sqrt(delta)
                roots = [(-self.a_b_c[1] - s_delta) / (2 * self.a_b_c[0]), (-self.a_b_c[1] + s_delta) / (2 * self.a_b_c[0])]
                roots.sort()
                self.result = "2\n{0:.6f}\n{1:.6f}".format(roots[0], roots[1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask20BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
