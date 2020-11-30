class CodeforcesTask1131BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.scores = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.scores.append([int(y) for y in input().split(" ")])

    def process_task(self):
        draws = 0
        laststart = -1
        laststop = -1
        self.scores = [[0, 0]] + self.scores
        for x in range(self.n):
            start_intersect = max(self.scores[x][0], self.scores[x][1])
            stop_intersect = min(self.scores[x + 1][0], self.scores[x + 1][1])
            inter_draws = max(0, stop_intersect - start_intersect + 1)
            if laststop == start_intersect:
                inter_draws -= 1
            if laststart == start_intersect:
                inter_draws = stop_intersect - laststop

            #print(start_intersect, stop_intersect, inter_draws, draws)
            if (laststart, laststop) != (start_intersect, stop_intersect):
                draws += inter_draws

            laststart, laststop = start_intersect, stop_intersect
        self.result = str(draws)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1131BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
