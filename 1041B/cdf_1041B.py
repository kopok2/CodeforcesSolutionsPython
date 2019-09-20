import math


class CodeforcesTask1041BSolution:
    def __init__(self):
        self.result = ''
        self.a_b_x_y = []

    def read_input(self):
        self.a_b_x_y = [int(x) for x in input().split(" ")]

    def process_task(self):
        f = int(math.gcd(self.a_b_x_y[2], self.a_b_x_y[3]))
        dw = self.a_b_x_y[3] // f
        dh = self.a_b_x_y[2] // f
        valid_widths = self.a_b_x_y[0] // dh
        valid_heights = self.a_b_x_y[1] // dw
        self.result = str(min(valid_heights, valid_widths))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1041BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
