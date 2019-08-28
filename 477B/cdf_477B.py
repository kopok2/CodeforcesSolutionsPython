class CodeforcesTask477BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        m = (6 * self.n_k[0] - 1) * self.n_k[1]
        results = []
        for x in range(self.n_k[0]):
            results.append([6 * x + 1, 6 * x + 2, 6 * x + 3, 6 * x + 5])
        self.result = "{0}\n{1}".format(m, "\n".join([" ".join([str(x * self.n_k[1]) for x in res]) for res in results]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask477BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
