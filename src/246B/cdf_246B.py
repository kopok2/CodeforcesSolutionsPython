class CodeforcesTask246BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.array = []

    def read_input(self):
        self.n = int(input())
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        s = sum(self.array)
        if not s % self.n:
            self.result = str(self.n)
        else:
            self.result = str(self.n - 1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask246BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
