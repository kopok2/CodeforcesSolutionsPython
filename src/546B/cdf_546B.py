class CodeforcesTask546BSolution:
    def __init__(self):
        self.result = ''
        self.badges = []

    def read_input(self):
        input()
        self.badges = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.badges.sort()
        cost = 0
        for x in range(1, len(self.badges)):
            if self.badges[x] <= self.badges[x - 1]:
                cost += self.badges[x - 1] - self.badges[x] + 1
                self.badges[x] = self.badges[x - 1] + 1
        self.result = str(cost)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask546BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
