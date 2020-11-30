def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


class CodeforcesTask49BSolution:
    def __init__(self):
        self.result = ''
        self.expression = []

    def read_input(self):
        self.expression = [int(x) for x in input().split(" ")]

    def process_task(self):
        nums = str(self.expression[0]) + str(self.expression[1])
        base = max([int(c) for c in nums]) + 1
        num1 = int(str(self.expression[0]), base)
        num2 = int(str(self.expression[1]), base)
        self.result = str(len(baseN(num1 + num2, base)))


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask49BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
