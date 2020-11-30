class CodeforcesTask610ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        if self.n % 2:
            r = 0
        else:
            r = (self.n // 2 - 1) // 2
        self.result = str(r)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask610ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
