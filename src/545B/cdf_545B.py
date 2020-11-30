class CodeforcesTask545BSolution:
    def __init__(self):
        self.result = ''
        self.s = ''
        self.t = ''

    def read_input(self):
        self.s = input()
        self.t = input()

    def process_task(self):
        n = len(self.s)
        res = [0] * n
        cnt = 0
        b = False
        for x in range(n):
            if self.s[x] != self.t[x]:
                if b:
                    res[x] = self.s[x]
                else:
                    res[x] = self.t[x]
                b = not b
                cnt += 1
            else:
                res[x] = self.s[x]
        if not cnt % 2:
            self.result = "".join([str(x) for x in res])
        else:
            self.result = "impossible"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask545BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
