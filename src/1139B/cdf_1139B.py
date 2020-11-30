class CodeforcesTask1139BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.a = []

    def read_input(self):
        self.n = int(input())
        self.a = [int(x) for x in input().split(" ")]

    def process_task(self):
        p = 0
        mx = 10 ** 10
        for a in self.a[::-1]:
            if a < mx:
                mx = a
                p += a
            else:
                mx = max(0, mx - 1)
                p += mx
        self.result = str(p)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1139BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
