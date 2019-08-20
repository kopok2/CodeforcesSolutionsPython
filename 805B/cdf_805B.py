class CodeforcesTask805BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        self.result = (self.n // 4) * "aabb"
        if self.n % 4:
            if self.n % 4 == 3:
                self.result += "aab"
            elif self.n % 4 == 2:
                self.result += "aa"
            else:
                self.result += "a"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask805BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
