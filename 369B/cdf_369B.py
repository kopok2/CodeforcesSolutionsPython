class CodeforcesTask369BSolution:
    def __init__(self):
        self.result = ''
        self.n_k_l_r_sa_sk = []

    def read_input(self):
        self.n_k_l_r_sa_sk = [int(x) for x in input().split(" ")]

    def process_task(self):
        points = [self.n_k_l_r_sa_sk[2]] * self.n_k_l_r_sa_sk[0]
        score = self.n_k_l_r_sa_sk[2] * self.n_k_l_r_sa_sk[0]
        putin = self.n_k_l_r_sa_sk[5] - self.n_k_l_r_sa_sk[2] * self.n_k_l_r_sa_sk[1]
        pos = 0
        while putin:
            points[pos] += 1
            putin -= 1
            score += 1
            pos += 1
            if pos == self.n_k_l_r_sa_sk[1]:
                pos = 0
        rem = self.n_k_l_r_sa_sk[4] - score
        pos = self.n_k_l_r_sa_sk[1]
        while rem:
            points[pos] += 1
            rem -= 1
            pos += 1
            if pos == self.n_k_l_r_sa_sk[0]:
                pos = self.n_k_l_r_sa_sk[1]
        self.result = " ".join([str(x) for x in points])


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask369BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
