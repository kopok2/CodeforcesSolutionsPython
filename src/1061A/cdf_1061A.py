class CodeforcesTask1061ASolution:
    def __init__(self):
        self.result = ''
        self.n_s = []

    def read_input(self):
        self.n_s = [int(x) for x in input().split(" ")]

    def process_task(self):
        r = 0
        while self.n_s[1] > self.n_s[0]:
            r += 1
            self.n_s[1] -= self.n_s[0]
        r += 1
        self.result = str(r)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1061ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
