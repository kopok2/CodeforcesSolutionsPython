class CodeforcesTask702ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.array = []

    def read_input(self):
        self.n = int(input())
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        mx = 1
        cr = 1
        for x in range(1, self.n):
            if self.array[x] > self.array[x - 1]:
                cr += 1
            else:
                cr = 1
            mx = max(cr, mx)
        self.result = str(mx)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask702ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
