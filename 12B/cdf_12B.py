class CodeforcesTask12BSolution:
    def __init__(self):
        self.result = ''
        self.number = 0
        self.solution = 0

    def read_input(self):
        self.number = int(input())
        self.solution = input()

    def process_task(self):
        try:
            if len(str(self.solution)) > 1 and str(self.solution)[0] == "0":
                self.result = "WRONG_ANSWER"
            else:
                cnts = [0] * 10
                for c in str(self.number):
                    cnts[int(c)] += 1
                start = min([int(x) for x in str(self.number) if int(x)])
                cnts[start] -= 1
                res = [start]
                for x in range(10):
                    res += [x] * cnts[x]
                real_result = int("".join([str(x) for x in res]))
                self.result = "OK" if real_result == int(self.solution) else "WRONG_ANSWER"
        except ValueError:
            if not self.number and self.solution == "0":
                self.result = "OK"
            else:
                self.result = "WRONG_ANSWER"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask12BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
