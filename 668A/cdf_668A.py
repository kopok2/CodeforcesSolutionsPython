class CodeforcesTask668ASolution:
    def __init__(self):
        self.result = ''
        self.n_m_q = []
        self.experiment = []

    def read_input(self):
        self.n_m_q = [int(x) for x in input().split(" ")]
        for x in range(self.n_m_q[2]):
            self.experiment.append([int(y) for y in input().split(" ")])

    def process_task(self):
        try:
            construction = self.experiment[::-1]
            matrix = [[0] * self.n_m_q[1] for x in range(self.n_m_q[0])]
            for con in construction:
                if con[0] == 1:
                    tmp = matrix[con[1] - 1][-1]
                    for x in range(self.n_m_q[1]):
                        tmp, matrix[con[1] - 1][x] = matrix[con[1] - 1][x], tmp
                elif con[0] == 2:
                    tmp = matrix[-1][con[1] - 1]
                    for x in range(self.n_m_q[0]):
                        tmp, matrix[x][con[1] - 1] = matrix[x][con[1] - 1], tmp
                elif con[0] == 3:
                    matrix[con[1] - 1][con[2] - 1] = con[3]
            self.result = "\n".join([" ".join([str(x) for x in row]) for row in matrix])
        except Exception as e:
            print(e, con, matrix)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask668ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
