class CodeforcesTask242BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.segments = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.segments.append([int(y) for y in input().split(" ")])

    def process_task(self):
        starts = [x[0] for x in self.segments]
        stops = [x[1] for x in self.segments]
        start = min(starts)
        stop = max(stops)
        self.result = "-1"
        for x in range(self.n):
            if self.segments[x][0] <= start and self.segments[x][1] >= stop:
                self.result = str(x + 1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask242BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
