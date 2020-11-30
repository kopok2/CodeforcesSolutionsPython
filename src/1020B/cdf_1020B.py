class CodeforcesTask1020BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.claims = []

    def read_input(self):
        self.n = int(input())
        self.claims = [int(x) for x in input().split(" ")]

    def process_task(self):
        result = []
        for n in range(self.n):
            holes = [0] * self.n
            visiting = n
            while not holes[visiting]:
                holes[visiting] += 1
                visiting = self.claims[visiting] - 1
            result.append(visiting + 1)
        self.result = " ".join([str(x) for x in result])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1020BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
