from collections import deque
import random


class CodeforcesTask566BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.rules = []

    def read_input(self):
        self.n = int(input())
        self.rules = [[int(x) for x in input().split(" ")] + [y + 1] for y in range(self.n * 4)]

    def process_task(self):

        loads = [4] * self.n
        random.shuffle(self.rules)
        to_use = deque(self.rules)
        order = []
        res = True
        ba = 0
        while to_use and res:
            moving = to_use.popleft()
            loads[moving[0] - 1] -= 1
            if loads[moving[1] - 1] < 9 and loads[moving[2] - 1] < 9 + (-1 if moving[2] == moving[1] else 0):
                ba = 0
                loads[moving[1] - 1] += 1
                loads[moving[2] - 1] += 1
                order.append(moving[3])
            else:
                ba += 1
                loads[moving[0] - 1] += 1
                to_use.append(moving)
            if ba > self.n * 12:
                res = False
        self.result = "NO" if not res else f"YES\n{' '.join([str(x) for x in order])}"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask566BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
