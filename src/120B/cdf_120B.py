class CodeforcesTask120BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.questions = []

    def read_input(self):
        in_ = open("input.txt").read().split("\n")
        self.n_k = [int(x) for x in in_[0].split(" ")]
        self.questions = [int(x) for x in in_[1].split(" ")]

    def process_task(self):
        x = self.n_k[1]
        while not self.questions[x - 1]:
            x += 1
            if x > self.n_k[0]:
                x = 1
        self.result = str(x)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask120BSolution()
    Solution.read_input()
    Solution.process_task()
    open("output.txt", "w").write(Solution.get_result())
