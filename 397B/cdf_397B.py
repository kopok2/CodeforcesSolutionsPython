class CodeforcesTask397BSolution:
    def __init__(self):
        self.result = ''
        self.t = 0
        self.queries = []

    def read_input(self):
        self.t = int(input())
        for _ in range(self.t):
            self.queries.append([int(x) for x in input().split(" ")])

    def process_task(self):
        res = []
        for query in self.queries:
            k = query[0] // query[1]
            res.append("Yes" if k * query[2] >= query[0] else "No")
        self.result = "\n".join(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask397BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
