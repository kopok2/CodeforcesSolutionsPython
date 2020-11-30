class CodeforcesTask227ASolution:
    def __init__(self):
        self.result = ''
        self.a = []
        self.b = []
        self.c = []

    def read_input(self):
        self.a = [int(x) for x in input().split(" ")]
        self.b = [int(x) for x in input().split(" ")]
        self.c = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.a[0] == self.b[0]:
            if self.c[0] == self.a[0]:
                self.result = "towards"
            elif self.c[0] > self.a[0]:
                if self.b[1] > self.a[1]:
                    self.result = "right"
                else:
                    self.result = "left"
            else:
                if self.b[1] > self.a[1]:
                    self.result = "left"
                else:
                    self.result = "right"
        else:
            a = (self.b[1] - self.a[1]) / (self.b[0] - self.a[0])
            b = self.a[1] - a * self.a[0]
            way = lambda x: a * x + b
            #print(way(self.c[0]), round(way(self.c[0])), self.c[1])
            if round(way(self.c[0])) == self.c[1]:
                self.result = "towards"
            elif not a:
                if self.a[0] < self.b[0]:
                    if self.c[1] > 0:
                        self.result = "left"
                    else:
                        self.result = "right"
                else:
                    if self.c[1] > 0:
                        self.result = "right"
                    else:
                        self.result = "left"
            elif a > 0:
                if self.a[0] < self.b[0]:
                    if self.c[1] > self.b[1]:
                        self.result = "left"
                    else:
                        self.result = "right"
                else:
                    if self.c[1] > self.b[1]:
                        self.result = "right"
                    else:
                        self.result = "left"
            else:
                if self.a[0] < self.b[0]:
                    if self.c[1] > self.b[1]:
                        self.result = "left"
                    else:
                        self.result = "right"
                else:
                    if self.c[1] > self.b[1]:
                        self.result = "right"
                    else:
                        self.result = "left"
        self.result = self.result.upper()

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask227ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
