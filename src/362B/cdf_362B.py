class CodeforcesTask362BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.dirty = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        if self.n_m[1]:
            self.dirty = [int(x) for x in input().split(" ")]

    def process_task(self):
        dirty = {}
        for d in self.dirty:
            dirty[d] = True
        can_ = True
        for d in self.dirty:
            if d - 1 in dirty and d + 1 in dirty:
                can_ = False
                break
        if 1 in dirty or self.n_m[0] in dirty:
            can_ = False
        self.result = "YES" if can_ else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask362BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
