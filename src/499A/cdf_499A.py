class CodeforcesTask499ASolution:
    def __init__(self):
        self.result = ''
        self.n_x = []
        self.best_moments = []

    def read_input(self):
        self.n_x = [int(x) for x in input().split(" ")]
        for x in range(self.n_x[0]):
            self.best_moments.append([int(j) for j in input().split(" ")])

    def process_task(self):
        watch_time = 0
        watch_time += (self.best_moments[0][0] - 1) % self.n_x[1]
        for moment in self.best_moments:
            watch_time += moment[1] - moment[0] + 1
        for x in range(len(self.best_moments) - 1):
            watch_time += (self.best_moments[x + 1][0] - 1 - self.best_moments[x][1]) % self.n_x[1]
        self.result = str(watch_time)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask499ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
