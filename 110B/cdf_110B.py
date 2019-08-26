class CodeforcesTask110BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        self.result = "abcd" * (self.n // 4) + "abcd"[:self.n % 4]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask110BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
