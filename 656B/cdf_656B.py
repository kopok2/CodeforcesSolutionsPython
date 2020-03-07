class CodeforcesTask656BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.m = []
        self.r = []

    def read_input(self):
        self.n = int(input())
        self.m = [int(x) for x in input().split(" ")]
        self.r = [int(x) for x in input().split(" ")]

    def process_task(self):
        bad_days = 0
        for day in range(10**5):
            for x in range(self.n):
                if day % self.m[x] == self.r[x]:
                    bad_days += 1
                    break
        self.result = str(bad_days / (10 ** 5))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask656BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
