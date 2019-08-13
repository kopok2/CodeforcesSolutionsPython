def f(i, cnt, dp):
    if dp[i] < 0:
        if not i:
            dp[i] = 0
        elif i == 1:
            dp[i] = cnt[i]
        else:
            dp[i] = max(dp[i - 1], dp[i - 2] + cnt[i] * i)
    return dp[i]


class CodeforcesTask455ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        counts = [0 for x in range(1000001)]
        for num in self.sequence:
            counts[num] += 1
        dp = [-1 for x in range(1000001)]
        for x in range(self.n + 1):
            f(x, counts, dp)
        self.result = str(f(self.n, counts, dp))
        unique = [(counts[i], i) for i in range(1000001) if counts[i]]
        if len(unique) == 1:
            self.result = str(unique[0][1] * unique[0][0])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask455ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
