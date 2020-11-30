class CodeforcesTask604ASolution:
    def __init__(self):
        self.result = ''
        self.times = []
        self.subs = []
        self.hacks = []

    def read_input(self):
        self.times = [int(x) for x in input().split(" ")]
        self.subs = [int(x) for x in input().split(" ")]
        self.hacks = [int(x) for x in input().split(" ")]

    def process_task(self):
        scores = [max(0.3 * (x + 1) * 500, (1 - self.times[x]/250) * ((x + 1) * 500) - 50 * self.subs[x]) for x in range(len(self.subs))]
        self.result = str(int(sum(scores) - self.hacks[1] * 50 + self.hacks[0] * 100))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask604ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
