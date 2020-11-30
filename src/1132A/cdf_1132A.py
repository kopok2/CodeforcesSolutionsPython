class CodeforcesTask1132ASolution:
    def __init__(self):
        self.result = ''
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.c4 = 0

    def read_input(self):
        self.c1 = int(input())
        self.c2 = int(input())
        self.c3 = int(input())
        self.c4 = int(input())

    def process_task(self):
        opened_brackets = 0
        opened = False
        if self.c1:
            opened = True
            opened_brackets += self.c1
        if self.c3:
            opened = True
        if self.c4:
            opened = opened_brackets - self.c4 != 0
        self.result = "0" if opened else "1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1132ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
