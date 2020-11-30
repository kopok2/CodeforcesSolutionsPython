class CodeforcesTask1038BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        if self.n <= 2:
            self.result = "No"
        else:
            if self.n % 2:
                self.result = "Yes\n{0}\n{1}".format(" ".join([str(self.n // 2 + self.n % 2)] + [str(x + 1) for x in range(self.n // 2 + self.n % 2)]),
                                                 " ".join([str(self.n // 2)] + [str(x + 1) for x in range(self.n // 2 + self.n % 2, self.n)]))
            else:
                self.result = "Yes\n{0}\n{1}".format("2 {0} {1}".format(1, self.n), "{0} {1}".format(self.n - 2, " ".join([str(x) for x in range(2, self.n)])))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1038BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
