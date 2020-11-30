class CodeforcesTask189ASolution:
    def __init__(self):
        self.result = ''
        self.n_a_b_c = []

    def read_input(self):
        self.n_a_b_c = [int(x) for x in input().split(" ")]

    def process_task(self):
        dp = [0] * (self.n_a_b_c[0] + 1)
        dp[0] = 1
        for x in range(self.n_a_b_c[0]):
            for a in self.n_a_b_c[1:]:
                if dp[x]:
                    if x + a <= self.n_a_b_c[0]:
                        dp[x + a] = max(dp[x + a], dp[x] + 1)
        self.result = str(dp[-1] - 1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask189ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
