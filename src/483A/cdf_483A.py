import math


class CodeforcesTask483ASolution:
    def __init__(self):
        self.result = ''
        self.l_r = []

    def read_input(self):
        self.l_r = [int(x) for x in input().split(" ")]

    def process_task(self):
        sol = False
        for a in range(self.l_r[0], self.l_r[1] + 1):
            for b in range(a + 1, self.l_r[1] + 1):
                for c in range(b + 1, self.l_r[1] + 1):
                    if int(math.gcd(a, b)) == 1 and int(math.gcd(b, c)) == 1 and int(math.gcd(a, c)) != 1:
                        self.result = "{0} {1} {2}".format(a, b, c)
                        sol = True
        if not sol:
            self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask483ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
