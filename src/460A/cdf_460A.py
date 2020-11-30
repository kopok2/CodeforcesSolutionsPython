class CodeforcesTask460ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]

    def process_task(self):
        days = 0
        s = self.n_m[0]
        ts = self.n_m[1]
        while s:
            s -= 1
            days += 1
            ts -= 1
            if not ts:
                s += 1
                ts = self.n_m[1]
        self.result = str(days)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask460ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
