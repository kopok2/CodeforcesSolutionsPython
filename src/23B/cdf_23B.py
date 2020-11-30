class CodeforcesTask23BSolution:
    def __init__(self):
        self.result = ''
        self.t = 0
        self.tests = []

    def read_input(self):
        self.t = int(input())
        for x in range(self.t):
            self.tests.append(int(input()))

    def process_task(self):
        results = []
        for t in self.tests:
            results.append(str(max(0, t - 2)))
        self.result = "\n".join(results)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask23BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
