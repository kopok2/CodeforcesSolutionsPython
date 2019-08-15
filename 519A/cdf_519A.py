class CodeforcesTask519ASolution:
    def __init__(self):
        self.result = ''
        self.board = ""

    def read_input(self):
        for x in range(8):
            self.board += input()

    def process_task(self):
        points = {"Q": 9, "R": 5, "B": 3, "N": 3, "P": 1, "K": 0, ".": 0,
                  "q": -9, "r": -5, "b": -3, "n": -3, "p": -1, "k": 0}
        result = 0
        for point in self.board:
            result += points[point]
        if not result:
            self.result = "Draw"
        elif result > 0:
            self.result = "White"
        else:
            self.result = "Black"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask519ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
