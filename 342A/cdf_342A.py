class CodeforcesTask342ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        counts = [0 for x in range(1, 8)]
        for x in range(self.n):
            counts[self.sequence[x] - 1] += 1
        if max(counts) > self.n // 3:
            self.result = "-1"
        elif counts[0] != self.n // 3:
            self.result = "-1"
        elif 7 in self.sequence or 5 in self.sequence:
            self.result = "-1"
        else:
            self.result = []
            while counts[3]:
                counts[3] -= 1
                if counts[1]:
                    counts[0] -= 1
                    counts[1] -= 1
                    self.result.append("1 2 4\n")
            while counts[5]:
                counts[5] -= 1
                if counts[2]:
                    counts[0] -= 1
                    counts[2] -= 1
                    self.result.append("1 3 6\n")
                elif counts[1]:
                    counts[0] -= 1
                    counts[1] -= 1
                    self.result.append("1 2 6\n")
            if sum(counts):
                self.result = "-1"
            else:
                for r in self.result:
                    print(r)
                self.result = ""

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask342ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
