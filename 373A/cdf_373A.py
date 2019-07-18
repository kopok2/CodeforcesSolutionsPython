class CodeforcesTask373ASolution:
    def __init__(self):
        self.result = ''
        self.k = 0
        self.panels = ''

    def read_input(self):
        self.k = int(input())
        for x in range(4):
            self.panels += input()

    def process_task(self):
        times = [str(x) for x in range(1, 10)]
        can = True
        for time in times:
            if self.panels.count(time) > self.k * 2:
                can = False
                break
        if can:
            self.result = "YES"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask373ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
