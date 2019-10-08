from collections import deque


def flood(board, pos):
    result = []
    if not board[pos[0]][pos[1]]:
        board[pos[0]][pos[1]] = 1
        if pos[0] > 0:
            result.append((board, (pos[0] - 1, pos[1])))
        if pos[1] > 0:
            result.append((board, (pos[0], pos[1] - 1)))
            if pos[0] > 0:
                result.append((board, (pos[0] - 1, pos[1] - 1)))
            if pos[0] < len(board) - 1:
                result.append((board, (pos[0] + 1, pos[1] - 1)))
        if pos[0] < len(board) - 1:
            result.append((board, (pos[0] + 1, pos[1])))
        if pos[1] < len(board) - 1:
            result.append((board, (pos[0], pos[1] + 1)))
            if pos[0] > 0:
                result.append((board, (pos[0] - 1, pos[1] + 1)))
            if pos[0] < len(board) - 1:
                result.append((board, (pos[0] + 1, pos[1] + 1)))
    return result


class CodeforcesTask1033ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.king = []
        self.queen = []
        self.target = []

    def read_input(self):
        self.n = int(input())
        self.king = [int(x) for x in input().split(" ")]
        self.queen = [int(x) for x in input().split(" ")]
        self.target = [int(x) for x in input().split(" ")]

    def process_task(self):
        board = [[0] * self.n for x in range(self.n)]
        self.queen = self.queen[::-1]
        self.target = self.target[::-1]
        self.king = self.king[::-1]
        self.king, self.queen = self.queen, self.king
        for x in range(self.n):
            board[self.queen[0] - 1][x] = -1
            board[x][self.queen[1] - 1] = -1
        x, y = self.queen
        while 0 <= x - 1 < self.n and 0 <= y - 1 < self.n:
            board[x - 1][y - 1] = -1
            x += 1
            y += 1
        x, y = self.queen
        while 0 <= x - 1 < self.n and 0 <= y - 1 < self.n:
            board[x - 1][y - 1] = -1
            x -= 1
            y -= 1
        x, y = self.queen
        while 0 <= x - 1 < self.n and 0 <= y - 1 < self.n:
            board[x - 1][y - 1] = -1
            x -= 1
            y += 1
        x, y = self.queen
        while 0 <= x - 1 < self.n and 0 <= y - 1 < self.n:
            board[x - 1][y - 1] = -1
            x += 1
            y -= 1
        to_flood = deque([(board, (self.king[0] - 1, self.king[1] - 1))])
        while to_flood:
            flooding = to_flood.popleft()
            to_flood.extend(flood(*flooding))

        self.result = "YES" if board[self.target[0] - 1][self.target[1] - 1] == 1 else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1033ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
