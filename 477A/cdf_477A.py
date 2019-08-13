from fractions import Fraction


class CodeforcesTask477ASolution:
    def __init__(self):
        self.result = ''
        self.a_b = []

    def read_input(self):
        self.a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        a = Fraction(self.a_b[0], 1)
        b = Fraction(self.a_b[1], 1)
        ff = Fraction(1_000_000_007, 1)
        B = (b * (b - 1) / 2) % ff
        A1 = (a * (a + 1) / 2) % ff
        A = (A1 * b + a) % ff
        ss = (A * B) % ff
        self.result = str(int(ss))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask477ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
