class CodeforcesTask982ASolution:
    def __init__(self):
        self.result = ''
        self.seating = ''

    def read_input(self):
        input()
        self.seating = input()

    def process_task(self):
        if "11" in self.seating:
            self.result = "No"
        else:
            if "000" in self.seating:
                self.result = "No"
            elif len(self.seating) > 1:
                if "00" in self.seating[:2]:
                    self.result = "No"
                elif "00" in self.seating[-2:]:
                    self.result = "No"
                else:
                    self.result = "Yes"
            else:
                if "0" in self.seating:
                    self.result = "No"
                else:
                    self.result = "Yes"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask982ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
