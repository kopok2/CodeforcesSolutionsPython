class CodeforcesTask47BSolution:
    def __init__(self):
        self.result = ''
        self.weightings = []

    def read_input(self):
        for x in range(3):
            self.weightings.append(input())

    def process_task(self):
        for x in range(3):
            if ">" in self.weightings[x]:
                self.weightings[x] = self.weightings[x][::-1].replace(">", "<")
        mn = [0] * 3
        for x in range(3):
            mn[ord(self.weightings[x][0]) - ord("A")] += 1
        if mn == [1, 1, 1]:
            self.result = "Impossible"
        else:
            self.result = "{0}{1}{2}".format(chr(ord("A") + mn.index(2)), chr(ord("A") + mn.index(1)), chr(ord("A") + mn.index(0)))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask47BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
