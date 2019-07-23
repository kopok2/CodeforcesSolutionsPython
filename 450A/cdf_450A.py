class CodeforcesTask450ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.line = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.line = [(i, int(x)) for i, x in enumerate(input().split(" "))]

    def process_task(self):
        last = None
        while self.line:
            last = self.line.pop(0)
            last = (last[0], last[1] - self.n_m[1])
            if last[1] > 0:
                self.line.append(last)
        self.result = str(last[0] + 1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask450ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
