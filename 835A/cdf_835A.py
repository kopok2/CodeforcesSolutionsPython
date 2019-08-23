class CodeforcesTask835ASolution:
    def __init__(self):
        self.result = ''
        self.s_vv_tt = []

    def read_input(self):
        self.s_vv_tt = [int(x) for x in input().split(" ")]

    def process_task(self):
        r1 = self.s_vv_tt[0] * self.s_vv_tt[1] + 2 * self.s_vv_tt[3]
        r2 = self.s_vv_tt[0] * self.s_vv_tt[2] + 2 * self.s_vv_tt[4]
        if r1 == r2:
            self.result = "Friendship"
        elif r1 < r2:
            self.result = "First"
        else:
            self.result = "Second"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask835ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
