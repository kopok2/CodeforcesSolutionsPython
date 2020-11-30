def bin_dist(xx, yy):
    return sum((abs(int(x) - int(y)) for x, y in zip(xx, yy)))


class CodeforcesTask467BSolution:
    def __init__(self):
        self.result = ''
        self.n_m_k = []
        self.armies = []

    def read_input(self):
        self.n_m_k = [int(x) for x in input().split(" ")]
        for _ in range(self.n_m_k[1] + 1):
            self.armies.append(int(input()))

    def process_task(self):
        bins = ["0" * (self.n_m_k[0] - len(bin(x)[2:])) + bin(x)[2:] for x in self.armies]
        self.result = str(sum((1 if bin_dist(bins[-1], x) <= self.n_m_k[2] else 0 for x in bins[:-1])))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask467BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
