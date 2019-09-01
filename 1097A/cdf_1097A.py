class CodeforcesTask1097ASolution:
    def __init__(self):
        self.result = ''
        self.table = ''
        self.deck = []

    def read_input(self):
        self.table = input()
        self.deck = input().split(" ")

    def process_task(self):
        self.result = "NO"
        for x in range(5):
            if self.table[0] == self.deck[x][0] or self.table[1] == self.deck[x][1]:
                self.result = "YES"
                break

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1097ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
