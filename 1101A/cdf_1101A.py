class CodeforcesTask1101ASolution:
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
            x = query[2]
            if x < query[0]:
                results.append(x)
            else:
                x = query[2] * (query[1] // query[2] + 1)
                results.append(x)
        self.result = "\n".join([str(x) for x in results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1101ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
