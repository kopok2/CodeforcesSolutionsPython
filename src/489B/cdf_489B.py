class CodeforcesTask489BSolution:
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
        self.a.sort()
        self.b.sort()
        pairs = 0
        for x in range(self.n):
            for y in range(self.m):
                if abs(self.a[x] - self.b[y]) <= 1:
                    pairs += 1
                    self.b[y] = 1000
                    break
        self.result = str(pairs)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask489BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
