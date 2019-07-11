import math


class CodeforcesTask17ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        primes = []
        for x in range(2, self.n_k[0]):
            ad_x = True
            for j in range(2, int(math.sqrt(x)) + 1):
                if not x % j:
                    ad_x = False
                    break
            if ad_x:
                primes.append(x)
        ks = 0
        for x in range(len(primes) - 1):
            np = primes[x] + primes[x + 1] + 1
            if np <= self.n_k[0]:
                ad_k = True
                for j in range(2, int(math.sqrt(np)) + 1):
                    if not np % j:
                        ad_k = False
                        break
                if ad_k:
                    ks += 1
            else:
                break
        if ks >= self.n_k[1]:
            self.result = "YES"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask17ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
