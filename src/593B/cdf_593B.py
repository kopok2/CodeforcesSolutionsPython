from operator import itemgetter


class CodeforcesTask593BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.x1_x2 = []
        self.lines = []

    def read_input(self):
        self.n = int(input())
        self.x1_x2 = [int(x) for x in input().split(" ")]
        for x in range(self.n):
            self.lines.append([int(x) for x in input().split(" ")])

    def process_task(self):
        x1 = self.x1_x2[0] + 0.00000001
        x2 = self.x1_x2[1] - 0.00000001
        left = [(self.lines[x][0] * x1 + self.lines[x][1], x) for x in range(self.n)]
        right = [(self.lines[x][0] * x2 + self.lines[x][1], x) for x in range(self.n)]
        left.sort(key=itemgetter(0, 1))
        right.sort(key=itemgetter(0, 1))
        lorder = [x[1] for x in left]
        rorder = [x[1] for x in right]
        if lorder == rorder:
            self.result = "NO"
        else:
            self.result = "YES"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask593BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
