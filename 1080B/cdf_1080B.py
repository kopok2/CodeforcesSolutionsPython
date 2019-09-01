class CodeforcesTask1080BSolution:
    def __init__(self):
        self.result = ''
        self.q = 0
        self.queries = []

    def read_input(self):
        self.q = int(input())
        for x in range(self.q):
            self.queries.append([int(y) for y in input().split(" ")])

    def process_task(self):
        results = []
        for query in self.queries:
            if query[0] == query[1]:
                results.append(query[0] if not query[0] % 2 else - query[0])
            elif query[0] % 2 and query[1] % 2:
                results.append(-query[0] + (-1) * ((query[1] - query[0]) // 2))
            elif query[0] % 2 and not query[1] % 2:
                results.append((query[1] - query[0] + 1) // 2)
            elif not query[0] % 2 and query[1] % 2:
                results.append(- (query[1] - query[0]) // 2)
            else:
                results.append(query[0] + (query[1] - query[0]) // 2)
        self.result = "\n".join([str(x) for x in results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1080BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
