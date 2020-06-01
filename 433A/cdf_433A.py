from collections import Counter


class CodeforcesTask433ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.a = []

    def read_input(self):
        self.n = int(input())
        self.a = [int(x) for x in input().split(" ")]

    def process_task(self):
        cnt = Counter(self.a)
        sol = False
        for a in range(cnt[100] + 1):
            for b in range(cnt[200] + 1):
                if a * 100 + b * 200 == (cnt[100] - a) * 100 + (cnt[200] - b) * 200:
                    sol = True
        self.result = "NO" if not sol else "YES"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask433ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
