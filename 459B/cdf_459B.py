class CodeforcesTask459BSolution:
    def __init__(self):
        self.result = ''
        self.n = []
        self.array = []

    def read_input(self):
        self.n = int(input())
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        mx = max(self.array)
        mn = min(self.array)
        diff = mx - mn
        mxc = self.array.count(mx)
        mnc = self.array.count(mn)
        if diff:
            self.result = "{0} {1}".format(diff, mxc * mnc)
        else:
            self.result = "0 {0}".format(mxc * (mxc - 1) // 2)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask459BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
