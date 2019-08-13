class CodeforcesTask1037BSolution:
    def __init__(self):
        self.result = ''
        self.n_s = []
        self.array = []

    def read_input(self):
        self.n_s = [int(x) for x in input().split(" ")]
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.array.sort()
        median = self.array[self.n_s[0] // 2]
        if median == self.n_s[1]:
            moves = 0
        elif median > self.n_s[1]:
            moves = -sum([min(self.n_s[1] - x, 0)for x in self.array[:self.n_s[0] // 2 + 1]])
        else:
            moves = -sum([min(0, x - self.n_s[1]) for x in self.array[self.n_s[0] // 2:]])
        self.result = str(moves)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1037BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
