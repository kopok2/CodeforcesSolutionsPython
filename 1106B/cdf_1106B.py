class CodeforcesTask1106BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.stock = []
        self.prices = []
        self.customers = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.stock = [int(x) for x in input().split(" ")]
        self.prices = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.customers.append([int(y) for y in input().split(" ")])

    def process_task(self):
        results = []
        stock_pricing = [(self.prices[x], x) for x in range(self.n_m[0])]
        stock_pricing.sort(reverse=True)
        #print(stock_pricing)
        for customer in self.customers:
            cost = 0
            base_order = min(customer[1], self.stock[customer[0] - 1])
            rem = customer[1] - base_order
            cost += base_order * self.prices[customer[0] - 1]
            self.stock[customer[0] - 1] -= base_order
            while rem:
                if stock_pricing:
                    cheap_order = min(self.stock[stock_pricing[-1][1]], rem)
                    cost += cheap_order * stock_pricing[-1][0]
                    self.stock[stock_pricing[-1][1]] -= cheap_order
                    rem -= cheap_order
                    if not self.stock[stock_pricing[-1][1]]:
                        stock_pricing.pop(-1)
                else:
                    cost = 0
                    break
            results.append(cost)
        self.result = "\n".join([str(x) for x in results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1106BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
