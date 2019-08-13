import math


class CodeforcesTask221BSolution:
    def __init__(self):
        self.result = ''
        self.x = 0

    def read_input(self):
        self.x = int(input())

    def process_task(self):
        if self.x == 1:
            self.result = "1"
        else:
            numix = 1
            repo = str(self.x)
            if "1" in repo:
                numix += 1
            for x in range(2, int(math.sqrt(self.x)) + 1):
                if x < self.x:
                    if not self.x % x:
                        #print(x, self.x // x)
                        have = False
                        for c in str(x):
                            if c in repo:
                                have = True
                                break
                        if have:
                            numix += 1
                        if self.x // x != x:
                            have = False
                            for c in str(self.x // x):
                                if c in repo:
                                    have = True
                                    break
                            if have:
                                numix += 1
            self.result = str(numix)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask221BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
