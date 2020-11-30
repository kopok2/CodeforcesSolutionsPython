class CodeforcesTask404BSolution:
    def __init__(self):
        self.result = ''
        self.a_d = []
        self.n = 0

    def read_input(self):
        self.a_d = [float(x) for x in input().split(" ")]
        self.n = int(input())

    def process_task(self):
        for x in range(1, self.n + 1):
            lpos = x * self.a_d[1] % (4 * self.a_d[0])
            pos = [0, 0]
            if lpos <= self.a_d[0]:
                pos[0] = lpos
            elif lpos <= self.a_d[0] * 2:
                pos[0] = self.a_d[0]
                pos[1] = lpos - self.a_d[0]
            elif lpos <= self.a_d[0] * 3:
                pos[0] = self.a_d[0] - (lpos - self.a_d[0] * 2)
                pos[1] = self.a_d[0]
            else:
                pos[1] = self.a_d[0] - (lpos - self.a_d[0] * 3)
            print("{0} {1}".format(*pos))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask404BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
