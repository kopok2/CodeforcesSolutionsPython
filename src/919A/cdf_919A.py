class CodeforcesTask919ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.prices = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.prices.append([int(x) for x in input().split(" ")])

    def process_task(self):
        prices = [x[0]/x[1] for x in self.prices]
        min_price = min(prices)
        self.result = str(min_price * self.n_m[1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask919ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
