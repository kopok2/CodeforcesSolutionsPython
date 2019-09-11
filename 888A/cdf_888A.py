class CodeforcesTask888ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.array = []

    def read_input(self):
        self.n = int(input())
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        extremas_cnt = 0
        for x in range(1, self.n - 1):
            if self.array[x - 1] > self.array[x] < self.array[x + 1]:
                extremas_cnt += 1
            elif self.array[x - 1] < self.array[x] > self.array[x + 1]:
                extremas_cnt += 1
        self.result = str(extremas_cnt)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask888ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
