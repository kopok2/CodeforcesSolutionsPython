class CodeforcesTask397ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.segments = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.segments.append([int(y) for y in input().split(" ")])

    def process_task(self):
        segment = [1 if self.segments[0][0] <= x < self.segments[0][1] else 0 for x in range(100)]
        for x in range(self.n - 1):
            for y in range(self.segments[x + 1][0], self.segments[x + 1][1]):
                segment[y] = 0
        self.result = str(sum(segment))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask397ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
