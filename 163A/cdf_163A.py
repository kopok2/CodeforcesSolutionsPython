import math


def newton(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


class CodeforcesTask163ASolution:
    def __init__(self):
        self.result = ''
        self.s = ''
        self.t = ''

    def read_input(self):
        self.s = input()
        self.t = input()

    def process_task(self):
        dp = [[0 for x in range(5005)] for y in range(5005)]
        l1 = len(self.s)
        l2 = len(self.t)
        mod = 1_000_000_007
        for x in range(l1):
            for y in range(l2):
                dp[x + 1][y + 1] = dp[x + 1][y] % mod
                fact = 1 if self.s[x] == self.t[y] else 0
                dp[x + 1][y + 1] += (fact * (dp[x][y] + 1)) % mod
        result = 0
        for x in range(l1):
            result = (result + dp[x + 1][l2]) % mod
        self.result = str(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask163ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
