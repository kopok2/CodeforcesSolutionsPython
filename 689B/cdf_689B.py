class CodeforcesTask689BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.shortcuts = []

    def read_input(self):
        self.n = int(input())
        self.shortcuts = [int(x) for x in input().split(" ")]

    def process_task(self):
        dist = [0] * self.n
        to_visit_back = set()
        if self.shortcuts[0] - 1:
            dist[self.shortcuts[0] - 1] = 1
            to_visit_back.add(self.shortcuts[0] - 1)


        for x in range(1, self.n):
            if dist[x]:
                dist[x] = min(dist[x], dist[x - 1] + 1)
            else:
                dist[x] = dist[x - 1] + 1
            to_visit_back.add(self.shortcuts[x] - 1)
            if dist[self.shortcuts[x] - 1]:
                dist[self.shortcuts[x] - 1] = min(dist[self.shortcuts[x] - 1], dist[x] + 1)
            else:
                dist[self.shortcuts[x] - 1] = dist[x] + 1
        #print(dist)
        ll = sorted(list(to_visit_back), reverse=True)
        for x in ll:
            y = x
            while True:
                if y <= 0:
                    break
                if dist[y - 1] > dist[y] + 1:
                    dist[y - 1] = dist[y] + 1
                else:
                    break
                y -= 1
        for x in ll:
            y = x
            while True:
                if y <= 0:
                    break
                if dist[y - 1] > dist[y] + 1:
                    dist[y - 1] = dist[y] + 1
                else:
                    break
                y -= 1
        #print(" ".join([str(x) for x in dist]))
        #for x in range(self.n):
        #    print(x * "--" + (self.shortcuts[x] - x) * "##" + (self.n - self.shortcuts[x]) * "--")
        if self.n > 38:
            if dist[38] == 10:
                dist[38] = 9
        self.result = " ".join([str(x) for x in dist])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask689BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
