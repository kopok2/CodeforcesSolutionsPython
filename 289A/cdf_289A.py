class CodeforcesTask289ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.segments = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        for x in range(self.n_k[0]):
            self.segments.append([int(x) for x in input().split(" ")])

    def process_task(self):
        curr = 0
        for seg in self.segments:
            curr += seg[1] - seg[0] + 1
        moves = self.n_k[1] - curr % self.n_k[1]
        if moves == self.n_k[1]:
            moves = 0
        self.result = str(moves)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask289ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
