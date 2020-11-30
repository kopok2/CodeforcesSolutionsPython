class CodeforcesTask584ASolution:
    def __init__(self):
        self.result = ''
        self.n_t = []

    def read_input(self):
        self.n_t = [int(x) for x in input().split(" ")]

    def process_task(self):
        if len(str(self.n_t[1])) > self.n_t[0]:
            self.result = "-1"
        else:
            res = 10 ** (self.n_t[0] - 1) if self.n_t[1] == 10 else self.n_t[1] * (10 ** (self.n_t[0] - 1))
            self.result = str(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask584ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
