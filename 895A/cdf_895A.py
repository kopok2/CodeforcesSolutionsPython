class CodeforcesTask895ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sectors = []

    def read_input(self):
        self.n = int(input())
        self.sectors = [int(x) for x in input().split(" ")]

    def process_task(self):
        mn = 360
        for a in range(self.n):
            for b in range(a, self.n):
                mn = min(mn, abs(2 * sum(self.sectors[a:b]) - 360))
        self.result = str(mn)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask895ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
