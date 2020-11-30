class CodeforcesTask33ASolution:
    def __init__(self):
        self.result = ''
        self.n_m_k = []
        self.teeth = []

    def read_input(self):
        self.n_m_k = [int(x) for x in input().split(" ")]
        self.teeth = [[] for x in range(self.n_m_k[1])]
        for x in range(self.n_m_k[0]):
            t = [int(x) for x in input().split(" ")]
            self.teeth[t[0] - 1].append(t[1])

    def process_task(self):
        self.result = str(min(sum([min(x) for x in self.teeth]), self.n_m_k[2]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask33ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
