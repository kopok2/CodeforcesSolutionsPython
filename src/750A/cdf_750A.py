class CodeforcesTask750ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        time = 240 - self.n_k[1]
        i = 1
        solved = 0
        while time - i * 5 >= 0 and i <= self.n_k[0]:
            solved += 1
            time -= i * 5
            i += 1
        self.result = str(solved)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask750ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
