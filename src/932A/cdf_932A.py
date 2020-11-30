class CodeforcesTask932ASolution:
    def __init__(self):
        self.result = ''
        self.a = ''

    def read_input(self):
        self.a = input()

    def process_task(self):
        self.result = self.a + self.a[::-1][1:]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask932ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
