class CodeforcesTask370ASolution:
    def __init__(self):
        self.result = ''
        self.cords = []

    def read_input(self):
        self.cords = [int(x) for x in input().split(" ")]

    def process_task(self):
        h = abs(self.cords[2] - self.cords[0])
        v = abs(self.cords[3] - self.cords[1])
        if self.cords[0] == self.cords[2] or self.cords[1] == self.cords[3]:
            rook = 1
        else:
            rook = 2
        if (self.cords[0] + self.cords[1]) % 2 != (self.cords[2] + self.cords[3]) % 2:
            bishop = 0
        elif h == v:
            bishop = 1
        else:
            bishop = 2
        king = max(h, v)
        self.result = "{0} {1} {2}".format(rook, bishop, king)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask370ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
