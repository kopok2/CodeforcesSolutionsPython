import math


class CodeforcesTask139BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.walls = []
        self.m = 0
        self.papers = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.walls.append([int(y) for y in input().split(" ")])
        self.m = int(input())
        for x in range(self.m):
            self.papers.append([int(y) for y in input().split(" ")])

    def process_task(self):
        tot_cost = 0
        mx = 500 ** 4 + 1
        for wall in self.walls:
            mn = mx
            cov = wall[0] * 2 + wall[1] * 2
            for paper in self.papers:
                paper_cov = paper[1] * (paper[0] // wall[2])
                if paper_cov:
                    cost = math.ceil(cov / paper_cov) * paper[2]
                    mn = min(mn, cost)
            tot_cost += mn
        self.result = str(tot_cost)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask139BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
