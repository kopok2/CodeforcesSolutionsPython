class CodeforcesTask950ASolution:
    def __init__(self):
        self.result = ''
        self.l_r_a = []

    def read_input(self):
        self.l_r_a = [int(x) for x in input().split(" ")]

    def process_task(self):
        size = min(self.l_r_a[0], self.l_r_a[1])
        rl = self.l_r_a[0] - size
        rl += self.l_r_a[1] - size
        size *= 2
        if rl:
            if self.l_r_a[2] > rl:
                size += rl * 2
                remain = self.l_r_a[2] - rl
                size += (remain // 2) * 2
            else:
                size += self.l_r_a[2] * 2
        else:
            size += (self.l_r_a[2] // 2) * 2
        self.result = str(size)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask950ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
