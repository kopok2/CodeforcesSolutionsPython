class CodeforcesTask90BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.crossword = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.crossword.append(input())

    def process_task(self):
        crossing = [[[c, True] for c in row] for row in self.crossword]
        for x in range(self.n_m[0]):
            for y in range(self.n_m[1]):
                #print(x, y)
                if self.crossword[x][y] in self.crossword[x][:y] + self.crossword[x][y + 1:]:
                    crossing[x][y][1] = False
                if self.crossword[x][y] in [self.crossword[z][y] for z in range(self.n_m[0]) if z != x]:
                    crossing[x][y][1] = False
        result = []
        for row in crossing:
            for c in row:
                if c[1]:
                    result.append(c[0])
        self.result = "".join(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask90BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
