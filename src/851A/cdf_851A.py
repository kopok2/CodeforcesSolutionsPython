class CodeforcesTask851ASolution:
    def __init__(self):
        self.result = ''
        self.n_k_t = []

    def read_input(self):
        self.n_k_t = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.n_k_t[1] <= self.n_k_t[2] <= self.n_k_t[0]:
            self.result = str(self.n_k_t[1])
        elif self.n_k_t[2] < self.n_k_t[1]:
            self.result = str(self.n_k_t[2])
        else:
            self.result = str(self.n_k_t[0] + self.n_k_t[1] - self.n_k_t[2])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask851ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
