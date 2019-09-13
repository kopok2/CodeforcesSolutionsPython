class CodeforcesTask899ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.teams = []

    def read_input(self):
        self.n = int(input())
        self.teams = [int(x) for x in input().split(" ")]

    def process_task(self):
        ss = sum(self.teams)
        b = ss - self.n
        a = self.n - b
        t = min(a, b)
        if a > b:
            t += (a - b) // 3
        self.result = str(t)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask899ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
