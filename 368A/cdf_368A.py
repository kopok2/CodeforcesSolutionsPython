class CodeforcesTask368ASolution:
    def __init__(self):
        self.result = ''
        self.n_d = []
        self.hooks = []
        self.guests = 0

    def read_input(self):
        self.n_d = [int(x) for x in input().split(" ")]
        self.hooks = [int(x) for x in input().split(" ")]
        self.guests = int(input())

    def process_task(self):
        self.hooks.sort()
        profit = max(0, self.guests - self.n_d[0]) * (-self.n_d[1]) + sum(self.hooks[:min(self.n_d[0], self.guests)])
        self.result = str(profit)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask368ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
