class CodeforcesTask262ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.nums = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.nums = [int(x) for x in input().split(" ")]

    def process_task(self):
        r = 0
        for num in self.nums:
            if str(num).count("4") + str(num).count("7") <= self.n_k[1]:
                r += 1
        self.result = str(r)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask262ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
