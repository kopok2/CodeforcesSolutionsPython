class CodeforcesTask676BSolution:
    def __init__(self):
        self.result = ''
        self.n_t = []

    def read_input(self):
        self.n_t = [int(x) for x in input().split(" ")]

    def process_task(self):
        glasses = [[0.0] * (x + 1) for x in range(self.n_t[0])]
        for s in range(self.n_t[1]):
            glasses[0][0] += 1.0
            for x in range(self.n_t[0] - 1):
                for y in range(x + 1):
                    if glasses[x][y] > 1.0:
                        to_pour = glasses[x][y] - 1.0
                        glasses[x + 1][y] += to_pour / 2
                        glasses[x + 1][y + 1] += to_pour / 2
                        glasses[x][y] = 1.0
        full = 0
        for g in glasses:
            for glass in g:
                if glass >= 1.0:
                    full += 1
        self.result = str(full)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask676BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
