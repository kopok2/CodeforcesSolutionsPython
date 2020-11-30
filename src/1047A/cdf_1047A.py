class CodeforcesTask1047ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        if not self.n % 3:
            a = 1
            b = 1
            c = self.n - 2
        else:
            a = 1
            b = 2
            c = self.n - 3
        self.result = f"{a} {b} {c}"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1047ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
