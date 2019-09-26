class CodeforcesTask729BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.plan = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.plan.append([int(y) for y in input().split(" ")])

    def process_task(self):
        left_rows = [[0] * self.n_m[1] for x in range(self.n_m[0])]
        right_rows = [[0] * self.n_m[1] for x in range(self.n_m[0])]
        top_cols = [[0] * self.n_m[1] for x in range(self.n_m[0])]
        bottom_cols = [[0] * self.n_m[1] for x in range(self.n_m[0])]

        for y in range(self.n_m[0]):
            left_rows[y][0] = self.plan[y][0]
        for x in range(1, self.n_m[1]):
            for y in range(self.n_m[0]):
                left_rows[y][x] = self.plan[y][x] + left_rows[y][x - 1]

        for y in range(self.n_m[0]):
            right_rows[y][-1] = self.plan[y][-1]
        for x in range(self.n_m[1] - 2, -1, -1):
            for y in range(self.n_m[0]):
                right_rows[y][x] = self.plan[y][x] + right_rows[y][x + 1]

        for x in range(self.n_m[1]):
            top_cols[0][x] = self.plan[0][x]
        for x in range(self.n_m[1]):
            for y in range(1, self.n_m[0]):
                top_cols[y][x] = self.plan[y][x] + top_cols[y - 1][x]

        for x in range(self.n_m[1]):
            bottom_cols[-1][x] = self.plan[-1][x]
        for x in range(self.n_m[1]):
            for y in range(self.n_m[0] - 2, -1, -1):
                bottom_cols[y][x] = self.plan[y][x] + bottom_cols[y + 1][x]

        """print("left")
        for r in left_rows:
            print(r)
        print("right")
        for r in right_rows:
            print(r)
        print("top")
        for r in top_cols:
            print(r)
        print("bottom")
        for r in bottom_cols:
            print(r)"""

        cnt = 0
        ways = [[0] * self.n_m[1] for x in range(self.n_m[0])]
        for x in range(self.n_m[1]):
            for y in range(self.n_m[0]):
                if not self.plan[y][x]:
                    if left_rows[y][x]:
                        cnt += 1
                        ways[y][x] += 1
                    if right_rows[y][x]:
                        cnt += 1
                        ways[y][x] += 1
                    if top_cols[y][x]:
                        cnt += 1
                        ways[y][x] += 1
                    if bottom_cols[y][x]:
                        cnt += 1
                        ways[y][x] += 1
        self.result = str(cnt)
        #print("ways")
        #for r in ways:
        #    print(r)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask729BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
