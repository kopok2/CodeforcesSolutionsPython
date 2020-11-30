from fractions import Fraction


class CodeforcesTask197BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.p_x = []
        self.q_x = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.p_x = [int(x) for x in input().split(" ")]
        self.q_x = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.n_m[0] > self.n_m[1]:
            if self.p_x[0] * self.q_x[0] > 0:
                self.result = "Infinity"
            else:
                self.result = "-Infinity"
        elif self.n_m[1] > self.n_m[0]:
            self.result = "0/1"
        else:
            result = Fraction(self.p_x[0], self.q_x[0])
            self.result = "{0}/{1}".format(result.numerator, result.denominator)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask197BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
