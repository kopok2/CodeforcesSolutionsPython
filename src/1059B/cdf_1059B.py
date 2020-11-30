def check_painted(c, r, g):
    res = True
    for i in range(3):
        for j in range(3):
            if not (i == 1 and j == 1):
                if not g[r - i][c - j] == "#":
                    res = False
    return res


class CodeforcesTask1059BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.grid = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        grid = []
        for _ in range(self.n_m[0]):
            grid.append(input())
        self.grid = grid

    def process_task(self):
        painted = [["."] * self.n_m[1] for _ in range(self.n_m[0])]
        for column in range(2, self.n_m[1]):
            for row in range(2, self.n_m[0]):
                if check_painted(column, row, self.grid):
                    for i in range(3):
                        for j in range(3):
                            if not (i == 1 and j == 1):
                                painted[row - i][column - j] = "#"

        res = True
        for r1, r2 in zip(painted, self.grid):
            if r2 != "".join(r1):
                res = False
                break
        self.result = "YES" if res else "NO"


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1059BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
