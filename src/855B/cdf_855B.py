class CodeforcesTask855BSolution:
    def __init__(self):
        self.result = ''
        self.n_p_q_r = []
        self.a = []

    def read_input(self):
        self.n_p_q_r = [int(x) for x in input().split(" ")]
        self.a = [int(x) for x in input().split(" ")]

    def process_task(self):
        dp = [[0] * self.n_p_q_r[0] for x in range(3)]
        for x in range(3):
            dp[x][0] = self.a[0] * self.n_p_q_r[1 + x]
            if x > 0:
                dp[x][0] += dp[x - 1][0]
            for y in range(1, self.n_p_q_r[0]):
                if not x:
                    dp[x][y] = max(dp[x][y - 1], self.a[y] * self.n_p_q_r[1 + x])
                else:
                    dp[x][y] = max(dp[x][y - 1], self.a[y] * self.n_p_q_r[1 + x] + dp[x - 1][y])
        self.result = str(dp[2][-1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask855BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
