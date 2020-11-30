def is_full(board, x, y):
    for a in range(3):
        for b in range(3):
            if board[x * 3 + a][y * 3 + b] not in ["o", "x"]:
                return False
    return True


def fill_board(board, exclude, x, y):
    if exclude:
        for a in range(9):
            for b in range(9):
                if not ((x * 3 <= a <= x * 3 + 2) and (y * 3 <= b <= y * 3 + 2)):
                    if board[a][b] not in ["o", "x"]:
                        board[a][b] = "!"
    else:
        for a in range(3):
            for b in range(3):
                if board[x * 3 + a][y * 3 + b] not in ["o", "x"]:
                    board[x * 3 + a][y * 3 + b] = "!"


class CodeforcesTask907BSolution:
    def __init__(self):
        self.result = ''
        self.board = []
        self.last_move = []

    def read_input(self):
        for x in range(11):
            in_ = input()
            if in_:
                self.board.append(list(in_.replace(" ", "")))
        self.last_move = [int(x) for x in input().split(" ")]

    def process_task(self):
        fill_board(self.board, is_full(self.board, *[(x - 1) % 3 for x in self.last_move]),
                   *[(x - 1) % 3 for x in self.last_move])
        out_board = [" ".join(["".join(x) for x in [row[:3], row[3:6], row[6:]]]) for row in self.board]
        out_board = out_board[:3] + [""] + out_board[3:6] + [""] + out_board[6:]
        self.result = "\n".join(out_board)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask907BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
