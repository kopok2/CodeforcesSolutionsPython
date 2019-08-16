class CodeforcesTask371BSolution:
    def __init__(self):
        self.result = ''
        self.a_b = []

    def read_input(self):
        self.a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        a1 = 0
        a2 = 0
        a3 = 0
        while not self.a_b[0] % 2:
            self.a_b[0] //= 2
            a1 += 1
        while not self.a_b[0] % 3:
            self.a_b[0] //= 3
            a2 += 1
        while not self.a_b[0] % 5:
            self.a_b[0] //= 5
            a3 += 1
        x = self.a_b[0]
        b1 = 0
        b2 = 0
        b3 = 0
        while not self.a_b[1] % 2:
            self.a_b[1] //= 2
            b1 += 1
        while not self.a_b[1] % 3:
            self.a_b[1] //= 3
            b2 += 1
        while not self.a_b[1] % 5:
            self.a_b[1] //= 5
            b3 += 1
        y = self.a_b[1]
        if x != y:
            self.result = "-1"
        else:
            self.result = str(abs(a1 - b1) + abs(a2 - b2) + abs(a3 - b3))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask371BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
