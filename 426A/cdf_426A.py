class CodeforcesTask426ASolution:
    def __init__(self):
        self.result = ''
        self.n_s = []
        self.mugs = []

    def read_input(self):
        self.n_s = [int(x) for x in input().split(" ")]
        self.mugs = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.mugs.sort()
        self.result = "YES" if sum(self.mugs[:-1]) <= self.n_s[1] else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask426ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
