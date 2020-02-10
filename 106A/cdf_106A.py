class CodeforcesTask106ASolution:
    def __init__(self):
        self.result = ''
        self.trump = ''
        self.cards = []

    def read_input(self):
        self.trump = input()
        self.cards = input().split(" ")

    def process_task(self):
        order = "6789TJQKA"
        if self.trump == self.cards[0][1]:
            if self.trump == self.cards[1][1]:
                if order.index(self.cards[0][0]) > order.index(self.cards[1][0]):
                    self.result = "YES"
                else:
                    self.result = "NO"
            else:
                self.result = "YES"
        else:
            if self.cards[0][1] == self.cards[1][1]:
                if order.index(self.cards[0][0]) > order.index(self.cards[1][0]):
                    self.result = "YES"
                else:
                    self.result = "NO"
            else:
                self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask106ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
