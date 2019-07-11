class CodeforcesTask935ASolution:
    def __init__(self):
        self.result = ''
        self.employees = 0

    def read_input(self):
        self.employees = int(input())

    def process_task(self):
        ways = 0
        for x in range(1, self.employees // 2 + 1):
            if not (self.employees - x) % x:
                ways += 1
        self.result = str(ways)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask935ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
