class CodeforcesTask873ASolution:
    def __init__(self):
        self.result = ''
        self.n_k_x = []
        self.chores = []

    def read_input(self):
        self.n_k_x = [int(x) for x in input().split(" ")]
        self.chores = [int(x) for x in input().split(" ")][::-1]

    def process_task(self):
        for x in range(self.n_k_x[1]):
            self.chores[x] = min(self.chores[x], self.n_k_x[2])
        self.result = str(sum(self.chores))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask873ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
