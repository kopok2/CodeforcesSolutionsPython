class CodeforcesTask1092ASolution:
    def __init__(self):
        self.result = ''
        self.t = 0
        self.queries = []

    def read_input(self):
        self.t = int(input())
        for x in range(self.t):
            self.queries.append([int(y) for y in input().split(" ")])

    def process_task(self):
        results = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for query in self.queries:
            r = alphabet[:query[1]] * (query[0] // query[1]) + alphabet[:query[0] % query[1]]
            results.append(r)
        self.result = "\n".join(results)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1092ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
