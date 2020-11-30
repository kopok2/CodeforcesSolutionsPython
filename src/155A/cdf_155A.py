class CodeforcesTask155ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.performance = []

    def read_input(self):
        self.n = int(input())
        self.performance = [int(x) for x in input().split(" ")]

    def process_task(self):
        mx = mn = self.performance[0]
        amaze = 0
        for a in self.performance[1:]:
            if a > mx:
                mx = a
                amaze += 1
            elif a < mn:
                mn = a
                amaze += 1
        self.result = str(amaze)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask155ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
