def beau(k):
    return (2 ** k - 1) * (2 ** (k - 1))


class CodeforcesTask893BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        k = 1
        mx = 1
        while beau(k) <= self.n:
            if not self.n % beau(k):
                mx = beau(k)
            k += 1
        self.result = str(int(mx))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask893BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
