class CodeforcesTask999BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.code = ''

    def read_input(self):
        self.n = int(input())
        self.code = input()

    def process_task(self):
        for x in range(1, self.n + 1):
            if not self.n % x:
                self.code = self.code[:x][::-1] + self.code[x:]
        self.result = self.code

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask999BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
