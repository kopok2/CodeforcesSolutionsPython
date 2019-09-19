class CodeforcesTask1145BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        spells = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        if self.n <= 10:
            self.result = "YES" if "n" not in spells[self.n - 1] else "NO"
        elif self.n == 12:
            self.result = "YES"
        elif 10 < self.n < 20:
            self.result = "NO"
        else:
            bignum = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
            if "n" in bignum[int(str(self.n)[0]) - 2]:
                self.result = "NO"
            else:
                if int(str(self.n)[1]):
                    if "n" in spells[int(str(self.n)[1])- 1]:
                        self.result = "NO"
                    else:
                        self.result = "YES"
                else:
                    self.result = "YES"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1145BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
