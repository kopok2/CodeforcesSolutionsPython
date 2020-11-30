class CodeforcesTask828BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.square = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.square.append(input())

    def process_task(self):
        bxmax = bymax = 0
        bxmin = bymin = max(self.n_m) + 1
        blacks = 0
        for x in range(self.n_m[0]):
            for y in range(self.n_m[1]):
                if self.square[x][y] == "B":
                    blacks += 1
                    bxmin = min(bxmin, x)
                    bxmax = max(bxmax, x)
                    bymin = min(bymin, y)
                    bymax = max(bymax, y)
        side = 1 + max((bxmax - bxmin), (bymax - bymin))
        if side > min(self.n_m):
            self.result = "-1"
        elif side < 0:
            self.result = "1"
        else:
            self.result = str((side ** 2) - blacks)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask828BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
