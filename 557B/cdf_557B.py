class CodeforcesTask557BSolution:
    def __init__(self):
        self.result = ''
        self.n_w = []
        self.cups = []

    def read_input(self):
        self.n_w = [int(x) for x in input().split(" ")]
        self.cups = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.cups.sort()
        max_per_g = (self.n_w[1] / 3) / self.n_w[0]
        real_per_g = min(self.cups[0], max_per_g)
        max_per_b = max_per_g * 2
        real_per_b = min(2 * real_per_g, self.cups[self.n_w[0]])
        ammount = 1.5 * self.n_w[0] * real_per_b
        self.result = str(ammount)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask557BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
