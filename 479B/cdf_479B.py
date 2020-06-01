class CodeforcesTask479BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.heights = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.heights = [int(x) for x in input().split(" ")]

    def process_task(self):
        res = []
        for _ in range(self.n_k[1]):
            from_i = self.heights.index(max(self.heights))
            to_i = self.heights.index(min(self.heights))
            if from_i == to_i:
                break
            self.heights[from_i] -= 1
            self.heights[to_i] += 1
            res.append((from_i + 1, to_i + 1))
        stab = max(self.heights) - min(self.heights)
        ops = "\n".join(" ".join([str(y) for y in x]) for x in res)
        self.result = f"{stab} {len(res)}\n{ops}"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask479BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
