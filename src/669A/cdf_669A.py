class CodeforcesTask669ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        res = 2 * (self.n // 3) + self.n % 3
        if self.n % 3 == 2:
            res -= 1
        self.result = str(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask669ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
