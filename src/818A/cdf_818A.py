class CodeforcesTask818ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        r = self.n_k[1] + 1
        x = self.n_k[0] // 2 // r
        self.result = "{1} {2} {0}".format(self.n_k[0] -  r * x, x, x * self.n_k[1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask818ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
