class CodeforcesTask157ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.board = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.board.append([int(y) for y in input().split(" ")])

    def process_task(self):
        hor_sums = [sum(x) for x in self.board]
        vert_sums = []
        for x in range(self.n):
            ss = 0
            for y in range(self.n):
                ss += self.board[y][x]
            vert_sums.append(ss)
        winning = 0
        for hor in hor_sums:
            for ver in vert_sums:
                if ver > hor:
                    winning += 1
        self.result = str(winning)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask157ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
