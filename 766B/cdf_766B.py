class CodeforcesTask766BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.segments = []

    def read_input(self):
        self.n = int(input())
        self.segments = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.segments.sort()
        can_ = False
        for x in range(self.n - 2):
            if self.segments[x] + self.segments[x + 1] > self.segments[x + 2]:
                can_ = True
                break
        self.result = "YES" if can_ else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask766BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
