class CodeforcesTask777BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.she = []
        self.mor = []

    def read_input(self):
        self.n = int(input())
        self.she = [int(x) for x in input()]
        self.mor = [int(x) for x in input()]

    def process_task(self):
        self.she.sort(reverse=True)
        self.mor.sort(reverse=True)
        mx = max(max(self.she), max(self.mor))
        atta = 0
        deff = 0
        shecnt = [0 for x in range(mx + 1)]
        morcnt = [0 for x in range(mx + 1)]
        for x in range(self.n):
            shecnt[self.she[x]] += 1
            morcnt[self.mor[x]] += 1
        for base in range(mx, -1, -1):
            #print(shecnt, morcnt)
            for it in range(shecnt[base]):
                for i in range(mx, base, -1):
                    if morcnt[i] and shecnt[base] > 0:
                        atta += 1
                        morcnt[i] -= 1
                        shecnt[base] -= 1
        shecnt = [0 for x in range(mx + 1)]
        morcnt = [0 for x in range(mx + 1)]
        for x in range(self.n):
            shecnt[self.she[x]] += 1
            morcnt[self.mor[x]] += 1
        for base in range(mx, -1, -1):
            for it in range(shecnt[base]):
                for i in range(mx, base - 1, -1):
                    if morcnt[i] and shecnt[base] > 0:
                        deff += 1
                        morcnt[i] -= 1
                        shecnt[base] -= 1
        self.result = "{0}\n{1}".format(self.n - deff, atta)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask777BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
