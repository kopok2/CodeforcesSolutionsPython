class CodeforcesTask657ASolution:
    def __init__(self):
        self.result = ''
        self.n_d_h = []

    def read_input(self):
        self.n_d_h = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.n_d_h[2] * 2 < self.n_d_h[1] or self.n_d_h[0] + 1 < self.n_d_h[1] or (self.n_d_h[0] > 2 and self.n_d_h[1] == 1):
            self.result = "-1"
        else:
            vertices = []
            t_b_p = self.n_d_h[0] - 1
            if self.n_d_h[1] >= self.n_d_h[2]:
                f_b_l = self.n_d_h[2]
                f_b_r = self.n_d_h[1] - self.n_d_h[2]
            else:
                f_b_l = self.n_d_h[2]
                f_b_r = 0
            cr = 1
            for _ in range(f_b_l):
                vertices.append("{0} {1}".format(cr, cr + 1))
                cr += 1
                t_b_p -= 1
            for i in range(f_b_r):
                if not i:
                    vertices.append("{0} {1}".format(1, cr + 1))
                else:
                    vertices.append("{0} {1}".format(cr, cr + 1))
                t_b_p -= 1
                cr += 1
            for _ in range(t_b_p):
                if self.n_d_h[2] > 1:
                    vertices.append("2 {0}".format(cr + 1))
                else:
                    vertices.append("1 {0}".format(cr + 1))
                cr += 1

            self.result = "\n".join(vertices)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask657ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
