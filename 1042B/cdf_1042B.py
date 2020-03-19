class CodeforcesTask1042BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.juices = []

    def read_input(self):
        self.n = int(input())
        for _ in range(self.n):
            inp = input().split(" ")
            inp[1] = list(inp[1])
            inp[1].sort()
            inp[1] = "".join(inp[1])
            self.juices.append([int(inp[0]), inp[1]])

    def process_task(self):
        pricing = {}
        schemes = ["A", "B", "C", "AB", "BC", "AC", "ABC"]
        for juice in self.juices:
            if not juice[1] in pricing:
                pricing[juice[1]] = juice[0]
            else:
                pricing[juice[1]] = min(pricing[juice[1]], juice[0])
        for s in schemes:
            if s not in pricing:
                pricing[s] = 10 ** 7
        prices = []
        for i in range(1, 2 ** 7):
            mask = "0" * (7 - len(bin(i)[2:])) + bin(i)[2:]
            now = ''
            price = 0
            for x in range(7):
                if mask[x] == '1':
                    now += schemes[x]
                    price += pricing[schemes[x]]
            if "A" in now and "B" in now and "C" in now:
                prices.append(price)
        res = min(prices)
        if res >= 10 ** 7:
            res = -1
        self.result = str(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1042BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
