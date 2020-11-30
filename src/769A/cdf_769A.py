class CodeforcesTask769ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.years = []

    def read_input(self):
        self.n = int(input())
        self.years = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.years.sort()
        self.result = str(self.years[self.n // 2])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask769ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
