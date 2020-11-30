class CodeforcesTask709ASolution:
    def __init__(self):
        self.result = ''
        self.n_b_d = []
        self.oranges = []

    def read_input(self):
        self.n_b_d = [int(x) for x in input().split(" ")]
        self.oranges = [int(x) for x in input().split(" ")]

    def process_task(self):
        emp = 0
        cont = 0
        for orange in self.oranges:
            if orange <= self.n_b_d[1]:
                cont += orange
                if cont > self.n_b_d[2]:
                    cont = 0
                    emp += 1
        self.result = str(emp)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask709ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
