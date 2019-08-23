def kth_d_root(k, x):
    return 9 * (k - 1) + x


class CodeforcesTask1107BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.queries = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.queries.append([int(y) for y in input().split(" ")])

    def process_task(self):
        for query in self.queries:
            self.result += "{0}\n".format(kth_d_root(*query))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1107BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
