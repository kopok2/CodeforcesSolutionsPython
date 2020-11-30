class CodeforcesTask369ASolution:
    def __init__(self):
        self.result = ''
        self.n_m_k = []
        self.plan = []

    def read_input(self):
        self.n_m_k = [int(x) for x in input().split(" ")]
        self.plan = [int(x) for x in input().split(" ")]

    def process_task(self):
        cleans = 0
        bowls, plates = self.n_m_k[1], self.n_m_k[2]
        for day in self.plan:
            if day == 1:
                if bowls:
                    bowls -= 1
                else:
                    cleans += 1
            else:
                if plates:
                    plates -= 1
                elif bowls:
                    bowls -= 1
                else:
                    cleans += 1
        self.result = str(cleans)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask369ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
