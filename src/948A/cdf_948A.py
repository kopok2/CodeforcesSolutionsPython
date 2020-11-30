class CodeforcesTask948ASolution:
    def __init__(self):
        self.result = ''
        self.pasture_dims = []
        self.pasture = []

    def read_input(self):
        self.pasture_dims = [int(x) for x in input().split(" ")]
        for x in range(self.pasture_dims[0]):
            self.pasture.append(list(input()))

    def process_task(self):
        can = True
        for r in range(self.pasture_dims[0]):
            for c in range(self.pasture_dims[1]):
                if self.pasture[r][c] == "S":
                    if r > 0:
                        if self.pasture[r - 1][c] == "W":
                            can = False
                        elif self.pasture[r - 1][c] == ".":
                            self.pasture[r - 1][c] = "D"
                    if r < self.pasture_dims[0] - 1:
                        if self.pasture[r + 1][c] == "W":
                            can = False
                        elif self.pasture[r + 1][c] == ".":
                            self.pasture[r + 1][c] = "D"
                    if c > 0:
                        if self.pasture[r][c - 1] == "W":
                            can = False
                        elif self.pasture[r][c - 1] == ".":
                            self.pasture[r][c - 1] = "D"
                    if c < self.pasture_dims[1] - 1:
                        if self.pasture[r][c + 1] == "W":
                            can = False
                        elif self.pasture[r][c + 1] == ".":
                            self.pasture[r][c + 1] = "D"
        if not can:
            print("No")
        else:
            print("Yes")
            for row in self.pasture:
                print("".join(row))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask948ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
