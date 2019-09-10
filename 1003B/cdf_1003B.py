class CodeforcesTask1003BSolution:
    def __init__(self):
        self.result = ''
        self.a_b_x = []

    def read_input(self):
        self.a_b_x = [int(x) for x in input().split(" ")]

    def process_task(self):
        result = []
        starting = "0" if self.a_b_x[0] >= self.a_b_x[1] else "1"
        second = "1" if self.a_b_x[0] >= self.a_b_x[1] else "0"
        c = True
        for x in range(self.a_b_x[2] - 1):
            if c:
                result.append(starting)
                c = not c
                if starting == "0":
                    self.a_b_x[0] -= 1
                else:
                    self.a_b_x[1] -= 1
            else:
                result.append(second)
                c = not c
                if second == "0":
                    self.a_b_x[0] -= 1
                else:
                    self.a_b_x[1] -= 1
        if c:
            if starting == "0":
                result.append(starting * self.a_b_x[0])
                result.append(second * self.a_b_x[1])
            else:
                result.append(starting * self.a_b_x[1])
                result.append(second * self.a_b_x[0])
        else:
            if starting == "0":
                result.append(second * self.a_b_x[1])
                result.append(starting * self.a_b_x[0])
            else:
                result.append(second * self.a_b_x[0])
                result.append(starting * self.a_b_x[1])
        self.result = "".join(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1003BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
