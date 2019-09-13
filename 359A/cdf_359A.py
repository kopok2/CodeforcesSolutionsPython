class CodeforcesTask359ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.board = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.board.append([int(y) for y in input().split(" ")])

    def process_task(self):
        if 1 in self.board[0] or 1 in self.board[-1]:
            self.result = "2"
        elif 1 in [x[0] for x in self.board] or 1 in [x[-1] for x in self.board]:
            self.result = "2"
        else:
            self.result = "4"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask359ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
