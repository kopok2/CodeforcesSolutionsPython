class CodeforcesTask57ASolution:
    def __init__(self):
        self.result = ''
        self.n_cords = []

    def read_input(self):
        self.n_cords = [int(x) for x in input().split(" ")]

    def process_task(self):
        n = self.n_cords[0]
        x1 = self.n_cords[1]
        y1 = self.n_cords[2]
        x2 = self.n_cords[3]
        y2 = self.n_cords[4]
        if not x1:
            path1 = 4 * n - y1
        else:
            if not y1:
                path1 = x1
            else:
                if y1 < n:
                    path1 = x1 + y1
                else:
                    path1 = 4 * n - x1 - y1
        if not x2:
            path2 = 4 * n - y2
        else:
            if not y2:
                path2 = x2
            else:
                if y2 < n:
                    path2 = x2 + y2
                else:
                    path2 = 4 * n - x2 - y2
        diff1 = path1 - path2
        diff2 = 4 * n - diff1
        diff1 = diff1 % (4 * n)
        diff2 = diff2 % (4 * n)
        self.result = str(abs(min(diff1, diff2)))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask57ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
