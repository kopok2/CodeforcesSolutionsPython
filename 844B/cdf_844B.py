import math


def choose(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


class CodeforcesTask844BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.board = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.board.append([int(x) for x in input().split(" ")])

    def process_task(self):
        white_row_sums = [sum(row) for row in self.board]
        black_row_sums = [self.n_m[1] - row for row in white_row_sums]
        white_col_sums = [0] * self.n_m[1]
        for x in range(self.n_m[1]):
            for y in range(self.n_m[0]):
                white_col_sums[x] += self.board[y][x]
        black_col_sums = [self.n_m[0] - row for row in white_col_sums]
        subsets = white_row_sums + black_row_sums + white_col_sums + black_col_sums
        sub_cnt = 0
        for ss in subsets:
            sub_cnt += 2 ** ss - 1
        self.result = str(int(sub_cnt - self.n_m[0] * self.n_m[1]))


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask844BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
