class CodeforcesTask1060BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        if self.n < 10:
            self.result = str(self.n)
        else:
            self.result = str(sum([9] * (len(str(self.n)) - 1) +
                              [int(x) for x in str(self.n - int("9" * (len(str(self.n)) - 1)))]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1060BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
