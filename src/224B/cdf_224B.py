class CodeforcesTask224BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.sequence = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        cnt = [0 for x in range(100000)]
        for x in self.sequence:
            cnt[x - 1] += 1
        els = sum([1 if x else 0 for x in cnt])
        l = 0
        r = self.n_k[0] - 1
        if els < self.n_k[1]:
            self.result = "-1 -1"
        else:
            while els >= self.n_k[1]:
                cnt[self.sequence[r] - 1] -= 1
                if not cnt[self.sequence[r] - 1]:
                    els -= 1
                r -= 1
            r += 1
            els += 1
            while els == self.n_k[1]:
                cnt[self.sequence[l] - 1] -= 1
                if not cnt[self.sequence[l] - 1]:
                    els -= 1
                l += 1
                if l >= r:
                    break
            if l:
                l -= 1
            self.result = "{0} {1}".format(l + 1, r + 1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask224BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
