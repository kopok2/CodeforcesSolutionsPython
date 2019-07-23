class CodeforcesTask962ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.tasks = []

    def read_input(self):
        self.n = int(input())
        self.tasks = [int(x) for x in input().split(" ")]

    def process_task(self):
        tasks = sum(self.tasks)
        eq = tasks // 2 + tasks % 2
        s = 0
        for x in range(self.n):
            s += self.tasks[x]
            if s >= eq:
                self.result = str(x + 1)
                break

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask962ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
