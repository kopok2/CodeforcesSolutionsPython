class CodeforcesTask875ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        sols = []
        for x in range(100):
            res = self.n - x
            if res > 0:
                well = res + sum([int(j) for j in str(res)])
                if well == self.n:
                    sols.append(res)
        sols.sort()
        self.result = "{0}\n{1}".format(len(sols), "\n".join([str(x) for x in sols]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask875ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
