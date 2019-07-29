class CodeforcesTask1008ASolution:
    def __init__(self):
        self.result = ''
        self.word = ''

    def read_input(self):
        self.word = input()

    def process_task(self):
        vowels = {"a", "o", "u", "i", "e", "n"}
        valid = True
        validating = False
        x = 0
        while x < len(self.word):
            c = self.word[x]
            if c in vowels:
                if validating:
                    if c != "n":
                        validating = False
                    else:
                        valid = False
                        break
            else:
                if validating:
                    valid = False
                    break
                else:
                    validating = True
            x += 1
        if valid:
            valid = not validating
        if valid:
            self.result = "YES"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1008ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
