class CodeforcesTask402BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.heights = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.heights = [int(x) for x in input().split(" ")]

    def process_task(self):
        w_k = 1001
        chosen = -1
        for base in range(1, 1001):
            costs = sum([0 if self.heights[x] == base + self.n_k[1] * x else 1 for x in range(self.n_k[0])])
            if costs < w_k:
                chosen = base
                w_k = costs
        operations = []
        for x in range(self.n_k[0]):
            if self.heights[x] != chosen + self.n_k[1] * x:
                diff = (chosen + self.n_k[1] * x) - self.heights[x]
                sign = "+" if diff > 0 else "-"
                operations.append("{0} {1} {2}".format(sign, x + 1, abs(diff)))
        self.result = "{0}\n{1}".format(len(operations), "\n".join(operations))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask402BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
