from collections import defaultdict


class CodeforcesTask981BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.first = []
        self.m = 0
        self.second = []

    def read_input(self):
        self.n = int(input())
        for _ in range(self.n):
            self.first.append([int(y) for y in input().split(" ")])
        self.m = int(input())
        for _ in range(self.m):
            self.second.append([int(y) for y in input().split(" ")])

    def process_task(self):
        top_income = defaultdict(int)
        income = 0
        for a in self.first + self.second:
            top_income[a[0]] = max(top_income[a[0]], a[1])
        income = sum(top_income.values())
        self.result = str(income)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask981BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
