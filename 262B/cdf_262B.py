class CodeforcesTask262BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.incomes = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.incomes = [int(x) for x in input().split(" ")]

    def process_task(self):
        negs = sum([1 if x < 0 else 0 for x in self.incomes])
        if self.n_k[1] <= negs:
            for x in range(self.n_k[1]):
                self.incomes[x] = abs(self.incomes[x])
            self.result = str(sum(self.incomes))
        else:
            rest = self.n_k[1] - negs
            refined = [abs(x) for x in self.incomes]
            refined.sort()
            if rest % 2:
                refined[0] = -refined[0]
            self.result = str(sum(refined))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask262BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
