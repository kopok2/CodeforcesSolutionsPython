class CodeforcesTask652BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.array = []

    def read_input(self):
        self.n = int(input())
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.array.sort()
        result = []
        for x in range(self.n // 2):
            result.append(self.array[x])
            result.append(self.array[x + self.n // 2 + self.n % 2])
        if self.n % 2:
            result.append(self.array[self.n // 2])
        self.result = " ".join([str(x) for x in result])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask652BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
