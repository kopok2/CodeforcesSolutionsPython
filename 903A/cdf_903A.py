class CodeforcesTask903ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.tests = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.tests.append(int(input()))

    def process_task(self):
        results = []
        for x in range(self.n):
            can_be = False
            for a in range(33):
                for b in range(14):
                    if 3 * a + 7 * b == self.tests[x]:
                        can_be = True
                        break
            if can_be:
                results.append("YES")
            else:
                results.append("NO")
        self.result = "\n".join(results)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask903ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
