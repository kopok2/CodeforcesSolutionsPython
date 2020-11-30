class CodeforcesTask670ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        r = self.n % 7
        off = (self.n // 7) * 2
        d = 0
        if r == 6:
            d = 1
        self.result = "{0} {1}".format(off + d, off + min(2, r))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask670ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
