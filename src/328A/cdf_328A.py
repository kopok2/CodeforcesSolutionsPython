class CodeforcesTask328ASolution:
    def __init__(self):
        self.result = ''
        self.progression = []

    def read_input(self):
        self.progression = [int(x) for x in input().split(" ")]

    def process_task(self):
        arit = [self.progression[x] - self.progression[x - 1] for x in range(1, len(self.progression))]
        if arit[0] == arit[1] == arit[2]:
            self.result = str(self.progression[-1] + arit[0])
        else:
            geo = [self.progression[x] / self.progression[x - 1] for x in range(1, len(self.progression))]
            if geo[0] == geo[1] == geo[2]:
                if (geo[0] * self.progression[-1]).is_integer():
                    self.result = str(int(geo[0] * self.progression[-1]))
                else:
                    self.result = "42"
            else:
                self.result = "42"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask328ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
