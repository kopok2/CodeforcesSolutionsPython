def calc_shift_cost(row):
    starts = [i for i, x in enumerate(row) if x]
    for start in starts:
        d = 2
        pos = start + 1
        if pos == len(row):
            pos = 0
        while row[pos] != 1:
            if row[pos]:
                row[pos] = min(row[pos], d)
            else:
                row[pos] = d
            d += 1
            pos += 1
            if pos == len(row):
                pos = 0
        d = 2
        pos = start - 1
        if pos == -1:
            pos = len(row) - 1
        while row[pos] != 1:
            if row[pos]:
                row[pos] = min(row[pos], d)
            else:
                row[pos] = d
            d += 1
            pos -= 1
            if pos == -1:
                pos = len(row) - 1
    for x in range(len(row)):
        row[x] -= 1


class CodeforcesTask229ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.board = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.board.append([int(x) for x in input()])

    def process_task(self):
        for row in self.board:
            if sum(row):
                calc_shift_cost(row)
            else:
                self.result = "-1"
                break
        if not self.result:
            costs = []
            for x in range(self.n_m[1]):
                ss = 0
                for y in range(self.n_m[0]):
                    ss += self.board[y][x]
                costs.append(ss)
            self.result = str(min(costs))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask229ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
