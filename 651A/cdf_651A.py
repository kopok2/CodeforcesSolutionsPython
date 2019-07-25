class CodeforcesTask651ASolution:
    def __init__(self):
        self.result = ''
        self.a1_a2 = []

    def read_input(self):
        self.a1_a2 = [int(x) for x in input().split(" ")]

    def process_task(self):
        time = 0
        while min(self.a1_a2) > 0 and sum(self.a1_a2) >= 3:
            time += 1
            if self.a1_a2[0] >= self.a1_a2[1]:
                self.a1_a2[0] -= 2
                self.a1_a2[1] += 1
            else:
                self.a1_a2[0] += 1
                self.a1_a2[1] -= 2
        self.result = str(time)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask651ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
