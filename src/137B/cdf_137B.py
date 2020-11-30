class CodeforcesTask137BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.nums = []

    def read_input(self):
        self.n = int(input())
        self.nums = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.result = str(self.n - len(set([x for x in self.nums if x <= self.n])))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask137BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
