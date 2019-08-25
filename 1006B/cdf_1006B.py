class CodeforcesTask1006BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.problems = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.problems = [int(x) for x in input().split(" ")]

    def process_task(self):
        to_solve = self.problems[::]
        to_solve.sort(reverse=True)
        to_solve = to_solve[:self.n_k[1]]
        max_points = sum(to_solve)
        days = []
        day = 0
        for x in range(self.n_k[0]):
            day += 1
            if self.problems[x] in to_solve:
                to_solve.remove(self.problems[x])
                days.append(day)
                day = 0
        days[-1] += day
        self.result = "{0}\n{1}".format(max_points, " ".join([str(x) for x in days]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1006BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
