class CodeforcesTask1105BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.string = ''

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.string = input()

    def process_task(self):
        scores = [0] * 26
        prev = None
        prog = 0
        for x in range(self.n_k[0]):
            c = self.string[x]
            if prev == c:
                prog += 1
            else:
                prog = 1
            if prog == self.n_k[1]:
                scores[ord(c) - 97] += 1
                prog = 0
            prev = c
        self.result = str(max(scores))


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1105BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
