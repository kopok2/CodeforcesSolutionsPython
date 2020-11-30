class CodeforcesTask803BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        to_visit = []
        dists = [self.n + 1] * self.n
        for x in range(self.n):
            if not self.sequence[x]:
                dists[x] = 0
                if 0 < x < self.n - 1:
                    if self.sequence[x - 1] or self.sequence[x + 1]:
                        to_visit.append(x)
                else:
                    to_visit.append(x)
        while to_visit:
            visiting = to_visit.pop()
            x = visiting - 1
            dist = 1
            while x >= 0:
                if dists[x] > dist:
                    dists[x] = dist
                else:
                    break
                x -= 1
                dist += 1
            x = visiting + 1
            dist = 1
            while x < self.n:
                if dists[x] > dist:
                    dists[x] = dist
                else:
                    break
                x += 1
                dist += 1
        self.result = " ".join([str(x) for x in dists])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask803BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
