def all_parked(parked):
    result = True
    for p in parked:
        result = result and p
    return result


class CodeforcesTask995ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.parking = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        for x in range(4):
            self.parking.append([int(y) for y in input().split(" ")])

    def process_task(self):
        parked = [False for x in range(self.n_k[1])]
        moves = []
        for x in range(self.n_k[0]):
            if self.parking[0][x] == self.parking[1][x] and self.parking[1][x]:
                moves.append([self.parking[0][x], 1, x + 1])
                self.parking[1][x] = 0
                parked[self.parking[0][x] - 1] = True
            if self.parking[3][x] == self.parking[2][x] and self.parking[3][x]:
                moves.append([self.parking[3][x], 4, x + 1])
                self.parking[2][x] = 0
                parked[self.parking[3][x] - 1] = True
        if sum([1 if not x else 0 for x in parked]) == self.n_k[1] and self.n_k[1] == self.n_k[0] * 2:
            self.result = "-1"
        else:
            while not all_parked(parked):
                moved = [False for x in range(self.n_k[0])]
                #for p in self.parking:
                #    print(p)
                #print("\n")
                #print(moves)
                if self.parking[1][0] and not self.parking[2][0]:
                    moves.append([self.parking[1][0], 3, 1])
                    self.parking[2][0] = self.parking[1][0]
                    self.parking[1][0] = 0
                    moved[0] = True
                for x in range(1, self.n_k[0]):
                    if not self.parking[1][x - 1] and self.parking[1][x]:
                        moves.append([self.parking[1][x], 2, x])
                        self.parking[1][x - 1] = self.parking[1][x]
                        self.parking[1][x] = 0
                if not self.parking[1][self.n_k[0] - 1] and self.parking[2][self.n_k[0] - 1] and not moved[self.n_k[0] - 1]:
                    moves.append([self.parking[2][self.n_k[0] - 1], 2, self.n_k[0]])
                    self.parking[1][self.n_k[0] - 1] = self.parking[2][self.n_k[0] - 1]
                    self.parking[2][self.n_k[0] - 1] = 0
                for x in range(self.n_k[0] - 1):
                    if not self.parking[2][x + 1] and self.parking[2][x] and not moved[x]:
                        moves.append([self.parking[2][x], 3, x + 2])
                        self.parking[2][x + 1] = self.parking[2][x]
                        self.parking[2][x] = 0
                        moved[x + 1] = True
                for x in range(self.n_k[0]):
                    if self.parking[0][x] == self.parking[1][x] and self.parking[1][x]:
                        moves.append([self.parking[0][x], 1, x + 1])
                        self.parking[1][x] = 0
                        parked[self.parking[0][x] - 1] = True
                    if self.parking[3][x] == self.parking[2][x] and self.parking[3][x]:
                        moves.append([self.parking[3][x], 4, x + 1])
                        self.parking[2][x] = 0
                        parked[self.parking[3][x] - 1] = True
            self.result = "{0}\n{1}".format(len(moves), "\n".join([" ".join([str(x) for x in move]) for move in moves]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask995ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
