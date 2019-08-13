class CodeforcesTask263BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.squares = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.squares = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.squares.sort(reverse=True)
        if self.n_k[1] > self.n_k[0]:
            self.result = "-1"
        elif self.n_k[1] == 1:
            self.result = "{0} {0}".format(self.squares[0])
        else:
            self.result = "{0} {0}".format(self.squares[self.n_k[1] - 1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask263BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
