def findlcm(a, b):
    if(a > b):
        maximum = a
    else:
        maximum = b

    while(True):
        if(maximum % a == 0 and maximum % b == 0):
            lcm = maximum;
            break;
        maximum = maximum + 1
    return lcm

class CodeforcesTask340ASolution:
    def __init__(self):
        self.result = ''
        self.x_y_a_b = []

    def read_input(self):
        self.x_y_a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        mult = findlcm(self.x_y_a_b[0], self.x_y_a_b[1])
        res = 0
        left = self.x_y_a_b[2] if not self.x_y_a_b[2] % mult else mult + (self.x_y_a_b[2] // mult) * mult
        right = self.x_y_a_b[3] if not self.x_y_a_b[3] % mult else (self.x_y_a_b[3] // mult) * mult
        res = right // mult - left // mult + 1
        self.result = str(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask340ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
