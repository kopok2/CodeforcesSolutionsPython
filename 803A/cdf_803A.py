class CodeforcesTask803ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.n_k[0] ** 2 < self.n_k[1]:
            self.result = "-1"
        else:
            matrix = [[0] * self.n_k[0] for x in range(self.n_k[0])]
            to_place = self.n_k[1]
            x = 0
            y = 0
            while to_place:
                if x == y:
                    matrix[x][y] = 1
                    to_place -= 1
                elif to_place > 1:
                    matrix[x][y] = 1
                    matrix[y][x] = 1
                    to_place -= 2
                x += 1
                if x >= self.n_k[0]:
                    y += 1
                    x = y

            self.result = "\n".join([" ".join([str(x) for x in row]) for row in matrix])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask803ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
