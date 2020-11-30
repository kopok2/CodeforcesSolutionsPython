class CodeforcesTask624ASolution:
    def __init__(self):
        self.result = ''
        self.d_l_v_v = []

    def read_input(self):
        self.d_l_v_v = [int(x) for x in input().split(" ")]

    def process_task(self):
        time = (self.d_l_v_v[1] - self.d_l_v_v[0]) / (self.d_l_v_v[2] + self.d_l_v_v[3])
        self.result = str(time)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask624ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
