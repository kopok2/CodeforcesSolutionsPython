import math


def get_primes(r):
    result = []
    for x in range(2, r):
        isp = True
        for y in range(2, int(math.sqrt(x)) + 1):
            if not x % y:
                isp = False
                break
        if isp:
            result.append(x)
    return result


class CodeforcesTask947ASolution:
    def __init__(self):
        self.result = ''
        self.x2 = 0

    def read_input(self):
        self.x2 = int(input())

    def process_task(self):
        primes = get_primes(self.x2)
        print(primes)
        input()
        factors2 = [x for x in primes if not self.x2 % x]
        print(factors2)
        ones = []
        for f2 in factors2:
            for x in range((self.x2 // f2 - 1) * f2 + 1, self.x2 + 1):
                ones.append(x)
        ones = list(set(ones))
        print(ones)
        zeros = []
        for one in ones:
            factors1 = [x for x in primes if not one % x]
            print(factors1, one)
            for f1 in factors1:
                zeros.append(one - f1 + 1)
        zeros = [x for x in zeros if x >= 3]
        self.result = str(min(zeros))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask947ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
