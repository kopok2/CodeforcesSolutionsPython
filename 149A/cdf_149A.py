class CodeforcesTask149ASolution:
    def __init__(self):
        self.result = ''
        self.k = 0
        self.months = []

    def read_input(self):
        self.k = int(input())
        self.months = [int(x) for x in input().split(" ")]

    def process_task(self):
        result = 0
        self.months.sort(reverse=True)
        while self.k > 0 and self.months:
            self.k -= self.months.pop(0)
            result += 1
        if self.k > 0:
            result = -1
        self.result = str(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask149ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
