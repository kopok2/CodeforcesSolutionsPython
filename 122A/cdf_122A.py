class CodeforcesTask122ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        res = False
        for i in range(1, self.n + 1):
            is_lucky = True
            for c in str(i):
                if c not in "74":
                    is_lucky = False
                    break
            if is_lucky:
                if not self.n % i:
                    res = True
                    break
        self.result = "YES" if res else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask122ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
