class CodeforcesTask131ASolution:
    def __init__(self):
        self.result = ''
        self.word = ''

    def read_input(self):
        self.word = input()

    def process_task(self):
        change = True
        for c in self.word[1:]:
            if c.islower():
                change = False
        if change:
            lo = True
            for c in self.word:
                if not c.isupper():
                    lo = False
            if lo:
                self.result = self.word.lower()
            else:
                self.result = self.word[0].upper() + self.word[1:].lower()
        else:
            self.result = self.word

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask131ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
