class CodeforcesTask544BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.n_k[0] % 2:
            m = (self.n_k[0] // 2 + 1) ** 2
            l = (self.n_k[0] // 2) ** 2
            max_islands = m + l
        else:
            max_islands = 2 * ((self.n_k[0] // 2) ** 2)
        if self.n_k[1] > max_islands:
            self.result = "NO"
        else:
            to_add = self.n_k[1]
            m = True
            x = 0
            y = 0
            map = [["S" for i in range(self.n_k[0])] for j in range(self.n_k[0])]
            while to_add:
                map[y][x] = "L"
                x += 2
                if x >= self.n_k[0]:
                    m = not m
                    x = 0 if m else 1

                    y += 1
                to_add -= 1
            self.result = "YES\n{0}".format("\n".join(["".join(row) for row in map]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask544BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
