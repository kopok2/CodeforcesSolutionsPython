class CodeforcesTask731BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.days = []

    def read_input(self):
        self.n = int(input())
        self.days = [int(x) for x in input().split(" ")]

    def process_task(self):
        can_ = True
        for x in range(self.n):
            if self.days[x] % 2:
                if x < self.n - 1:
                    if self.days[x + 1] > 0:
                        self.days[x + 1] -= 1
                    else:
                        can_ = False
                        break
                else:
                    can_ = False
                    break
        self.result = "YES" if can_ else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask731BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
