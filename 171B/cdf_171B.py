def star(n, starn_prev):
    if n == 1:
        return 1
    elif n == 2:
        return 13
    else:
        return starn_prev + 18 + 6 * (1 + 2 * (n - 3))


class CodeforcesTask171BSolution:
    def __init__(self):
        self.result = ''
        self.a = 0

    def read_input(self):
        self.a = int(input())

    def process_task(self):
        current = 0
        for x in range(1, self.a + 1):
            prev = current
            current = star(x, prev)
        self.result = str(current)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask171BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
