class CodeforcesTask479ASolution:
    def __init__(self):
        self.result = ''
        self.a = 0
        self.b = 0
        self.c = 0

    def read_input(self):
        self.a = int(input())
        self.b = int(input())
        self.c = int(input())

    def process_task(self):
        self.result = str(max(self.a * self.b + self.c, self.a * (self.b + self.c),
                              self.a + self.b * self.c, (self.a + self.b) * self.c,
                              self.a + self.b + self.c, self.a * self.b * self.c))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask479ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
