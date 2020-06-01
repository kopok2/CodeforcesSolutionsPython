class CodeforcesTask1131ASolution:
    def __init__(self):
        self.result = ''
        self.w_h_w_h = []

    def read_input(self):
        self.w_h_w_h = [int(x) for x in input().split(" ")]

    def process_task(self):
        w = max(self.w_h_w_h[0], self.w_h_w_h[2])
        h = self.w_h_w_h[1] + self.w_h_w_h[3]
        res = w * 2 + h * 2 + 4
        self.result = str(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1131ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
