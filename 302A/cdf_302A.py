class CodeforcesTask302ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.array = []
        self.queries = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.array = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.queries.append([int(y) for y in input().split(" ")])

    def process_task(self):
        ones = 0
        for x in self.array:
            if x == 1:
                ones += 1
        zeros = self.n_m[0] - ones
        mn = min(ones, zeros)
        for query in self.queries:
            j = (query[1] - query[0] + 1)
            if j % 2:
                print("0")
            elif j // 2 <= mn:
                print("1")
            else:
                print("0")

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask302ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
