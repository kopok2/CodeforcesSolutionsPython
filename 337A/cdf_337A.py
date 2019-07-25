class CodeforcesTask337ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.puzzles = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.puzzles = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.puzzles.sort()
        min_diff = 1001
        for x in range(self.n_m[1] - self.n_m[0] + 1):
            min_diff = min(min_diff, max(self.puzzles[x:x+self.n_m[0]]) - min(self.puzzles[x:x+self.n_m[0]]))
        self.result = str(min_diff)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask337ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
