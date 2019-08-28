def is_valid(a, b, x):
    return not a % b and a * b > x and a / b < x


class CodeforcesTask1088ASolution:
    def __init__(self):
        self.result = ''
        self.x = 0

    def read_input(self):
        self.x = int(input())

    def process_task(self):
        aa = 0
        bb = 0
        found = False
        for a in range(1, self.x + 1):
            for b in range(1, self.x + 1):
                if is_valid(a, b, self.x):
                    aa = a
                    bb = b
                    found = True
                    break
            if found:
                break
        if aa * bb:
            self.result = "{0} {1}".format(aa, bb)
        else:
            self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1088ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
