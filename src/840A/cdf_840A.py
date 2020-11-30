import math


def bcof(x, y):
    a = math.factorial(x)
    b = math.factorial(y)
    c = math.factorial(x - y)  # that appears to be useful to get the correct result
    return a // (b * c)


def F(n, k):
    return bcof(n + 1, k + 1)


class CodeforcesTask840ASolution:
    def __init__(self):
        self.result = ''
        self.m = 0
        self.a = []
        self.b = []

    def read_input(self):
        self.m = int(input())
        self.a = [int(x) for x in input().split(" ")]
        self.b = [int(x) for x in input().split(" ")]

    def process_task(self):
        b = [(i, x) for i, x in enumerate(self.b)]
        b.sort(key=lambda tup: tup[1])
        self.a.sort(reverse=True)
        new_a = [0 for x in range(len(b))]
        for x in range(len(b)):
            new_a[b[x][0]] = self.a[x]
        self.result = " ".join([str(x) for x in new_a])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask840ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
