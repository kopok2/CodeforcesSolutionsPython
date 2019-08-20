class CodeforcesTask975BSolution:
    def __init__(self):
        self.result = ''
        self.mancala = []

    def read_input(self):
        self.mancala = [int(x) for x in input().split(" ")]

    def process_task(self):
        mx = 0
        for move in range(14):
            taken = self.mancala[move]
            n_board = self.mancala[::]
            n_board[move] = 0
            adding = taken // 14
            n_board = [x + adding for x in n_board]
            taken = taken % 14
            move += 1
            move = move % 14
            while taken:
                n_board[move] += 1
                taken -= 1
                move += 1
                move = move % 14
            mx = max(mx, sum([x for x in n_board if not x % 2]))
        self.result = str(mx)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask975BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
