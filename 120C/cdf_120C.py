class CodeforcesTask120CSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.jars = []

    def read_input(self):
        in_ = open("input.txt").read().split("\n")
        self.n_k = [int(x) for x in in_[0].split(" ")]
        self.jars = [int(x) for x in in_[1].split(" ")]

    def process_task(self):
        jars = [x - min((x // self.n_k[1]) * self.n_k[1], self.n_k[1] * 3) for x in self.jars]
        self.result = str(sum(jars))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask120CSolution()
    Solution.read_input()
    Solution.process_task()
    open("output.txt", "w").write(Solution.get_result())
