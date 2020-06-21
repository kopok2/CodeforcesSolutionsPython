class CodeforcesTask664BSolution:
    def __init__(self):
        self.result = ''
        self.equation = ''

    def read_input(self):
        self.equation = input()

    def process_task(self):
        n = int(self.equation.split('=')[1].strip())
        left_eq = self.equation.split('=')[0]
        plus = 1 + left_eq.count('+')
        minus = left_eq.count('-')
        if plus - minus * n <= n <= plus * n - minus:
            val = n * plus - minus
            values = [n] * plus + [-1] * minus
            changing = 0
            while val != n:
                if changing < plus:
                    if val - n >= n - 1:
                        values[changing] = 1
                        val -= n - 1
                    else:
                        values[changing] -= val - n
                        val = n
                else:
                    if val - n >= n - 1:
                        values[changing] = -n
                        val -= n - 1
                    else:
                        values[changing] +=  - val + n
                        val = n
                changing += 1
            sign_str = ("+" + self.equation.split('=')[0]).replace(" ", "").replace("+?", "+|").replace("-?", "-|")[:-1]

            plus_values = values[:plus]
            minus_values = values[plus:]
            eq_string = ''
            for sign in sign_str.split("|"):
                    vl = plus_values.pop(0) if sign == "+" else minus_values.pop(0)
                    eq_string += sign + " " + str(abs(vl)) + " "
            eq_string += "= " + str(n)
            eq_string = eq_string[2:]

            self.result = "Possible\n" + eq_string
        else:
            self.result = "Impossible"


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask664BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
