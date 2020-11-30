class CodeforcesTask739ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.ms = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.ms.append([int(x) for x in input().split(" ")])

    def process_task(self):
        lens = [x[1] - x[0] + 1 for x in self.ms]
        target = min(lens)
        result = []
        current = 0
        for x in range(self.n_m[0]):
            result.append(current)
            current += 1
            if current == target:
                current = 0
        self.result = "{0}\n{1}".format(target, " ".join([str(x) for x in result]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask739ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
