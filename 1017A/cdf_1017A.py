class CodeforcesTask1017ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.marks = []

    def read_input(self):
        self.n = int(input())
        for a in range(self.n):
            self.marks.append((400 - sum([int(x) for x in input().split(" ")]), a))

    def process_task(self):
        self.marks.sort()
        for i in range(self.n):
            if self.marks[i][1] == 0:
                self.result = str(i + 1)
                break

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1017ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
