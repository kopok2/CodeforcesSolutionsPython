from operator import itemgetter
import math
import fractions


def res(a, b, x, y, low):
    if low:
        return abs(fractions.Fraction(x, y) - fractions.Fraction(a, b))
    else:
        return abs((x / y) - (a / b))


class CodeforcesTask281BSolution:
    def __init__(self):
        self.result = ''
        self.x_y_n = []

    def read_input(self):
        self.x_y_n = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.x_y_n[2] >= self.x_y_n[1]:
            a, b = self.x_y_n[0], self.x_y_n[1]
            while not math.gcd(a, b) == 1:
                g = math.gcd(a, b)
                a //= g
                b //= g
            self.result = "{0}/{1}".format(a, b)
        else:
            results = []
            base = self.x_y_n[0] / self.x_y_n[1]
            l = self.x_y_n[2] < 100
            for den in range(1, self.x_y_n[2] + 1):
                a2 = int(base * den)
                a1 = a2 - 1
                a3 = a2 + 1
                results.append((res(a1, den, self.x_y_n[0], self.x_y_n[1], l), a1, den))
                results.append((res(a2, den, self.x_y_n[0], self.x_y_n[1], l), a2, den))
                results.append((res(a3, den, self.x_y_n[0], self.x_y_n[1], l), a3, den))
            results.sort(key=itemgetter(0))
            #print(results)
            a, b = results[0][1], results[0][2]
            while not math.gcd(a, b) == 1:
                g = math.gcd(a, b)
                a //= g
                b //= g
            self.result = "{0}/{1}".format(a, b)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask281BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
