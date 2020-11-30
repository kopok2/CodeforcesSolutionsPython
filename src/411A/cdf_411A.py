class CodeforcesTask411ASolution:
    def __init__(self):
        self.result = ''
        self.password = ''

    def read_input(self):
        self.password = input()

    def process_task(self):
        correct = True
        if len(self.password) < 5:
            correct = False
        else:
            cond1_met = False
            cond2_met = False
            cond3_met = False
            for c in "abcdefghijklmnoprstuvwxyz":
                if c in self.password:
                    cond1_met = True
                    break
            for c in "abcdefghijklmnoprstuvwxyz".upper():
                if c in self.password:
                    cond2_met = True
                    break
            for c in "123456790":
                if c in self.password:
                    cond3_met = True
                    break
            correct = cond1_met and cond2_met and cond3_met
        if correct:
            self.result = "Correct"
        else:
            self.result = "Too weak"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask411ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
