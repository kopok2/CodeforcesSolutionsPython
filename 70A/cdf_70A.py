class CodeforcesTask70ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        self.result = str(1 if not self.n else 3 ** (self.n - 1) % (10**6 + 3))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask70ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
