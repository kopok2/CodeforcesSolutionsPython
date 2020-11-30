class CodeforcesTask808BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.records = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.records = [int(x) for x in input().split(" ")]

    def process_task(self):
        ss = sum(self.records[:self.n_k[1]])
        avs = ss
        for x in range(self.n_k[0] - self.n_k[1]):
            ss += self.records[self.n_k[1] + x] - self.records[x]
            avs += ss
        self.result = str(avs / (self.n_k[0] - self.n_k[1] + 1))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask808BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
