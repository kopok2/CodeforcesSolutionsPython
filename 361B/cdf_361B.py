class CodeforcesTask361BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.n_k[0] == self.n_k[1]:
            self.result = "-1"
        else:
            res = [0] * self.n_k[0]
            for x in range(self.n_k[0] - self.n_k[1], self.n_k[0]):
                res[x] = x + 1
            res[0] = self.n_k[0] - self.n_k[1]
            for x in range(1, self.n_k[0] - self.n_k[1]):
                res[x] = x
            self.result = " ".join([str(x) for x in res])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask361BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
