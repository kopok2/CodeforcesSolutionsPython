from fractions import gcd
from functools import reduce


def list_gcd(l):
    x = reduce(gcd, l)
    return x


def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    result = [x for x in range(2, n) if prime[x - 1]]
    return result


class CodeforcesTask1034ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.integers = []

    def read_input(self):
        self.n = int(input())
        self.integers = [int(x) for x in input().split(" ")]

    def process_task(self):
        base = list_gcd(self.integers)
        remains = [x // base for x in self.integers]
        if sum(remains) == self.n:
            self.result = "-1"
        else:
            remains.sort(reverse=True)
            if 1 in remains:
                remaining = remains[:remains.index(1)]
            else:
                remaining = remains
            ps = sieve(max(remaining))
            max_divi = 1
            for p in ps:
                divu = [1 if not x % p else 0 for x in remaining]
                max_divi = max(max_divi, sum(divu))
            self.result = str(self.n - max_divi)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1034ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
