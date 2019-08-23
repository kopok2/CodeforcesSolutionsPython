class CodeforcesTask1106ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.matrix = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.matrix.append(input())

    def process_task(self):
        crosses = 0
        for y in range(1, self.n - 1):
            for x in range(1, self.n - 1):
                if self.matrix[y][x] == "X":
                    if self.matrix[y - 1][x - 1] == "X":
                        if self.matrix[y - 1][x + 1] == "X":
                            if self.matrix[y + 1][x - 1] == "X":
                                if self.matrix[y + 1][x + 1] == "X":
                                    crosses += 1
        self.result = str(crosses)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1106ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
