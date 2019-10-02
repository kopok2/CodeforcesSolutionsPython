class CodeforcesTask490ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sk = []

    def read_input(self):
        self.n = int(input())
        self.sk = [int(x) for x in input().split(" ")]

    def process_task(self):
        ones = []
        twos = []
        threes = []
        for a in [(x + 1, self.sk[x]) for x in range(self.n)]:
            if a[1] == 1:
                ones.append(a[0])
            elif a[1] == 2:
                twos.append(a[0])
            else:
                threes.append(a[0])
        results = []
        d = min(len(ones), len(twos), len(threes))
        for x in range(d):
            results.append("{0} {1} {2}".format(ones[x], twos[x], threes[x]))
        self.result = "{0}\n{1}".format(d, "\n".join(results))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask490ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
