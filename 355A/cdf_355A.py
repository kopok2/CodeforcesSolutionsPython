class CodeforcesTask355ASolution:
    def __init__(self):
        self.result = ''
        self.k_d = []

    def read_input(self):
        self.k_d = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.k_d[0] != 1 and self.k_d[1] == 0:
            self.result = "No solution"
        else:
            self.result = str(self.k_d[1]) + "0" * (self.k_d[0] - 1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask355ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
