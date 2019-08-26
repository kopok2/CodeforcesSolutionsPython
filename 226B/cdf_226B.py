class CodeforcesTask226BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.piles = []
        self.q = 0
        self.variants = []

    def read_input(self):
        self.n = int(input())
        self.piles = [int(x) for x in input().split(" ")]
        self.q = int(input())
        self.variants = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.piles.sort(reverse=True)
        sums = [0] * self.n
        sums[0] = self.piles[0]
        for x in range(self.n - 1):
            sums[x + 1] = self.piles[x + 1] + sums[x]
        anwsers = {}
        results = []
        for query in self.variants:
            if query in anwsers.keys():
                results.append(anwsers[query])
            else:
                anwser = 0
                factor = 1
                k = 1
                width = query
                x = 1
                while x + width < self.n:
                    anwser += (sums[x + width - 1] - sums[x - 1]) * factor
                    factor += 1
                    x += width
                    k += 1
                    width = query ** k
                anwser += (sums[-1] - sums[x - 1]) * factor
                results.append(anwser)
                anwsers[query] = anwser
        self.result = " ".join([str(x) for x in results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask226BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
