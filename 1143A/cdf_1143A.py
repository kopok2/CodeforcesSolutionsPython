class CodeforcesTask1143ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.doors = []

    def read_input(self):
        self.n = int(input())
        self.doors = [int(x) for x in input().split(" ")]

    def process_task(self):
        rights = sum(self.doors)
        x = 0
        opened_right = 0
        while opened_right < rights:
            opened_right += self.doors[x]
            x += 1
            if self.n - x == rights - opened_right:
                break
        self.result = str(x)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1143ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
