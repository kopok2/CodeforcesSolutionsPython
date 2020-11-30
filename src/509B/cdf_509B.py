class CodeforcesTask509BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.piles = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.piles = [int(x) for x in input().split(" ")]

    def process_task(self):
        mx_dist = max(self.piles) - min(self.piles)
        if mx_dist > self.n_k[1]:
            self.result = "NO"
        else:
            pile_order = " ".join([str(x + 1) for x in range(self.n_k[1])])
            results = []
            for pile in self.piles:
                pl = []
                pl += [pile_order for x in  range(pile // self.n_k[1])]
                pl.append(" ".join([str(x + 1) for x in range(self.n_k[1])][:(pile % self.n_k[1])]))
                results.append(" ".join(pl))
                if results[-1][0] == " ":
                    results[-1] = results[-1][1:]
            self.result = "YES\n{0}".format("\n".join(results))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask509BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
