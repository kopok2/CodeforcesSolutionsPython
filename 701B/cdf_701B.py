class CodeforcesTask701BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.positions = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.positions.append([int(y) for y in input().split(" ")])

    def process_task(self):
        colcnt = 0
        rowcnt = 0
        n = self.n_m[0]
        rows = [0] * n
        cols = [0] * n
        results = []
        for rook in self.positions:
            if not rows[rook[0] - 1]:
                rows[rook[0] - 1] = 1
                rowcnt += 1
            if not cols[rook[1] - 1]:
                cols[rook[1] - 1] = 1
                colcnt += 1
            results.append((n - rowcnt) * (n - colcnt))
        self.result = " ".join([str(x) for x in results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask701BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
