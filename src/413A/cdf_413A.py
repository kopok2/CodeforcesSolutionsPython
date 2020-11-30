class CodeforcesTask413ASolution:
    def __init__(self):
        self.result = ''
        self.n_m_min_max = []
        self.measurements = []

    def read_input(self):
        self.n_m_min_max = [int(x) for x in input().split(" ")]
        self.measurements = [int(x) for x in input().split(" ")]

    def process_task(self):
        if max(self.measurements) <= self.n_m_min_max[3] and min(self.measurements) >= self.n_m_min_max[2]:
            to_add = 0
            if self.n_m_min_max[3] not in self.measurements:
                to_add += 1
            if self.n_m_min_max[2] not in self.measurements:
                to_add += 1
            if self.n_m_min_max[0] - self.n_m_min_max[1] >= to_add:
                self.result = "Correct"
            else:
                self.result = "Incorrect"
        else:
            self.result = "Incorrect"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask413ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
