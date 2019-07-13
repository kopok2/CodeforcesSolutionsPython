class CodeforcesTask476ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]

    def process_task(self):
        sols = []
        for m in range(1, self.n_m[0] // self.n_m[1] + 1):
            #print(m)
            a = self.n_m[0] - m * self.n_m[1]
            b = self.n_m[1] * m - a
            #print(a, b, 2 * a + b)
            if a >= 0 and b >= 0:
                if 2 * a + b == self.n_m[0]:
                    sols.append(a + b)
        if sols:
            self.result = str(min(sols))
        else:
            self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask476ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
