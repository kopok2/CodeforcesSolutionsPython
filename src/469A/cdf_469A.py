class CodeforcesTask469ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.l1 = []
        self.l2 = []

    def read_input(self):
        self.n = int(input())
        self.l1 = [int(x) for x in input().split(" ")]
        self.l2 = [int(x) for x in input().split(" ")]

    def process_task(self):
        to_pass = set([x + 1 for x in range(self.n)])
        passable = set(self.l1[1:] + self.l2[1:])
        if to_pass == passable:
            self.result = "I become the guy."
        else:
            self.result = "Oh, my keyboard!"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask469ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
