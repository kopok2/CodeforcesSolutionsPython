class CodeforcesTask955BSolution:
    def __init__(self):
        self.result = ''
        self.s = ''

    def read_input(self):
        self.s = input()

    def process_task(self):
        chars = set([ord(c) for c in self.s])
        if len(chars) > 4:
            self.result = "No"
        elif len(chars) == 1:
            self.result = "No"
        else:
            if len(chars) == 4:
                self.result = "Yes"
            elif len(chars) == 3:
                if len(self.s) < 4:
                    self.result = "No"
                else:
                    self.result = "Yes"
            else:
                cnts = self.s.count(self.s[0])
                if len(self.s) - cnts == 1 or cnts == 1:
                    self.result = "No"
                else:
                    self.result = "Yes"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask955BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
