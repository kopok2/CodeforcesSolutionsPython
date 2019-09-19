class CodeforcesTask1113BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.machines = []

    def read_input(self):
        self.n = int(input())
        self.machines = [int(x) for x in input().split(" ")]

    def process_task(self):
        tc = list(set(self.machines))
        ss = sum(self.machines)
        if len(tc) > 1:
            z = [[] for x in range(100)]
            for x in range(1, 101):
                for y in range(1, x + 1):
                    if not x % y:
                        z[x - 1].append(y)
            mn = ss
            for a in tc:
                for b in tc:
                    if a != b:
                        base = a + b
                        for d in z[a - 1]:
                            if a // d + b * d < base:
                                mn = min(mn, ss - base + a // d + b * d)
            self.result = str(mn)
        else:
            self.result = str(ss)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1113BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
