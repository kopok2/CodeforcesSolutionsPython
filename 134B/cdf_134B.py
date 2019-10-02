TMP = 0


def dfs(a, b, n):
    global TMP
    if not b:
        TMP = n
        return None
    if b == 1:
        TMP += a - 1
        return None
    TMP += a // b
    dfs(b, a % b, n)


class CodeforcesTask134BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        ans = self.n - 1
        for i in range(1, self.n):
            global TMP
            TMP = 0
            dfs(self.n, i, self.n)
            ans = min(ans, TMP)
        self.result = str(ans)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask134BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
