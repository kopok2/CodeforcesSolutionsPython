class CodeforcesTask735BSolution:
    def __init__(self):
        self.result = ''
        self.nnn = []
        self.candidates = []

    def read_input(self):
        self.nnn = [int(x) for x in input().split(" ")]
        self.candidates = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.candidates.sort(reverse=True)
        nm = min(self.nnn[1], self.nnn[2])
        nx = max(self.nnn[1], self.nnn[2])
        mean1 = sum(self.candidates[:nm]) / nm
        mean2 = sum(self.candidates[nm:nm + nx]) / nx
        sum_means = mean1 + mean2
        self.result = str(sum_means)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask735BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
