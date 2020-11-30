class CodeforcesTask837BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.flag = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.flag.append(input())

    def process_task(self):
        if self.n_m[0] % 3 and self.n_m[1] % 3:
            self.result = "NO"
        else:
            variants = []
            if not self.n_m[0] % 3:
                c1 = self.flag[0][0]
                c2 = self.flag[self.n_m[0] // 3][0]
                c3 = self.flag[(self.n_m[0] // 3) * 2][0]
                if c1 != c2 and c1 != c3 and c3 != c2:
                    l1 = []
                    l2 = []
                    l3 = []
                    for x in range(self.n_m[0] // 3):
                        l1.append(c1 * self.n_m[1])
                        l2.append(c2 * self.n_m[1])
                        l3.append(c3 * self.n_m[1])
                    v = l1 + l2 + l3
                    variants.append(v)
            if not self.n_m[1] % 3:
                c1 = self.flag[0][0]
                c2 = self.flag[0][self.n_m[1] // 3]
                c3 = self.flag[0][(self.n_m[1] // 3) * 2]
                if c1 != c2 and c1 != c3 and c3 != c2:
                    x = (self.n_m[1] // 3)
                    l = c1 * x + c2 * x + c3 * x
                    v = [l for z in range(self.n_m[0])]
                    variants.append(v)
            canbe = False
            for v in variants:
                c = True
                for x in range(self.n_m[0]):
                    if self.flag[x] != v[x]:
                        c = False
                        break
                if c:
                    canbe = True
                    break
            self.result = "YES" if canbe else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask837BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
