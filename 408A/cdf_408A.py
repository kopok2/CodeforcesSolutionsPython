class CodeforcesTask408ASolution:
    def __init__(self):
        self.result = ''
        self.cash_count = 0
        self.client_cashwise = []
        self.baskets = []

    def read_input(self):
        self.cash_count = int(input())
        self.client_cashwise = [int(x) for x in input().split(" ")]
        for x in range(self.cash_count):
            self.baskets.append([int(x) for x in input().split(" ")])

    def process_task(self):
        times = [len(x) * 15 + 5 * sum(x) for x in self.baskets]
        self.result = str(min(times))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask408ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
