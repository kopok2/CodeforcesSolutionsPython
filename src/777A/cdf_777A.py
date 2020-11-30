class CodeforcesTask777ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.x = 0

    def read_input(self):
        self.n = int(input())
        self.x = int(input())

    def process_task(self):
        real_turn = self.n % 6
        moves = [[0, 1, 2], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1], [0, 2, 1]]
        self.result = str(moves[real_turn][self.x])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask777ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
