from collections import deque


class CodeforcesTask799BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.prices = []
        self.front_colors = []
        self.back_colors = []
        self.m = 0
        self.customers = []

    def read_input(self):
        self.n = int(input())
        self.prices = [int(x) for x in input().split(" ")]
        self.front_colors = [int(x) for x in input().split(" ")]
        self.back_colors = [int(x) for x in input().split(" ")]
        self.m = int(input())
        self.customers = [int(x) for x in input().split(" ")]

    def process_task(self):
        shop = [[[] for _ in range(3)] for __ in range(3)]
        for t in range(self.n):
            shop[self.front_colors[t] - 1][self.back_colors[t] - 1].append(self.prices[t])
        for x in range(3):
            for y in range(3):
                shop[x][y].sort()
                shop[x][y] = deque(shop[x][y])
        res = []
        for customer in self.customers:
            mn_p = 10**10
            selected = None
            for back in range(3):
                if shop[customer - 1][back]:
                    if shop[customer - 1][back][0] < mn_p:
                        selected = (customer - 1, back)
                        mn_p = shop[customer - 1][back][0]
            for front in range(3):
                if shop[front][customer - 1]:
                    if shop[front][customer - 1][0] < mn_p:
                        selected = (front, customer - 1)
                        mn_p = shop[front][customer - 1][0]
            if selected:
                res.append(shop[selected[0]][selected[1]].popleft())
            else:
                res.append(-1)
        self.result = " ".join([str(x) for x in res])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask799BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
