class CodeforcesTask596BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.array = []

    def read_input(self):
        self.n = int(input())
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        steps = 0
        for x in range(self.n):
            steps += abs(self.array[x] - (0 if not x else self.array[x - 1]))
        self.result = str(steps)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask596BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
