def capacity(n):
    result = n
    for x in range(n - 2, 0, -2):
        result += 2 * x
    return result


class CodeforcesTask201ASolution:
    def __init__(self):
        self.result = ''
        self.x = 0

    def read_input(self):
        self.x = int(input())

    def process_task(self):
        if self.x == 3:
            self.result = "5"
        else:
            for x in range(16):
                if x % 2:
                    s = capacity(x)
                    if s >= self.x:
                        self.result = str(x)
                        break

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask201ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
