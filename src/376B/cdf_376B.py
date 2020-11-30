class CodeforcesTask376BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.debts = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.debts.append([int(y) for y in input().split(" ")])

    def process_task(self):
        people_balance = [0] * self.n_m[0]
        for d in self.debts:
            people_balance[d[0] - 1] -= d[2]
            people_balance[d[1] - 1] += d[2]
        self.result = str(sum([abs(x) for x in people_balance]) // 2)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask376BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
