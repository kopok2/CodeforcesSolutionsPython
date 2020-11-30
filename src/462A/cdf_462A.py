class CodeforcesTask462ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.board = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.board.append(input())

    def process_task(self):
        adj = [[0] * self.n for x in range(self.n)]
        pos = True
        for x in range(self.n):
            for y in range(self.n):
                if x:
                    adj[x][y] += 1 if self.board[x - 1][y] == "o" else 0
                if y:
                    adj[x][y] += 1 if self.board[x][y - 1] == "o" else 0
                if x < self.n - 1:
                    adj[x][y] += 1 if self.board[x + 1][y] == "o" else 0
                if y < self.n - 1:
                    adj[x][y] += 1 if self.board[x][y + 1] == "o" else 0
                if adj[x][y] % 2:
                    pos = False
                    break
            if not pos:
                break
        self.result = "YES" if pos else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask462ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
