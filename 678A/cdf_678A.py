class CodeforcesTask678ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        if not self.n_k[0] % self.n_k[1]:
            self.result = str(sum(self.n_k))
        else:
            self.result = str(((self.n_k[0] // self.n_k[1]) + 1) * self.n_k[1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask678ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
