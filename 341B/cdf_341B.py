class CodeforcesTask341BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        li = 1
        ma = 1
        for x in range(self.n - 1):
            if self.sequence[x] < self.sequence[x + 1]:
                li += 1
            else:
                ma = max(ma, li)
                li = 1
        self.result = str(ma)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask341BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
