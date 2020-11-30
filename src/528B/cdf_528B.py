from operator import itemgetter


class CodeforcesTask528BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.points = []

    def read_input(self):
        self.n = int(input())
        for _ in range(self.n):
            self.points.append([int(x) for x in input().split(" ")])
            self.points[-1].append(sum(self.points[-1]))

    def process_task(self):
        self.points.sort(key=itemgetter(2))
        last = 0
        ans = 1
        for i in range(1, self.n):
            if self.points[i][0] - self.points[i][1] >= self.points[last][0] + self.points[last][1]:
                last = i
                ans += 1
        self.result = str(ans)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask528BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
