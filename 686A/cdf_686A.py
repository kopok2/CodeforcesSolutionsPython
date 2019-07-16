class CodeforcesTask686ASolution:
    def __init__(self):
        self.result = ''
        self.n_x = []
        self.operations = []

    def read_input(self):
        self.n_x = [int(x) for x in input().split(" ")]
        for x in range(self.n_x[0]):
            self.operations.append(int(input().replace(" ", "")))

    def process_task(self):
        ice = self.n_x[1]
        distress = 0
        for op in self.operations:
            if op >= 0:
                ice += op
            else:
                if abs(op) > ice:
                    distress += 1
                else:
                    ice += op
        self.result = "{0} {1}".format(ice, distress)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask686ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
