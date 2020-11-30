class CodeforcesTask1119ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.colors = []

    def read_input(self):
        self.n = int(input())
        self.colors = [int(x) for x in input().split(" ")]

    def process_task(self):
        lcl = self.colors[0]
        x = self.n
        while self.colors[x - 1] == lcl:
            x -= 1
        ldist = x - 1
        rcl = self.colors[-1]
        x = self.n
        self.colors = self.colors[::-1]
        while self.colors[x - 1] == rcl:
            x -= 1
        rdist = x - 1
        self.result = str(max(ldist, rdist))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1119ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
