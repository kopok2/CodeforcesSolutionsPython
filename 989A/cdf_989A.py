class CodeforcesTask989ASolution:
    def __init__(self):
        self.result = ''
        self.landscape = ''

    def read_input(self):
        self.landscape = input()

    def process_task(self):
        if "ABC" in self.landscape:
            self.result = "Yes"
        elif "ACB" in self.landscape:
            self.result = "Yes"
        elif "BAC" in self.landscape:
            self.result = "Yes"
        elif "BCA" in self.landscape:
            self.result = "Yes"
        elif "CAB" in self.landscape:
            self.result = "Yes"
        elif "CBA" in self.landscape:
            self.result = "Yes"
        else:
            self.result = "No"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask989ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
