class CodeforcesTask439BSolution:
    def __init__(self):
        self.result = ''
        self.n_x = []
        self.chapters = []

    def read_input(self):
        self.n_x = [int(x) for x in input().split(" ")]
        self.chapters = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.chapters.sort()
        lp = self.n_x[1]
        tot_time = 0
        for topic in self.chapters:
            tot_time += lp * topic
            lp = max(1, lp - 1)
        self.result = str(tot_time)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask439BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
