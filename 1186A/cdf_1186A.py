class CodeforcesTask1186ASolution:
    def __init__(self):
        self.result = ''
        self.n_m_k = []

    def read_input(self):
        self.n_m_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.result = "Yes" if self.n_m_k[0] <= min(self.n_m_k[1], self.n_m_k[2]) else "No"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1186ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
