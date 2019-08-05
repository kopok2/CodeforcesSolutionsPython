class CodeforcesTask752ASolution:
    def __init__(self):
        self.result = ''
        self.n_m_k = []

    def read_input(self):
        self.n_m_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        lane = (self.n_m_k[2] - 1) // (2 * self.n_m_k[1]) + 1
        row = (self.n_m_k[2] + 1 - (2 * self.n_m_k[1] * (lane - 1))) // 2
        position = "L" if self.n_m_k[2] % 2 else "R"
        self.result = "{0} {1} {2}".format(lane, row, position)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask752ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
