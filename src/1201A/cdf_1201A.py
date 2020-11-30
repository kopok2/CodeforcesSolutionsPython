class CodeforcesTask1201ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.answers = []
        self.points = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.answers.append(input())
        self.points = [int(x) for x in input().split(" ")]

    def process_task(self):
        points = 0
        for q in range(self.n_m[1]):
            a = [self.answers[x][q] for x in range(self.n_m[0])]
            cnts = [a.count(c) for c in list(set(a))]
            points += max(cnts) * self.points[q]
        self.result = str(points)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1201ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
