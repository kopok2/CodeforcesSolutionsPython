class CodeforcesTask368BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.array = []
        self.ls = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.array = [int(x) for x in input().split(" ")]
        for _ in range(self.n_m[1]):
            self.ls.append(int(input()))

    def process_task(self):
        ss = set()
        dp = [0] * self.n_m[0]
        for x in range(self.n_m[0] - 1, -1, -1):
            ss.add(self.array[x])
            dp[x] = len(ss)
        res = []
        for q in self.ls:
            res.append(dp[q - 1])
        self.result = "\n".join([str(x) for x in res])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask368BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
