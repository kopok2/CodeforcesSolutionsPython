class CodeforcesTask991BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.grades = []

    def read_input(self):
        self.n = int(input())
        self.grades = [int(x) for x in input().split(" ")]

    def process_task(self):
        work = 0
        ss = sum(self.grades)
        while round(ss / self.n + 0.00001) < 5:
            #print(self.grades, round(ss / self.n ), ss / self.n)
            self.grades.sort()
            ss += 5
            ss -= self.grades[0]
            self.grades[0] = 5
            work += 1
        self.result = str(work)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask991BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
