class CodeforcesTask265BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.trees = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.trees.append(int(input()))

    def process_task(self):
        time = self.n * 2 - 1
        time += self.trees[0]
        pos = self.trees[0]
        for x in range(self.n - 1):
            if pos <= self.trees[x + 1]:
                time += self.trees[x + 1] - pos
                pos = self.trees[x + 1]
            else:
                time += pos - self.trees[x + 1]
                pos = self.trees[x + 1]
        self.result = str(time)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask265BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
