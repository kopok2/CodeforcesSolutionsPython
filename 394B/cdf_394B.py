from fractions import Fraction


class CodeforcesTask394BSolution:
    def __init__(self):
        self.result = ''
        self.p_x = []

    def read_input(self):
        self.p_x = [int(x) for x in input().split(" ")]

    def process_task(self):
        params = [x for x in range(1, 10)]
        ys = []
        for d in params:
            a = Fraction(10)
            b = Fraction(self.p_x[0] - 1)
            c = Fraction(1, 10)
            e = Fraction(self.p_x[1])
            f = Fraction(1, 10)
            g = a ** b
            h = g - c
            i = h * d
            j = e - f
            k = i / j
            ys.append(k)
        ys = [y for y in ys if len(str(y)) == self.p_x[0]]

        try:
            print(min(ys))
        except ValueError:
            self.result = "Impossible"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask394BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
