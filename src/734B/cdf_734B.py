class CodeforcesTask734BSolution:
    def __init__(self):
        self.result = ''
        self.kkkk = []

    def read_input(self):
        self.kkkk = [int(x) for x in input().split(" ")]

    def process_task(self):
        c256 = min(self.kkkk[0], self.kkkk[2], self.kkkk[3])
        self.kkkk[0] -= c256
        c32 = min(self.kkkk[0], self.kkkk[1])
        self.result = str(c256 * 256 + c32 * 32)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask734BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
