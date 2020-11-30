class CodeforcesTask946BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]

    def process_task(self):
        a, b = self.n_m
        while True:
            if not a or not b:
                break
            elif a >= 2 * b:
                a -= (a // (2 * b)) * 2 * b
            elif b >= 2 * a:
                b -= (b // (2 * a)) * 2 * a
            else:
                break
        self.result = "{0} {1}".format(a, b)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask946BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
