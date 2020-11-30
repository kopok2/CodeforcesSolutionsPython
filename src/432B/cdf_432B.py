class CodeforcesTask432BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.kits = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.kits.append([int(y) for y in input().split(" ")])

    def process_task(self):
        home_kits = {}
        for kit in self.kits:
            if kit[0] not in home_kits:
                home_kits[kit[0]] = 1
            else:
                home_kits[kit[0]] += 1
        result = []
        for x in range(self.n):
            if self.kits[x][1] in home_kits:
                wrong = home_kits[self.kits[x][1]]
                result.append(str(self.n - 1 + wrong) + " " + str(self.n - 1 - wrong))
            else:
                result.append(str(self.n - 1) + " " + str(self.n - 1))
        self.result = "\n".join(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask432BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
