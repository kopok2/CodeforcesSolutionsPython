class CodeforcesTask215ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.a = []
        self.m = 0
        self.b = []

    def read_input(self):
        self.n = int(input())
        self.a = [int(x) for x in input().split(" ")]
        self.m = int(input())
        self.b = [int(x) for x in input().split(" ")]

    def process_task(self):
        ratios = []
        for x in range(self.n):
            for y in range(self.m):
                ratio = self.b[y] / self.a[x]
                if ratio.is_integer():
                    ratios.append(ratio)
        ratios.sort()
        self.result = str(ratios.count(ratios[-1]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask215ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
