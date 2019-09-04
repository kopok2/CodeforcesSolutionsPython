class CodeforcesTask536BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.p = ''
        self.y = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.p = input()
        self.y = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.p == self.p[0] * len(self.p):
            go = [1] * self.n_m[0]
            for y in self.y:
                go = go[:y] + [0] * len(self.p) + go[y + len(self.p):]
            result = 1
            non_zero = sum(go)
            d = 1000000007
            for i in range(non_zero):
                result = result * 26 % d
            self.result = str(result)
        else:
            projection = {}
            for x in range(self.n_m[0]):
                projection[x] = "?"
            canbe = True
            for y in self.y:
                for x in range(len(self.p)):
                    if y + x <= self.n_m[0]:
                        c = projection[y + x - 1]
                        if c == "?":
                            projection[y + x - 1] = self.p[x]
                        elif c != self.p[x]:
                            canbe = False
                            break
                    else:
                        canbe = False
                        break
                if not canbe:
                    break
            if not canbe:
                self.result = "0"
            else:
                non_zero = 0
                for x in range(self.n_m[0]):
                    if projection[x] == "?":
                        non_zero += 1
                result = 1
                d = 1000000007
                for i in range(non_zero):
                    result = result * 26 % d
                self.result = str(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask536BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
