import math


def xy_val(x, y, n):
    if not (x + y) % 2:
        if x > 1:
            num = 0
            if n % 2:
                num += math.ceil((x - 1) / 2) * math.ceil(n / 2)
                num += ((x - 1) // 2) * (n // 2)
                num += math.ceil(y / 2)
                return num
            else:
                num += (x - 1) * (n // 2)
                num += math.ceil(y / 2)
                return num
        else:
            return math.ceil(y / 2)
    else:
        if x > 1:
            num = 0
            if n % 2:
                num += math.ceil((x - 1) / 2) * math.ceil(n / 2)
                num += ((x - 1) // 2) * (n // 2)
                num += math.ceil(y / 2)
                if not x % 2:
                    num -= 1
                return num + xy_val(n, n, n)
            else:
                num += (x - 1) * (n // 2)
                num += math.ceil(y / 2)
                return num + xy_val(n, n, n)
        else:
            return math.ceil(y / 2) + xy_val(n, n, n)


class CodeforcesTask1027BSolution:
    def __init__(self):
        self.result = ''
        self.n_q = []
        self.queries = []

    def read_input(self):
        self.n_q = [int(x) for x in input().split(" ")]
        for x in range(self.n_q[1]):
            self.queries.append([int(y) for y in input().split(" ")])

    def process_task(self):
        #for x in range(4):
        #    print([xy_val(x + 1, y + 1, 4) for y in range(4)])
        #for x in range(5):
        #    print([xy_val(x + 1, y + 1, 5) for y in range(5)])
        for query in self.queries:
            print(xy_val(query[0], query[1], self.n_q[0]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1027BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
