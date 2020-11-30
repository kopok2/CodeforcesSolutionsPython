class CodeforcesTask169ASolution:
    def __init__(self):
        self.result = ''
        self.n_a_b = []
        self.chores = []

    def read_input(self):
        self.n_a_b = [int(x) for x in input().split(" ")]
        self.chores = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.chores.sort()
        self.result = str(self.chores[self.n_a_b[2]] - self.chores[self.n_a_b[2] - 1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask169ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
