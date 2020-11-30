class CodeforcesTask766ASolution:
    def __init__(self):
        self.result = ''
        self.a = ''
        self.b = ''

    def read_input(self):
        self.a = input()
        self.b = input()

    def process_task(self):
        if self.a == self.b:
            self.result = "-1"
        else:
            self.result = str(max(len(self.a), len(self.b)))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask766ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
