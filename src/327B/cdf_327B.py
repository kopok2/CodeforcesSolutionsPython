def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    result = []
    for p in range(2, n):
        if prime[p]:
            result.append(p)
    return result


class CodeforcesTask327BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        print(" ".join([str(x) for x in SieveOfEratosthenes(1500000)][:self.n]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask327BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
