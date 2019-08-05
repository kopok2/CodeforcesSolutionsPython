import math


def get_tshirts(S):
    winners = []
    i = (S // 50) % 475
    for x in range(25):
        i = (i * 96 + 42) % 475
        winners.append(26 + i)
    return winners


class CodeforcesTask807BSolution:
    def __init__(self):
        self.result = ''
        self.p_x_y = []

    def read_input(self):
        self.p_x_y = [int(x) for x in input().split(" ")]

    def process_task(self):
        hacks = 0.0
        if self.p_x_y[1] < self.p_x_y[2]:
            hacks += (self.p_x_y[2] - self.p_x_y[1]) // 100 + math.ceil((self.p_x_y[2] - self.p_x_y[1]) % 100 / 100)
            self.p_x_y[1] += ((self.p_x_y[2] - self.p_x_y[1]) // 100) * 100 + \
                             math.ceil((self.p_x_y[2] - self.p_x_y[1]) % 100 / 100) * 100
        started = self.p_x_y[1]
        if self.p_x_y[1] > self.p_x_y[2]:
            self.p_x_y[1] = self.p_x_y[1] - ((self.p_x_y[1] - self.p_x_y[2]) // 50) * 50
        while self.p_x_y[0] not in get_tshirts(self.p_x_y[1]):
            if self.p_x_y[1] >= started:
                hacks += 0.5
            self.p_x_y[1] += 50
        hacks += 0.5
        self.result = str(int((hacks * 2) // 2))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask807BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
