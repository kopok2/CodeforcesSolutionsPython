def max_beauty(ribbon, n):
    b_cnt = {}
    for c in ribbon:
        if c in b_cnt:
            b_cnt[c] += 1
        else:
            b_cnt[c] = 1
    mx = 0
    for key, val in b_cnt.items():
        mx = max(mx, val)
    l = len(ribbon)
    if mx == l and n == 1:
        return l - 1
    elif mx == l:
        return l
    else:
        return min(l, mx + n)


class CodeforcesTask979BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.ribbons = []

    def read_input(self):
        self.n = int(input())
        self.ribbons = [input() for x in range(3)]

    def process_task(self):
        names = ["Kuro", "Shiro", "Katie"]
        bes = [max_beauty(x, self.n) for x in self.ribbons]
        winning = max(bes)
        if bes.count(winning) > 1:
            self.result = "Draw"
        else:
            self.result = names[bes.index(winning)]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask979BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
