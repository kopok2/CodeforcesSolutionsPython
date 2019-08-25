class CodeforcesTask509ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        pre_row = [1] * self.n
        for x in range(self.n - 1):
            row = [1] * self.n
            for y in range(self.n - 1):
                row[y + 1] = pre_row[y + 1] + row[y]
            pre_row = row
        self.result = str(pre_row[-1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask509ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
