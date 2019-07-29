class CodeforcesTask980ASolution:
    def __init__(self):
        self.result = ''
        self.necklace = ''

    def read_input(self):
        self.necklace = input()

    def process_task(self):
        try:
            if not self.necklace.count("-") % self.necklace.count("o"):
                self.result = "YES"
            else:
                self.result = "NO"
        except ZeroDivisionError:
            self.result = "YES"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask980ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
