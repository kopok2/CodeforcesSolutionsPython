class CodeforcesTask248BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        if self.n < 3:
            self.result = "-1"
        else:
            res = ((10 ** (self.n - 1)) // 210) * 210 + (210 if 10 ** (self.n - 1) % 210 else 0)
            self.result = str(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask248BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
