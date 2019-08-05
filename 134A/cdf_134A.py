class CodeforcesTask134ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [float(x) for x in input().split(" ")]

    def process_task(self):
        ss = sum(self.sequence)
        other_rests = [(ss - self.sequence[x]) / (self.n - 1) for x in range(self.n)]
        matching = [i + 1 for i, x in enumerate(other_rests) if self.sequence[i] == x]
        self.result = "{0}\n{1}".format(len(matching), " ".join([str(x) for x in matching]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask134ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
