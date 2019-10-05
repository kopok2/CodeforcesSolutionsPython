class CodeforcesTask255ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.tasks = []

    def read_input(self):
        self.n = int(input())
        self.tasks = [int(x) for x in input().split(" ")]

    def process_task(self):
        res = [0] * 3
        for x in range(self.n):
            res[x % 3] += self.tasks[x]
        self.result = ["chest", "biceps", "back"][res.index(max(res))]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask255ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
