class CodeforcesTask719BSolution:
    def __init__(self):
        self.result = ''
        self.order = ''

    def read_input(self):
        input()
        self.order = input()

    def process_task(self):
        # rbrb...
        x = 0
        y = 0
        for i, a in enumerate(self.order):
            if i % 2 and a != 'b':
                x += 1
            elif not i % 2 and a != 'r':
                y += 1
        ans1 = max(x, y)

        # brbr...
        x = 0
        y = 0
        for i, a in enumerate(self.order):
            if i % 2 and a != 'r':
                x += 1
            elif not i % 2 and a != 'b':
                y += 1
        ans2 = max(x, y)
        self.result = str(min(ans1, ans2))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask719BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
