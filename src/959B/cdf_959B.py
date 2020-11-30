class CodeforcesTask959BSolution:
    def __init__(self):
        self.result = ''
        self.n_k_m = []
        self.lang = []
        self.prices = []
        self.groups = []
        self.message = []

    def read_input(self):
        self.n_k_m = [int(x) for x in input().split(" ")]
        self.lang = input().split(" ")
        self.prices = [int(x) for x in input().split(" ")]
        for _ in range(self.n_k_m[1]):
            self.groups.append([int(x) for x in input().split(" ")[1:]])
        self.message = input().split(" ")

    def process_task(self):
        groups = {}
        group_prices = {}
        for g in range(self.n_k_m[1]):
            for word in self.groups[g]:
                groups[self.lang[word - 1]] = g
                if g in group_prices:
                    group_prices[g] = min(group_prices[g], self.prices[word - 1])
                else:
                    group_prices[g] = self.prices[word - 1]
        price = 0
        for word in self.message:
            price += group_prices[groups[word]]
        self.result = str(price)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask959BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
