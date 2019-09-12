class CodeforcesTask518ASolution:
    def __init__(self):
        self.result = ''
        self.s = ''
        self.t = ''

    def read_input(self):
        self.s = list(input())
        self.t = list(input())

    def process_task(self):
        for x in range(len(self.t)):
            if self.t[- x - 1] != "a":
                self.t[- x - 1] = chr(ord(self.t[- x - 1]) - 1)
                for y in range(len(self.t) - x, len(self.t)):
                    self.t[y] = "z"
                break
        if "".join(self.s) < "".join(self.t):
            self.result = "".join(self.t)
        else:
            self.result = "No such string"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask518ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
