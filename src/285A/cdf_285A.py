class CodeforcesTask285ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        inc = [x for x in range(1, self.n_k[0] - self.n_k[1])]
        dc = [x for x in range(self.n_k[0] - self.n_k[1], self.n_k[0] + 1)][::-1]
        self.result = " ".join([str(x) for x in inc + dc])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask285ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
