class CodeforcesTask259BSolution:
    def __init__(self):
        self.result = ''
        self.square = []

    def read_input(self):
        for x in range(3):
            self.square.append([int(x) for x in input().split(" ")])

    def process_task(self):
        s = self.square
        s[0][0] = (s[1][0] + s[1][2] + s[2][0] + s[2][1] - s[0][1] - s[0][2]) // 2
        s[1][1] = s[2][0] + s[2][1] - s[0][0]
        s[2][2] = s[1][0] + s[1][2] - s[0][0]
        self.result = "{0}\n{1}\n{2}".format(*[" ".join([str(y) for y in x]) for x in s])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask259BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
