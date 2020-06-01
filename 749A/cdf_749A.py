class CodeforcesTask749ASolution:
    def __init__(self):
        self.result = ''
        self.n  = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        res = []
        if self.n % 2:
            res.append(3)
            res += [2] * ((self.n - 3) // 2)
        else:
            res += [2] * (self.n // 2)
        self.result = "{0}\n{1}".format(len(res), " ".join([str(x) for x in res]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask749ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
