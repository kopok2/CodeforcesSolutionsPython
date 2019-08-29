class CodeforcesTask1058BSolution:
    def __init__(self):
        self.result = ''
        self.n_d = []
        self.m = 0
        self.hoppers = []

    def read_input(self):
        self.n_d = [int(x) for x in input().split(" ")]
        self.m = int(input())
        for x in range(self.m):
            self.hoppers.append([int(y) for y in input().split(" ")])

    def process_task(self):
        in_field = [[False for x in range(self.n_d[0] + 1)] for y in range(self.n_d[0] + 1)]
        for s in range(self.n_d[1]):
            for x in range(self.n_d[0] - self.n_d[1] + 1):
                in_field[self.n_d[1] - s + x][s + x] = True
            for x in range(self.n_d[0] - self.n_d[1]):
                in_field[self.n_d[1] - s + x][s + x + 1] = True
        for x in range(self.n_d[0] - self.n_d[1] + 1):
            s = self.n_d[1]
            in_field[self.n_d[1] - s + x][s + x] = True
        for hopper in self.hoppers:
            res = "YES" if in_field[hopper[0]][hopper[1]] else "NO"
            print(res)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1058BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
