class CodeforcesTask525BSolution:
    def __init__(self):
        self.result = ''
        self.string = ''
        self.m = 0
        self.a = []

    def read_input(self):
        self.string = input()
        self.m = int(input())
        self.a = [int(x) for x in input().split(" ")]

    def process_task(self):
        ns = list(self.string)
        n = len(ns)
        reve = [False] * (n // 2 + n % 2)
        for m in range(self.m):
            reve[self.a[m] - 1] = not reve[self.a[m] - 1]
        to_reve = [False] * (n // 2 + n % 2)
        doing = False
        for x in range(n // 2 + n % 2):
            if doing:
                if not reve[x]:
                    to_reve[x] = True
                else:
                    doing = False
            else:
                if reve[x]:
                    doing = True
                    to_reve[x] = True
        for x in range(n // 2 + n % 2):
            if to_reve[x]:
                ns[x], ns[n - x - 1] = ns[n - x - 1], ns[x]
        self.result = ''.join(ns)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask525BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
