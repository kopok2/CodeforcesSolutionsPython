class CodeforcesTask382ASolution:
    def __init__(self):
        self.result = ''
        self.pans = []
        self.weights = ''

    def read_input(self):
        self.pans = input().split("|")
        self.weights = input()

    def process_task(self):
        if (sum([len(x) for x in self.pans]) + len(self.weights)) % 2:
            self.result = "Impossible"
        else:
            r = (sum([len(x) for x in self.pans]) + len(self.weights)) // 2
            if max([len(x) for x in self.pans]) <= r:
                if r - len(self.pans[0]):
                    self.pans[0] += self.weights[:r - len(self.pans[0])]
                if r - len(self.pans[1]):
                    self.pans[1] += self.weights[-r + len(self.pans[1]):]
                self.result = "|".join(self.pans)
            else:
                self.result = "Impossible"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask382ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
