class CodeforcesTask586BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.upper = []
        self.lower = []
        self.crossing = []

    def read_input(self):
        self.n = int(input())
        self.upper = [int(x) for x in input().split(" ")]
        self.lower = [int(x) for x in input().split(" ")]
        self.crossing = [int(x) for x in input().split(" ")]

    def process_task(self):
        preu = [0] * (self.n - 1)
        prel = [0] * (self.n - 1)
        preu[0] = self.upper[0]
        prel[0] = self.lower[-1]
        for x in range(1, self.n - 1):
            preu[x] = preu[x - 1] + self.upper[x]
            prel[x] = prel[x - 1] + self.lower[- x - 1]
        prel = prel[::-1]
        ways = []
        for x in range(self.n - 2):
            ways.append(self.crossing[x + 1] + prel[x + 1] + preu[x])
        ways.append(self.crossing[0] + prel[0])
        ways.append(self.crossing[-1] + preu[-1])
        ways.sort()
        shortest = ways[0] + ways[1]
        self.result = str(shortest)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask586BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
