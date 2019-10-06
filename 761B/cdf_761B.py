class CodeforcesTask761BSolution:
    def __init__(self):
        self.result = ''
        self.n_l = []
        self.track1 = []
        self.track2 = []

    def read_input(self):
        self.n_l = [int(x) for x in input().split(" ")]
        self.track1 = [int(x) for x in input().split(" ")]
        self.track2 = [int(x) for x in input().split(" ")]

    def process_task(self):
        dists1 = [self.track1[x] - self.track1[x - 1] for x in range(1, self.n_l[0])]
        dists2 = [self.track2[x] - self.track2[x - 1] for x in range(1, self.n_l[0])]
        can = False
        for x in range(self.n_l[0]):

            nd = self.track1[x:] + self.track1[:x]
            dists1 = [nd[x] - nd[x - 1] for x in range(1, self.n_l[0])]
            for x in range(1, self.n_l[0]):
                if dists1[x - 1] < 0:
                    dists1[x - 1] += self.n_l[1]
            #print(nd, dists1, dists2)
            if dists1 == dists2:
                can = True
                break
        self.result = "YES" if can else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask761BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
