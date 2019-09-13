class CodeforcesTask842ASolution:
    def __init__(self):
        self.result = ''
        self.l_r_x_y_k = []

    def read_input(self):
        self.l_r_x_y_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        can = False
        for b in range(self.l_r_x_y_k[2], self.l_r_x_y_k[3] + 1):
            a = self.l_r_x_y_k[-1] * b
            if self.l_r_x_y_k[0] <= a <= self.l_r_x_y_k[1]:
                can = True
                break
        self.result = "YES" if can else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask842ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
