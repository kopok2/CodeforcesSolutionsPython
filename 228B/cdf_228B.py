class CodeforcesTask228BSolution:
    def __init__(self):
        self.result = ''
        self.n1_m1 = []
        self.matrix1 = []
        self.n2_m2 = []
        self.matrix2 = []

    def read_input(self):
        self.n1_m1 = [int(x) for x in input().split(" ")]
        for x in range(self.n1_m1[0]):
            self.matrix1.append([int(y) for y in input()])
        self.n2_m2 = [int(x) for x in input().split(" ")]
        for x in range(self.n2_m2[0]):
            self.matrix2.append([int(y) for y in input()])

    def process_task(self):
        mx_factor = 0
        mx_choose = (0, 0)
        for x in range(-50, 51):
            for y in range(-50, 51):
                factor = 0
                for i in range(self.n1_m1[0]):
                    if 0 <= i + x < self.n2_m2[0]:
                        for j in range(self.n1_m1[1]):
                            if 0 <= j + y < self.n2_m2[1]:
                                factor += self.matrix1[i][j] * self.matrix2[x + i][y + j]
                if factor > mx_factor:
                    mx_factor = factor
                    mx_choose = (x, y)
        self.result = "{0} {1}".format(*mx_choose)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask228BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
