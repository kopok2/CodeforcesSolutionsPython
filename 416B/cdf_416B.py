class CodeforcesTask416BSolution:
    def __init__(self):
        self.result = ''
        self.m_n = []
        self.pictures = []

    def read_input(self):
        self.m_n = [int(x) for x in input().split(" ")]
        for x in range(self.m_n[0]):
            self.pictures.append([int(y) for y in input().split(" ")])

    def process_task(self):
        if self.m_n[0] > 1:
            # first painter
            for x in range(self.m_n[0] - 1):
                self.pictures[x + 1][0] += self.pictures[x][0]
            for n in range(self.m_n[1] - 1):
                self.pictures[0][n + 1] += self.pictures[0][n]
            for n in range(self.m_n[1] - 1):
                for x in range(self.m_n[0] - 1):
                    self.pictures[x + 1][n + 1] += max(self.pictures[x][n + 1], self.pictures[x + 1][n])
            for x in range(self.m_n[0]):
                print(self.pictures[x][self.m_n[1] - 1], end=" ")
        else:
            self.result = str(sum(self.pictures[0]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask416BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
