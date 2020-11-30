class CodeforcesTask989BSolution:
    def __init__(self):
        self.result = ''
        self.n_p = []
        self.records = []

    def read_input(self):
        self.n_p = [int(x) for x in input().split(" ")]
        self.records = list(input())

    def process_task(self):
        fixed = True
        for x in range(self.n_p[0] - self.n_p[1]):
            if self.records[x + self.n_p[1]] == "." and self.records[x] == ".":
                self.records[x] = "1"
                self.records[x + self.n_p[1]] = "0"
                fixed = False
                break
            if self.records[x + self.n_p[1]] == ".":
                self.records[x + self.n_p[1]] = "1" if self.records[x] == "0" else "0"
                fixed = False
                break
            if self.records[x] == ".":
                self.records[x] = "1" if self.records[x + self.n_p[1]] == "0" else "0"
                fixed = False
                break
            if self.records[x] == "1" and self.records[x + self.n_p[1]] == "0":
                fixed = False
                break
            if self.records[x] == "0" and self.records[x + self.n_p[1]] == "1":
                fixed = False
                break
        if not fixed:
            self.result = "".join(self.records).replace(".", "0")
        else:
            self.result = "No"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask989BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
