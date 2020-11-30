class CodeforcesTask261ASolution:
    def __init__(self):
        self.result = ''
        self.discounts = []
        self.items_count = 0
        self.prices = []

    def read_input(self):
        input()
        self.discounts = [int(x) for x in input().split(" ")]
        self.items_count = int(input())
        self.prices = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.discounts.sort()
        self.prices.sort(reverse=True)
        price = 0
        discount = self.discounts[0]
        for x in range(self.items_count):
            if x % (discount + 2) < discount:
                price += self.prices[x]
        self.result = str(price)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask261ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
