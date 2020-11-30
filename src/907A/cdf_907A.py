class CodeforcesTask907ASolution:
    def __init__(self):
        self.result = ''
        self.sizes = []

    def read_input(self):
        self.sizes = [int(x) for x in input().split(" ")]

    def process_task(self):
        res = []
        res.append(2 * self.sizes[0])
        res.append(min(2 * self.sizes[1], 2 * self.sizes[0] - 1))
        res.append(min(max(self.sizes[2], self.sizes[3]), min(self.sizes[2], self.sizes[3]) * 2))
        if res[2] >= self.sizes[1] or res[2] >= self.sizes[0] or min(self.sizes[2], self.sizes[3]) * 2 < max(self.sizes[2], self.sizes[3]):
            res = [-1]
        self.result = "\n".join([str(x) for x in res])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask907ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
