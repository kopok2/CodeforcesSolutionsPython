class CodeforcesTask398ASolution:
    def __init__(self):
        self.result = ''
        self.a_b = []

    def read_input(self):
        self.a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.a_b[0] ** 2 >=  2 * ((self.a_b[1] // 2) ** 2):
            score = self.a_b[0] ** 2
            if self.a_b[1] % 2:
                score -= ((self.a_b[1] - 1) // 2) ** 2 + ((self.a_b[1] - 1) // 2 + 1) ** 2
                deck = "x" * ((self.a_b[1] - 1) // 2) + "o" * self.a_b[0] + "x" * ((self.a_b[1] - 1) // 2 + 1)
            else:
                score -= ((self.a_b[1]) // 2) ** 2 + ((self.a_b[1]) // 2) ** 2
                deck = "x" * ((self.a_b[1]) // 2) + "o" * self.a_b[0] + "x" * ((self.a_b[1]) // 2)
            self.result = "{0}\n{1}".format(score, deck)
        else:
            if self.a_b[0]:
                division = self.a_b[0] + 1
                score = self.a_b[0] - (division - 1) * ((self.a_b[1] // division) ** 2) - (self.a_b[1] // division + self.a_b[1] % division) ** 2
                step = "x" * (self.a_b[1] // division) + "o"
                deck = step * (division - 1) + "x" * (self.a_b[1] % self.a_b[0])
                self.result = "{0}\n{1}".format(score, deck)
            else:
                score = - self.a_b[1] ** 2
                self.result = "{0}\n{1}".format(score, "x" * self.a_b[1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask398ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
