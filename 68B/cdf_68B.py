def energy(acc, level, perc_loss):
    surplus = sum([max(x - level, 0) for x in acc])
    en_cost = sum([(abs(min(0, x - level)) * 100) / (100 - perc_loss) for x in acc])
    return surplus >= en_cost


class CodeforcesTask68BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.accumulators = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.accumulators = [int(x) for x in input().split(" ")]

    def process_task(self):
        l = 0
        r = sum(self.accumulators) / self.n_k[0]
        while r - l >= 0.000_0001:
            mid = l + (r - l) / 2
            if energy(self.accumulators, mid, self.n_k[1]):
                l = mid
            else:
                r = mid
        self.result = str(r)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask68BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
