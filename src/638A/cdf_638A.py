class CodeforcesTask638ASolution:
    def __init__(self):
        self.result = ''
        self.n_a = []

    def read_input(self):
        self.n_a = [int(x) for x in input().split(" ")]

    def process_task(self):
        half = self.n_a[0] // 2
        if self.n_a[1] % 2:
            self.result = str(1 + self.n_a[1] // 2)
        else:
            self.result = str(1 + half - self.n_a[1] // 2)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask638ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
