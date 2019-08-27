class CodeforcesTask604BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.boxes = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.boxes = [int(x) for x in input().split(" ")]

    def process_task(self):
        x = 2 * (self.n_k[0] - self.n_k[1])
        boxed = []
        for y in range(x // 2):
            boxed.append(self.boxes[y] + self.boxes[x - y - 1])
        if x > 0:
            self.result = str(max(self.boxes[-1], max(boxed)))
        else:
            self.result = str(self.boxes[-1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask604BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
