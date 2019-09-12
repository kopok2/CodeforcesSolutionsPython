class CodeforcesTask748BSolution:
    def __init__(self):
        self.result = ''
        self.pattern = ''
        self.real = ''

    def read_input(self):
        self.pattern = input()
        self.real = input()

    def process_task(self):
        if self.pattern == self.real:
            self.result = "0"
        else:
            mapping = {}
            remapping = {}
            wrong = False
            for x in range(len(self.pattern)):
                if self.pattern[x] in mapping:
                    if mapping[self.pattern[x]] != self.real[x]:
                        wrong = True
                        break
                else:
                    if self.real[x] not in mapping:
                        mapping[self.pattern[x]] = self.real[x]
                        if self.real[x] not in remapping:
                            remapping[self.real[x]] = self.pattern[x]
                        else:
                            if remapping[self.real[x]] != self.pattern[x]:
                                wrong = True
                                break
                    else:
                        if mapping[self.real[x]] != self.pattern[x]:
                            wrong = True
                            break
            if not wrong:
                self.result = "{0}\n{1}".format(len(["{0} {1}".format(key, value)
                                                           for key, value in mapping.items() if key != value]),
                                                "\n".join(["{0} {1}".format(key, value)
                                                           for key, value in mapping.items() if key != value]))
            else:
                self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask748BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
