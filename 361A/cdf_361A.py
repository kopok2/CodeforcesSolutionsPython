class CodeforcesTask361ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        res = []
        for x in range(self.n_k[0]):
            line = [0] * self.n_k[0]
            line[x] = self.n_k[1]
            res.append(" ".join([str(y) for y in line]))
        self.result = "\n".join(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask361ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
