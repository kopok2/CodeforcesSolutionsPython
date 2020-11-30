class CodeforcesTask166ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.scores = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        for x in range(self.n_k[0]):
            self.scores.append([int(y) for y in input().split(" ")])

    def process_task(self):
        self.scores = [[100 - x[0], x[1]] for x in self.scores]
        self.scores.sort()
        place = 1
        cnt = 1
        xd = {1: 1}
        self.scores[0].append(1)
        for x in range(1, self.n_k[0]):
            if self.scores[x][0] > self.scores[x - 1][0]:
                place += 1
                cnt = 1
            elif self.scores[x][1] > self.scores[x - 1][1]:
                place += 1
                cnt = 1
            else:
                place += 1
                cnt += 1
            self.scores[x].append(place)
            xd[place] = cnt
            for x in range(cnt):
                if place - x in xd:
                    xd[place - x] = cnt
        self.result = str(xd[self.n_k[1]])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask166ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
