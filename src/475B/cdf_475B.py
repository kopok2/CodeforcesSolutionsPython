class CodeforcesTask475BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.horizontal = ''
        self.vertical = ''

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.horizontal = input()
        self.vertical = input()

    def process_task(self):
        if self.horizontal[0] == ">" and self.vertical[-1] == "^":
            self.result = "NO"
        elif self.horizontal[-1] == ">" and self.vertical[-1] == "v":
            self.result = "NO"
        elif self.horizontal[0] == "<" and self.vertical[0] == "^":
            self.result = "NO"
        elif self.horizontal[-1] == "<" and self.vertical[0] == "v":
            self.result = "NO"
        else:
            self.result = "YES"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask475BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
