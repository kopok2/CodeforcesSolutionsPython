class CodeforcesTask550ASolution:
    def __init__(self):
        self.result = ''
        self.string = ""

    def read_input(self):
        self.string = input()

    def process_task(self):
        if "AB" in self.string and "BA" in self.string:
            if "BA" in self.string.replace("AB", "__", 1):
                self.result = "YES"
            else:
                if "AB" in self.string.replace("BA", "__", 1):
                    self.result = "YES"
                else:
                    self.result = "NO"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask550ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
