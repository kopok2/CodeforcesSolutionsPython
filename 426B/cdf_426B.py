class CodeforcesTask426BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.matrix = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.matrix.append([int(y) for y in input().split(" ")])

    def process_task(self):
        size = self.n_m[0]
        while not size % 2:
            mirrorify = True
            for x in range(size // 2):
                if self.matrix[x] != self.matrix[size - x - 1]:
                    mirrorify = False
                    break
            if not mirrorify:
                break
            else:
                size //= 2
        self.result = str(size)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask426BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
