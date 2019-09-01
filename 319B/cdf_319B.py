class CodeforcesTask319BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.psychos = []

    def read_input(self):
        self.n = int(input())
        self.psychos = [int(x) for x in input().split(" ")]

    def process_task(self):
        changed = True
        steps = 0
        while changed:
            changed = False
            safe = 1
            newline = [self.psychos[0]]
            for x in range(len(self.psychos) - 1):
                if self.psychos[x + 1] > self.psychos[x]:
                    newline.append(self.psychos[x + 1])
                    safe += 1
            if safe == len(self.psychos):
                changed = False
            else:
                changed = True
                self.psychos = newline
            if changed:
                steps += 1
        self.result = str(steps)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask319BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
