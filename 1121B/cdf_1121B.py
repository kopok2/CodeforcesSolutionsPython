class CodeforcesTask1121BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sweets = []

    def read_input(self):
        self.n = int(input())
        self.sweets = [int(x) for x in input().split(" ")]

    def process_task(self):
        counts = [0 for x in range(max(self.sweets) * 2 + 1)]
        for x in range(self.n):
            for y in range(self.n):
                if x != y:
                    counts[self.sweets[x] + self.sweets[y]] += 1
        self.result = str(max(counts) // 2)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1121BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
