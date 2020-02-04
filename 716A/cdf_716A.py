class CodeforcesTask716ASolution:
    def __init__(self):
        self.result = ''
        self.n_c = []
        self.times = []

    def read_input(self):
        self.n_c = [int(x) for x in input().split(" ")]
        self.times = [int(x) for x in input().split(" ")]

    def process_task(self):
        words = 0
        last = -self.n_c[1]
        for word in self.times:
            if word - last > self.n_c[1]:
                words = 1
            else:
                words += 1
            last = word
        self.result = str(words)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask716ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
