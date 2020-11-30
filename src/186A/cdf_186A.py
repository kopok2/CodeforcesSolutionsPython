class CodeforcesTask186ASolution:
    def __init__(self):
        self.result = ''
        self.g1 = ''
        self.g2 = ''

    def read_input(self):
        self.g1 = list(input())
        self.g2 = list(input())

    def process_task(self):
        if len(self.g1) != len(self.g2):
            self.result = "NO"
        else:
            can_ = True
            d1 = None
            d2 = None
            for x in range(len(self.g1)):
                if self.g1[x] != self.g2[x]:
                    if d1:
                        d2 = x + 1
                    else:
                        d1 = x + 1
            if d1 and d2:
                #print(self.g1, self.g2)
                #print(d1, d2)
                self.g1[d1 - 1], self.g1[d2 - 1] = self.g1[d2 - 1], self.g1[d1 - 1]
                self.g1 = "".join(self.g1)
                self.g2 = "".join(self.g2)
                #print(self.g1, self.g2)
                can_ = self.g1 == self.g2
            elif not d1 and not d2:
                can_ = True
            else:
                can_ = False

            self.result = "YES" if can_ else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask186ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
