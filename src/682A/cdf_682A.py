class CodeforcesTask682ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]

    def process_task(self):
        pairs = 0
        sm = min(*self.n_m)
        bg = max(*self.n_m)
        for x in range((bg // 5) * 2 + 1):
            x += 1
            a = x * 5 - 1
            if a < 0:
                a = 0
            if a > bg:
                a = bg + sm - a
            if a < 0:
                a = 0
            # print(x, a, sm)
            pairs += min(a, sm)

        self.result = str(pairs)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask682ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
