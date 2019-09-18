class CodeforcesTask78BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        self.n -= 7
        self.result = "ROYGBIV"
        if self.n >= 4:
            self.result += "ROYG" * (self.n // 4) + "BIV"[:self.n % 4]
        else:
            if self.n == 1:
                self.result += "G"
            elif self.n == 2:
                self.result += "GB"[:self.n]
            else:
                self.result += "YGB"[:self.n]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask78BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
