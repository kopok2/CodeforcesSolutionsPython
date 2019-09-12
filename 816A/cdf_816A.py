class CodeforcesTask816ASolution:
    def __init__(self):
        self.result = ''
        self.hour = []

    def read_input(self):
        self.hour = [int(x) for x in input().split(":")]

    def process_task(self):
        m = 0
        while not "{0:02d}{1:02d}".format(self.hour[0], self.hour[1]) == "{0:02d}{1:02d}".format(self.hour[0], self.hour[1])[::-1]:
            self.hour[1] += 1
            if self.hour[1] >= 60:
                self.hour[1] = 0
                self.hour[0] += 1
                if self.hour[0] >= 24:
                    self.hour[0] = 0
            m += 1
        self.result = str(m)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask816ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
