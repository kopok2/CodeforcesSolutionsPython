class CodeforcesTask959ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        self.result = "Mahmoud" if not self.n % 2 else "Ehab"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask959ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
