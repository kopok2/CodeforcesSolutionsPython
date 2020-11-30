import math


class CodeforcesTask940BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.k = 0
        self.a = 0
        self.b = 0

    def read_input(self):
        self.n = int(input())
        self.k = int(input())
        self.a = int(input())
        self.b = int(input())

    def process_task(self):
        if self.n < self.k:
            cost = (self.n - 1) * self.a
        elif self.k == 1:
            cost = (self.n - 1) * self.a
        else:
            cost = 0
            x = self.n
            while x > 1:
                if x >= self.k:
                    rest = x % self.k
                    if rest:
                        cost += rest * self.a
                        x -= rest
                    else:
                        cost += min(self.b, (x - (x // self.k)) * self.a)
                        x //= self.k
                else:
                    cost += (x - 1) * self.a
                    x = 1
        self.result = str(cost)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask940BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
