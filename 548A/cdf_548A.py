class CodeforcesTask548ASolution:
    def __init__(self):
        self.result = ''
        self.conc = ''
        self.k = 0

    def read_input(self):
        self.conc = input()
        self.k = int(input())

    def process_task(self):
        if len(self.conc) % self.k:
            self.result = "NO"
        else:
            c_ = True
            nl = len(self.conc) // self.k
            for x in range(self.k):
                for y in range(nl):
                    if self.conc[x * nl + y] != self.conc[(x + 1) * nl - y - 1]:
                        c_ = False
                        break
                if not c_:
                    break
            self.result = "YES" if c_ else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask548ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
