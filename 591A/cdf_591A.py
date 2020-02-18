class CodeforcesTask591ASolution:
    def __init__(self):
        self.result = ''
        self.l = 0
        self.p = 0
        self.q = 0

    def read_input(self):
        self.l = int(input())
        self.p = int(input())
        self.q = int(input())

    def process_task(self):
        step = 10 ** (-6)
        a = (self.p * self.l) / (self.p + self.q)
        v1 = -self.p
        v2 = self.q
        p1 = a
        p2 = a
        while abs(p1 - p2) > 0.00001:
            p1 += step * v1
            p2 += step * v2
            if p1 < 0:
                v1 = -v1
            if p2 > self.l:
                v2 = -v2
        self.result = str(p1)



    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask591ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
