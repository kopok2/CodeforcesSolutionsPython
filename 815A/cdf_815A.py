class CodeforcesTask815ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.board = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.board.append([int(y) for y in input().split(" ")])

    def process_task(self):
        columns = []
        for x in range(self.n_m[1]):
            column = []
            for y in range(self.n_m[0]):
                column.append(self.board[y][x])
            columns.append(column)

        left_board_moves = [min(row) for row in self.board]
        bottom_board_moves = [min(column) for column in columns]
        reduce1 = min(bottom_board_moves)
        reduce2 = min(left_board_moves)
        if reduce1 * self.n_m[0] > reduce2 * self.n_m[1]:
            left_board_moves = [x - reduce1 for x in left_board_moves]
        else:
            bottom_board_moves = [x - reduce2 for x in bottom_board_moves]
        moves = sum(left_board_moves) + sum(bottom_board_moves)
        board_score = sum(left_board_moves) * self.n_m[1] + sum(bottom_board_moves) * self.n_m[0]
        real_board_score = sum([sum(x) for x in self.board])
        if board_score != real_board_score:
            self.result = "-1"
        else:
            print("{0}".format(moves))
            for x in range(self.n_m[0]):
                for y in range(left_board_moves[x]):
                    print("row {0}".format(x + 1))
            for x in range(self.n_m[1]):
                for y in range(bottom_board_moves[x]):
                    print("col {0}".format(x + 1))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask815ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
