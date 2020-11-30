from collections import defaultdict


class CodeforcesTask518BSolution:
    def __init__(self):
        self.result = ''
        self.s = ''
        self.t = ''

    def read_input(self):
        self.s = input()
        self.t = input()

    def process_task(self):
        letters = defaultdict(int)
        for c in self.t:
            letters[c] += 1
        yays = 0
        whoops = 0
        done = [0] * len(self.s)
        for x in range(len(self.s)):
            c = self.s[x]
            if letters[c]:
                done[x] = 1
                letters[c] -= 1
                yays += 1
        for x in range(len(self.s)):
            if not done[x]:
                c = self.s[x].swapcase()
                if letters[c]:
                    letters[c] -= 1
                    whoops += 1
        self.result = f"{yays} {whoops}"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask518BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
