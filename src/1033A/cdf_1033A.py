class CodeforcesTask1033ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.king = []
        self.queen = []
        self.target = []

    def read_input(self):
        self.n = int(input())
        self.queen = [int(x) for x in input().split(" ")]
        self.king = [int(x) for x in input().split(" ")]
        self.target = [int(x) for x in input().split(" ")]

    def process_task(self):
        can = False
        if self.queen[0] < self.king[0] and self.queen[0] < self.target[0]:
            if self.queen[1] < self.king[1] and self.queen[1] < self.target[1]:
                can = True
            elif self.queen[1] > self.king[1] and self.queen[1] > self.target[1]:
                can = True
        elif self.queen[0] > self.king[0] and self.queen[0] > self.target[0]:
            if self.queen[1] < self.king[1] and self.queen[1] < self.target[1]:
                can = True
            elif self.queen[1] > self.king[1] and self.queen[1] > self.target[1]:
                can = True
        self.result = "YES" if can else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1033ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
