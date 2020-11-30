class CodeforcesTask1102BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.values = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.values = [int(x) for x in input().split(" ")]

    def process_task(self):
        colorings = [{self.values[x]} for x in range(self.n_k[1])]
        colors = [0] * self.n_k[0]
        for x in range(self.n_k[1]):
            colors[x] = x + 1
        can_ = True
        #print(colorings)
        for x in range(self.n_k[1], self.n_k[0]):
            has_ = False
            for y in range(self.n_k[1]):
                #print(x, y, colorings)
                if self.values[x] not in colorings[y]:
                    colorings[y].add(self.values[x])
                    colors[x] = y + 1
                    has_ = True
                    break
            if not has_:
                can_ = False
                break
        if can_:
            self.result = "YES\n{0}".format(" ".join([str(x) for x in colors]))
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1102BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
