class CodeforcesTask681BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        if self.n < 1234:
            self.result = "NO"
        else:
            is_ = False
            for a in range(1000):
                for b in range(1000):
                    if (self.n - (a * 1234567 + b * 123456)) % 1234 == 0 and (self.n - (a * 1234567 + b * 123456)) >= 0:
                        is_ = True
                        break
                if is_:
                    break
            self.result = "YES" if is_ else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask681BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
