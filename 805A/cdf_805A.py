class CodeforcesTask805ASolution:
    def __init__(self):
        self.result = ''
        self.l_r = []

    def read_input(self):
        self.l_r = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.l_r[1] > self.l_r[0]:
            self.result = "2"
        else:
            self.result = str(self.l_r[0])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask805ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
