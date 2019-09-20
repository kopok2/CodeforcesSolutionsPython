import math


class CodeforcesTask114ASolution:
    def __init__(self):
        self.result = ''
        self.k = 0
        self.l = 0

    def read_input(self):
        self.k = int(input())
        self.l = int(input())

    def process_task(self):
        is_ = False
        re = 0
        for x in range(int(math.log(self.l, self.k)) + 2):
            if self.l == self.k ** x:
                re = x
                is_ = True
                break
        self.result = "YES\n{0}".format(re - 1) if is_ else "NO"


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask114ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
