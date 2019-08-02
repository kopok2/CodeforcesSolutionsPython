class CodeforcesTask330ASolution:
    def __init__(self):
        self.result = ''
        self.r_c = []
        self.cake = []

    def read_input(self):
        self.r_c = [int(x) for x in input().split(" ")]
        for r in range(self.r_c[0]):
            self.cake.append(list(input()))

    def process_task(self):
        for r in range(self.r_c[0]):
            for c in range(self.r_c[1]):
                if self.cake[r][c] == "S":
                    for x in range(self.r_c[0]):
                        if self.cake[x][c] == ".":
                            self.cake[x][c] = "r"
                        elif self.cake[x][c] == "s":
                            self.cake[x][c] = "S"
                    for y in range(self.r_c[1]):
                        if self.cake[r][y] == ".":
                            self.cake[r][y] = "s"
                        elif self.cake[r][y] == "r":
                            self.cake[r][y] = "S"
        self.result = str(self.r_c[0] * self.r_c[1] - ("".join(["".join(x) for x in self.cake])).count("S"))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask330ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
