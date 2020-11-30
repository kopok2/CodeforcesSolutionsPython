class CodeforcesTask659ASolution:
    def __init__(self):
        self.result = ''
        self.n_a_b = []

    def read_input(self):
        self.n_a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        k = sum(self.n_a_b[1:]) % self.n_a_b[0]
        if not k:
            k = self.n_a_b[0]
        self.result = str(k)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask659ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
