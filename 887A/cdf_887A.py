class CodeforcesTask887ASolution:
    def __init__(self):
        self.result = ''
        self.number = ''

    def read_input(self):
        self.number = input()

    def process_task(self):

        if "1" in self.number:
            if self.number.split("1", 1)[1].count("0") >= 6:
                self.result = "yes"
            else:
                self.result = "no"
        else:
            self.result = "no"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask887ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
