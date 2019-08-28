class CodeforcesTask884BSolution:
    def __init__(self):
        self.result = ''
        self.n_x = []
        self.encoding = []

    def read_input(self):
        self.n_x = [int(x) for x in input().split(" ")]
        self.encoding = [int(x) for x in input().split(" ")]

    def process_task(self):
        if sum(self.encoding) + (self.n_x[0] - 1) == self.n_x[1]:
            self.result = "YES"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask884BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
