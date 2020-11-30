class CodeforcesTask378ASolution:
    def __init__(self):
        self.result = ''
        self.a_b = []

    def read_input(self):
        self.a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        ways = [0, 0, 0]
        for x in range(1, 7):
            if abs(x - self.a_b[0]) < abs(x - self.a_b[1]):
                ways[0] += 1
            elif abs(x - self.a_b[0]) == abs(x - self.a_b[1]):
                ways[1] += 1
            else:
                ways[2] += 1
        self.result = "{0} {1} {2}".format(*ways)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask378ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
