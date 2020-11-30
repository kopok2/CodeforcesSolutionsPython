class CodeforcesTask1028BSolution:
    def __init__(self):
        self.result = ''

    def read_input(self):
        pass

    def process_task(self):
        self.result = "{0}\n{1}".format("9" * 200 + "0" * 199 + "1", "9" * 200)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1028BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
