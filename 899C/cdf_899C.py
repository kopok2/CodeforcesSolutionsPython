class CodeforcesTask899CSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        if not self.n % 4:
            sol = []
            for x in range(self.n // 4):
                sol.append(x + 1)
                sol.append(self.n - x)
            self.result = "0\n{0} {1}".format(len(sol), " ".join([str(x) for x in sol]))
        elif not self.n % 2:
            sol = []
            for x in range(self.n // 4):
                sol.append(x + 1)
                sol.append(self.n - x)
            sol.append(self.n // 2)
            self.result = "1\n{0} {1}".format(len(sol), " ".join([str(x) for x in sol]))
        elif self.n % 4 == 3:
            sol = []
            for x in range(self.n // 4):
                sol.append(x + 1)
                sol.append(self.n - x)
            sol.append(self.n - self.n // 4)
            self.result = "{2}\n{0} {1}".format(len(sol), " ".join([str(x) for x in sol]), 0)
        else:
            sol = []
            for x in range(self.n // 4):
                sol.append(x + 1)
                sol.append(self.n - x)
            sol.append(self.n // 4 + 1)
            self.result = "{2}\n{0} {1}".format(len(sol), " ".join([str(x) for x in sol]), 1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask899CSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
