class CodeforcesTask583ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.schedule = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n ** 2):
            self.schedule.append([int(y) for y in input().split(" ")])

    def process_task(self):
        vertical = [False for x in range(self.n)]
        horizontal = [False for x in range(self.n)]
        workdays = []
        for x in range(self.n ** 2):
            if not vertical[self.schedule[x][0] - 1] and not horizontal[self.schedule[x][1] - 1]:
                workdays.append(x + 1)
                vertical[self.schedule[x][0] - 1] = True
                horizontal[self.schedule[x][1] - 1] = True
        self.result = " ".join([str(x) for x in workdays])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask583ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
