class CodeforcesTask1055ASolution:
    def __init__(self):
        self.result = ''
        self.n_s = []
        self.line1 = []
        self.line2 = []

    def read_input(self):
        self.n_s = [int(x) for x in input().split(" ")]
        self.line1 = [int(x) for x in input().split(" ")]
        self.line2 = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.line1[0]:
            if self.line1[self.n_s[1] - 1]:
                self.result = "YES"
            else:
                if self.line2[self.n_s[1] - 1]:
                    can = False
                    for x in range(self.n_s[1], self.n_s[0]):
                        if self.line1[x] and self.line2[x]:
                            can = True
                            break
                    self.result = "YES" if can else "NO"
                else:
                    self.result = "NO"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1055ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
