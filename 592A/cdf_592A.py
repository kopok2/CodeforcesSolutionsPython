class CodeforcesTask592ASolution:
    def __init__(self):
        self.result = ''
        self.board = []

    def read_input(self):
        for x in range(8):
            self.board.append(input())

    def process_task(self):
        amin = 8
        bmin = 8
        n_board = []
        for x in range(8):
            line = ''
            for y in range(8):
                line += self.board[y][x]
            n_board.append(line)
        for b in n_board:
            if "B" in b:
                if "W" not in b.split("B")[-1]:
                    #print(b, b.split("B")[-1])
                    bmin = min(bmin, len(b.split("B")[-1]))
            if "W" in b:
                if "B" not in b.split("W")[0]:
                    #print(b, b.split("W")[0])
                    amin = min(amin, len(b.split("W")[0]))
        self.result = "A" if amin <= bmin else "B"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask592ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
