class CodeforcesTask327ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.a = []

    def read_input(self):
        self.n = int(input())
        self.a = [int(x) for x in input().split(" ")]

    def process_task(self):
        mx = 0
        base = sum(self.a)
        for x in range(self.n):
            for y in range(x + 1, self.n + 1):
                n = sum(self.a[x:y])
                nb = base - n + (y - x - n)
                #print(self.a[x:y], x, y, n, nb, mx)
                mx = max(mx, nb)
        self.result = str(mx)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask327ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
