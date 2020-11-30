class CodeforcesTask1105ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sticks = []

    def read_input(self):
        self.n = int(input())
        self.sticks = [int(x) for x in input().split(" ")]

    def process_task(self):
        mn = 10 ** 9
        ct = -1
        for t in range(1, 101):
            tc = 0
            for stick in self.sticks:
                if stick > t:
                    tc += stick - t - 1
                elif stick < t:
                    tc += t - stick - 1
            if tc < mn:
                mn = tc
                ct = t
        self.result = "{0} {1}".format(ct, mn)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1105ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
