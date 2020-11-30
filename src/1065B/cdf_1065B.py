class CodeforcesTask1065BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]

    def process_task(self):
        mn = max(self.n_m[0] - self.n_m[1] * 2, 0)
        x = 1
        while (x * (x - 1)) // 2 < self.n_m[1]:
            x += 1
        mx = self.n_m[0] - x
        self.result = "{0} {1}".format(mn, max(mn, mx))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1065BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
