class CodeforcesTask675BSolution:
    def __init__(self):
        self.result = ''
        self.n_a_b_c_d = []

    def read_input(self):
        self.n_a_b_c_d = [int(x) for x in input().split(" ")]

    def process_task(self):
        result = 0
        for x in range(1, self.n_a_b_c_d[0] + 1):
            y = self.n_a_b_c_d[2] - self.n_a_b_c_d[3] + x
            w = self.n_a_b_c_d[1] - self.n_a_b_c_d[4] + x
            q = self.n_a_b_c_d[2] - self.n_a_b_c_d[3] + w
            if 1 <= y <= self.n_a_b_c_d[0] and 1 <= w <= self.n_a_b_c_d[0] and 1 <= q <= self.n_a_b_c_d[0]:
                result += 1
                #print(x, y, w, q)
        self.result = str(result * (self.n_a_b_c_d[0]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask675BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
