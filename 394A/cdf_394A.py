class CodeforcesTask394ASolution:
    def __init__(self):
        self.result = ''
        self.expression = ''

    def read_input(self):
        self.expression = input()

    def process_task(self):
        expr = self.expression.split("=")
        c = len(expr[1])
        a = len(expr[0].split("+")[0])
        b = len(expr[0].split("+")[1])
        # print(a, b, c)
        diff = abs((a + b) - c)
        if diff == 0 or diff == 2:
            if c > a + b:
                a += 1
                c -= 1
                self.result = "|" * a + "+" + "|" * b + "=" + "|" * c
            elif not diff:
                self.result = self.expression
            elif a + b > 2:
                if a > 1:
                    a -= 1
                else:
                    b -= 1
                c += 1
                self.result = "|" * a + "+" + "|" * b + "=" + "|" * c
            else:
                self.result = "Impossible"
        else:
            self.result = "Impossible"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask394ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
