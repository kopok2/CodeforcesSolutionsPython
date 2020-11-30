from operator import itemgetter


class CodeforcesTask960BSolution:
    def __init__(self):
        self.result = ''
        self.n_k_k = 0
        self.A = 0
        self.B = 0

    def read_input(self):
        self.n_k_k = [int(x) for x in input().split(" ")]
        self.A = [int(x) for x in input().split(" ")]
        self.B = [int(x) for x in input().split(" ")]

    def process_task(self):
        c = [abs(self.A[x] - self.B[x]) for x in range(self.n_k_k[0])]
        x = self.n_k_k[1] + self.n_k_k[2]
        c.sort(reverse=True)
        while x:
            if c[0] > 0:
                c[0] -= 1
            else:
                c[0] += 1
            c.sort(reverse=True)
            x -= 1
        self.result = str(sum([x ** 2 for x in c]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask960BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
