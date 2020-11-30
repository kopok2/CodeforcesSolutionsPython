import math


class CodeforcesTask1033BSolution:
    def __init__(self):
        self.result = ''
        self.t = 0
        self.tests = []

    def read_input(self):
        self.t = int(input())
        for x in range(self.t):
            self.tests.append([int(y) for y in input().split(" ")])

    def process_task(self):
        results = []
        for test in self.tests:
            c = test[0] - test[1]
            if c == 1:
                is_prime = True
                d = sum(test)
                for x in range(2, int(math.sqrt(d)) + 1):
                    if not d % x:
                        is_prime = False
                        break
            else:
                is_prime = False
            results.append("YES" if is_prime else "NO")
        self.result = "\n".join(results)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1033BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
