import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if not x % i:
            return False
    return True


def factorize(n):
    if n == 1:
        return 1
    else:
        factors = 1
        s = math.sqrt(n) + 1
        x = 2
        start = n
        while x <= s:
            if is_prime(x):
                result = 1
                #n = start
                while not n % x:
                    #if n // x != 1:
                    result += 1
                    n //= x
                #if n != 1 and result > 1:
                #    factors *= 2
                if result >= 2:
                    factors *= result
            x += 1
        if is_prime(n) and n > 1:
            factors *= 2

        if factors == 1:
            factors = 2
        return factors


class CodeforcesTask1068BSolution:
    def __init__(self):
        self.result = ''
        self.b = 0

    def read_input(self):
        self.b = int(input())

    def process_task(self):
        self.result = str(factorize(self.b))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1068BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
