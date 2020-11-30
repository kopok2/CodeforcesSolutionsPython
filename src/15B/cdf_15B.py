class CodeforcesTask15BSolution:
    def __init__(self):
        self.result = ''
        self.t = 0
        self.tests = []

    def read_input(self):
        self.t = int(input())
        for x in range(self.t):
            self.tests.append([int(y) for y in input().split(" ")])

    def process_task(self):
        results = []
        for test in self.tests:
            vert = abs(test[3] - test[5])
            hori = abs(test[2] - test[4])
            if vert * 2 <= test[1]:
                vert_unr = 0
            else:
                vert_unr = 2 * vert - test[1]
            if hori * 2 <= test[0]:
                hori_unr = 0
            else:
                hori_unr = 2 * hori - test[0]
            unr = test[0] * vert_unr + test[1] * hori_unr - hori_unr * vert_unr
            unr += 2 * (vert - vert_unr) * (hori - hori_unr)
            results.append(unr)

        self.result = "\n".join([str(x) for x in results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask15BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
