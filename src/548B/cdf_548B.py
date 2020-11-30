class CodeforcesTask548BSolution:
    def __init__(self):
        self.result = ''
        self.n_m_q = []
        self.grid = []
        self.actions = []

    def read_input(self):
        self.n_m_q = [int(x) for x in input().split(" ")]
        for _ in range(self.n_m_q[0]):
            self.grid.append([int(y) for y in input().split(" ")])
        for _ in range(self.n_m_q[2]):
            self.actions.append([int(y) for y in input().split(" ")])

    def process_task(self):
        maxes = [0] * self.n_m_q[0]
        for row in range(self.n_m_q[0]):
            mx = 0
            cr = 0
            for y in range(self.n_m_q[1]):
                if self.grid[row][y]:
                    cr += 1
                    mx = max(mx, cr)
                else:
                    cr = 0
            maxes[row] = mx
        res = []
        for action in self.actions:
            self.grid[action[0] - 1][action[1] - 1] = 0 if self.grid[action[0] - 1][action[1] - 1] else 1
            mx = 0
            cr = 0
            for y in range(self.n_m_q[1]):
                if self.grid[action[0] - 1][y]:
                    cr += 1
                    mx = max(mx, cr)
                else:
                    cr = 0
            maxes[action[0] - 1] = mx
            res.append(str(max(maxes)))
        self.result = "\n".join(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask548BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
