def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


class CodeforcesTask150ASolution:
    def __init__(self):
        self.result = ''
        self.q = 0

    def read_input(self):
        self.q = int(input())

    def process_task(self):
        factors = prime_factors(self.q)
        if len(factors) == 1 or not factors:
            winner = 1
            move = 0
        elif len(factors) == 2:
            winner = 2
        else:
            winner = 1
            move = factors[0] * factors[1]
        if winner == 1:
            self.result = "{0}\n{1}".format(winner, move)
        else:
            self.result = "2"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask150ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
