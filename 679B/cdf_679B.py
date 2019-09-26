def cube(a):
    return a ** 3


def steps(m):
    if m <= 7:
        return m
    x = 1
    while cube(x + 1) <= m:
        x += 1
    return  1 + steps(max(m - cube(x), cube(x) - 1 - cube(x - 1)))


class CodeforcesTask679BSolution:
    def __init__(self):
        self.result = ''
        self.m = 0

    def read_input(self):
        self.m = int(input())

    def process_task(self):
        sub = 0
        ste = 0
        while self.m:
            ste += 1
            x = 1
            while cube(x + 1) <= self.m:
                x += 1
            if steps(self.m) == 1 + steps(self.m - cube(x)):
                self.m -= cube(x)
                sub += cube(x)
            else:
                self.m = cube(x) - 1 - cube(x - 1)
                sub += cube(x - 1)
        self.result = "{0} {1}".format(ste, sub)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask679BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
