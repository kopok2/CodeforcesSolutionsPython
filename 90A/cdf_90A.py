class CodeforcesTask90ASolution:
    def __init__(self):
        self.result = ''
        self.r_g_b = []

    def read_input(self):
        self.r_g_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        time = -1
        cable = 0
        while sum(self.r_g_b):
            self.r_g_b[cable] = max(0, self.r_g_b[cable] - 2)
            time += 1
            cable += 1
            if cable > 2:
                cable = 0
        time += 30
        self.result = str(time)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask90ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
