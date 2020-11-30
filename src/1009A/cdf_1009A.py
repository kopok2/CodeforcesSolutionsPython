class CodeforcesTask1009ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.prices = []
        self.wallet = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.prices = [int(x) for x in input().split(" ")]
        self.wallet = [int(x) for x in input().split(" ")]

    def process_task(self):
        bought = 0
        self.prices = self.prices[::-1]
        self.wallet = self.wallet[::-1]
        bill = self.wallet.pop(-1)
        while self.prices and bill:
            buyin = self.prices.pop(-1)

            if bill >= buyin:
                bill = None
                bought += 1
            if not bill:
                if self.wallet:
                    bill = self.wallet.pop(-1)
                else:
                    break
        self.result = str(bought)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1009ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
