class CodeforcesTask898BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.a = 0
        self.b = 0

    def read_input(self):
        self.n = int(input())
        self.a = int(input())
        self.b = int(input())

    def process_task(self):
        self.result = "NO"
        for x in range(10000000):
            if x * self.a > self.n:
                break
            if not (self.n - self.a * x) % self.b:
                y = (self.n - self.a * x) // self.b
                self.result = "YES\n{0} {1}".format(x, y)
                break

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask898BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
