import math


def factor(n):
    for x in range(2, int(math.sqrt(n)) + 1):
        if not n % x:
            return x


class CodeforcesTask797ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        factors = []
        x = self.n_k[0]
        f = 1
        while True:
            f = factor(x)
            if not f:
                break
            else:
                factors.append(f)
                x //= f
                if len(factors) == self.n_k[1] - 1:
                    factors.append(x)
                    break
        if f:
            self.result = " ".join([str(x) for x in factors])
        else:
            if self.n_k[1] == 1 and self.n_k[0] > 1:
                self.result = str(self.n_k[0])
            else:
                self.result = "-1"


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask797ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
