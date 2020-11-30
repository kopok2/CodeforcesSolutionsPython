class CodeforcesTask32ASolution:
    def __init__(self):
        self.result = ''
        self.n_d = []
        self.heights = []

    def read_input(self):
        self.n_d = [int(x) for x in input().split(" ")]
        self.heights = [int(x) for x in input().split(" ")]

    def process_task(self):
        ways = 0
        d = self.n_d[1]
        for x in range(self.n_d[0]):
            for y in range(self.n_d[0]):
                if x != y:
                    if abs(self.heights[x] - self.heights[y]) <= d:
                        ways += 1
        self.result = str(ways)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask32ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
