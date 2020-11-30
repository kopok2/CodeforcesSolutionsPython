class CodeforcesTask1133ASolution:
    def __init__(self):
        self.result = ''
        self.h1 = []
        self.h2 = []

    def read_input(self):
        self.h1 = [int(x) for x in input().split(":")]
        self.h2 = [int(x) for x in input().split(":")]

    def process_task(self):
        h1 = self.h1[0] * 60 + self.h1[1]
        h2 = self.h2[0] * 60 + self.h2[1]
        mid = (h1 + h2) / 2
        h_mid = int(mid // 60)
        m_mid = int(mid % 60)
        self.result = "{:02d}:{:02d}".format(h_mid, m_mid)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1133ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
