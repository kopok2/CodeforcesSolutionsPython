class CodeforcesTask1154ASolution:
    def __init__(self):
        self.result = ''
        self.s_s_s_ss = []

    def read_input(self):
        self.s_s_s_ss = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.s_s_s_ss.sort()
        c = self.s_s_s_ss[3] - self.s_s_s_ss[0]
        b = self.s_s_s_ss[3] - self.s_s_s_ss[1]
        a = self.s_s_s_ss[3] - self.s_s_s_ss[2]
        self.result = "{0} {1} {2}".format(a, b, c)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1154ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
