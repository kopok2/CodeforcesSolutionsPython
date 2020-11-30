class CodeforcesTask635BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.curr = []
        self.need = []

    def read_input(self):
        self.n = int(input()) - 1
        self.curr = [int(x) for x in input().split(" ") if int(x)]
        self.need = [int(x) for x in input().split(" ") if int(x)]

    def process_task(self):
        neighbours1 = {}
        neighbours2 = {}
        for x in range(self.n - 1):
            neighbours1[str(self.curr[x])] = (self.curr[x - 1], self.curr[x + 1])
            neighbours2[str(self.need[x])] = (self.need[x - 1], self.need[x + 1])
        neighbours1[str(self.curr[self.n - 1])] = (self.curr[self.n - 2], self.curr[0])
        neighbours2[str(self.need[self.n - 1])] = (self.need[self.n - 2], self.need[0])
        #print(neighbours1, neighbours2)
        canbe = True
        for p in self.curr:
            if neighbours1[str(p)] != neighbours2[str(p)]:
                canbe = False
                break
        self.result = "YES" if canbe else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask635BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
