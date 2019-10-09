class CodeforcesTask330BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.constraints = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.constraints.append([int(y) for y in input().split(" ")])

    def process_task(self):
        poss = set([x + 1 for x in range(self.n_m[0])])
        for cons in self.constraints:
            if cons[0] in poss:
                poss.remove(cons[0])
            if cons[1] in poss:
                poss.remove(cons[1])
        chosen = poss.pop()
        result = []
        for x in range(self.n_m[0]):
            if x + 1 != chosen:
                result.append("{0} {1}".format(chosen, x + 1))
        self.result = "{0}\n{1}".format(self.n_m[0] - 1, "\n".join(result))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask330BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
