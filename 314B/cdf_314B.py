import math


def a_can_from_b(a, b):
    pt = 0
    for chr in a:
        try:
            while b[pt] != chr:
                pt += 1
        except IndexError:
            return False
    return True



class CodeforcesTask314BSolution:
    def __init__(self):
        self.result = ''
        self.b_d = []
        self.a = ''
        self.c = ''

    def read_input(self):
        self.b_d = [int(x) for x in input().split(" ")]
        self.a = input()
        self.c = input()

    def process_task(self):
        left = 1
        right = math.ceil(self.b_d[0] / self.b_d[1])
        while right - left > 1:

            mid = left + (right - left) // 2
            #print(left, right, mid)
            if a_can_from_b(self.c * (self.b_d[1] * mid), self.a * self.b_d[0]):
                left = mid
            else:
                right = mid
        print(a_can_from_b(self.c * (self.b_d[1] * left), self.a * self.b_d[0]))
        print(self.c * (self.b_d[1] * left), self.a * self.b_d[0])
        print(len(self.a) * self.b_d[0], len(self.c) * (self.b_d[1] * left))
        self.result = str(left)


    def get_result(self):
        return self.result



if __name__ == "__main__":
    Solution = CodeforcesTask314BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
