class CodeforcesTask1003ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.coins = []

    def read_input(self):
        self.n = int(input())
        self.coins = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.result = str(max([self.coins.count(x) for x in range(1, max(self.coins) + 1)]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1003ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
