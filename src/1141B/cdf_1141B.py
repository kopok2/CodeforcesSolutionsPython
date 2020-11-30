class CodeforcesTask1141BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.schedule = []

    def read_input(self):
        self.n = int(input())
        self.schedule = input()

    def process_task(self):
        td = (self.schedule * 2).replace(" ", "")
        c = 0
        sc = [len(x) for x in td.split("0") if len(x)]
        if sc:
            c = max(sc)
        self.result = str(c)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1141BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
