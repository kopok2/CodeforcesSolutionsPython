class CodeforcesTask34BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.sale = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.sale = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.sale.sort()
        money = 0
        for x in range(self.n_m[1]):
            if self.sale[x] < 0:
                money -= self.sale[x]
            else:
                break
        self.result = str(money)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask34BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
